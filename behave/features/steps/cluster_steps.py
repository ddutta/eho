from behave import *
from random import choice, randint
from string import ascii_lowercase
from sys import path

path.append(path.append(".."))

import RestApi
rest = RestApi.RestApi()

@When ('User see cluster')
def get_cluster(context):
    global status_code
    res = rest.get_cluster()
    status_code = res.status_code

@When ('User create cluster')
def add_cluster(context):
    global status_code    
    data=json.dumps(dict(
        cluster = dict(
	name = 'QA_cluster_%d' % randint(0,100),
	base_image_id = 'd9342ba8-4c51-441c-8d5b-f9e14a901299',
        node_templates = {
            'jt_nn.medium': 1,
            'tt_dn.small': 5
        }
    )))
    res = rest.create_cluster(data)
    status_code = res.status_code
    
@When ('User delete cluster')
def del_cluster(context):
    global status_code    
    data = json.dumps(dict(
        cluster = dict(
	name = 'QA_cluster_93',
	base_image_id = 'd9342ba8-4c51-441c-8d5b-f9e14a901299',
        node_templates = {
            'jt_nn.medium': 1,
            'tt_dn.small': 5
        }
    )))
    res = rest.delete_cluster(data)
    status_code = res.status_code

