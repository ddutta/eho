from behave import *
from random import choice, randint
from string import ascii_lowercase
from sys import path
import RestApi
import json

path.append(path.append(".."))
rest = RestApi.RestApi()

template_ids = []

@When ('User see templates')
def get_templates(context):
    global status_code
    global res_content_list_templates
    global template_ids
    res_content_list_templates = []
    template_ids = []
    res = rest.get_templates()
    status_code = res.status_code
    if status_code == 200:
         res_content_list_templates = json.loads(res.content)

@When ('User see template with id:"{n}"')
def get_template(context, n):
    global status_code
    global res_content_get_template
    res = rest.get_template(template_ids[int(n)])
    status_code = res.status_code
    if status_code == 200:
        res_content_get_template = json.loads(res.content)

# @When('User add template name:"{name}" | image_id:"{im_id}" | n_n:"{n_n}" count_n_n:"{count_n_n}" | d_n:"{d_n}" count_d_n:"{count_d_n}"')
# def create_template_body(context, name, im_id,n_n, count_n_n, d_n, count_d_n):
#     global template_body
#     data = json.dumps(dict(
#         node_template = dict(
#             name = '%s' % (name),
#             node_type = 'JT+NN',
#             flavor_id = '%s' % (f_id),
#             job_tracker = {
#                 'heap_size': '%d'
#             },
#             name_node = {
#                 'heap_size': '2345'
#             }
#         )))
#     cluster_body = data

@When ('User create template')
def add_template(context):
    global template_body
    global status_code
    global res_content
    res = rest.create_template(template_body)
    status_code = res.status_code
    if status_code == 202:
        res_content = json.loads(res.content)
        template_ids.append(res_content.get(u'id'))

@When ('User delete template with id:"{n}"')
def del_template(context, n):
    global status_code
    res = rest.delete_template(template_ids[int(n)])
    status_code = res.status_code

@When ('User put template with id:"{n}"')
def put_template(context, n):
    global status_code
    global res_content
    global template_body
    res = rest.create_template(template_body, template_ids[n])
    status_code = res.status_code
    if status_code == 202:
        res_content = json.loads(res.content)

