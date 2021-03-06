# Copyright (c) 2013 Mirantis Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

from eventlet import monkey_patch
from flask import Flask
from keystoneclient.middleware.auth_token import filter_factory as auth_token
from werkzeug.exceptions import default_exceptions
from werkzeug.exceptions import HTTPException

from eho.server.middleware.auth_valid import filter_factory as auth_valid
from eho.server.scheduler import setup_scheduler
from eho.server.service.api import setup_api
from eho.server.storage.defaults import setup_defaults
from eho.server.utils.api import render
from eho.server.api import v02 as api_v02
from eho.server.storage.storage import setup_storage
from eho.server.service.cluster_ops import setup_ops


monkey_patch(os=True, select=True, socket=True, thread=True, time=True)


def make_app(**local_conf):
    """
    Entry point for Elastic Hadoop on OpenStack REST API server
    """
    app = Flask('eho.api')

    # reading defaults
    app.config.from_pyfile('etc/default.cfg', silent=True)
    app.config.from_pyfile('../etc/default.cfg', silent=True)

    # read local conf
    app.config.from_pyfile('etc/local.cfg', silent=True)
    app.config.from_pyfile('../etc/local.cfg', silent=True)

    app.config.from_envvar('EHO_API_CFG', silent=True)
    app.config.update(**local_conf)

    root_logger = logging.getLogger()
    ll = app.config.pop('LOG_LEVEL', 'WARN')
    if ll:
        root_logger.setLevel(ll)

    app.register_blueprint(api_v02.rest, url_prefix='/v0.2')

    if app.config['DEBUG']:
        print 'Configuration:'
        for k in app.config:
            print '\t%s = %s' % (k, app.config[k])

    setup_storage(app)
    setup_defaults(app)
    setup_scheduler(app)
    setup_ops(app)
    setup_api(app)

    def make_json_error(ex):
        status_code = (ex.code
                       if isinstance(ex, HTTPException)
                       else 500)
        description = (ex.description
                       if isinstance(ex, HTTPException)
                       else str(ex))
        return render({'error': status_code, 'error_message': description},
                      status=status_code)

    for code in default_exceptions.iterkeys():
        app.error_handler_spec[None][code] = make_json_error

    app.wsgi_app = auth_valid(app.config)(app.wsgi_app)

    app.wsgi_app = auth_token(
        app.config,
        auth_host=app.config['OS_AUTH_HOST'],
        auth_port=app.config['OS_AUTH_PORT'],
        auth_protocol=app.config['OS_AUTH_PROTOCOL'],
        admin_user=app.config['OS_ADMIN_USER'],
        admin_password=app.config['OS_ADMIN_PASSWORD'],
        admin_tenant=['OS_ADMIN_TENANT']
    )(app.wsgi_app)

    return app
