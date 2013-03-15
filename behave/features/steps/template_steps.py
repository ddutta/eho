from behave import *
from random import choice, randint
from string import ascii_lowercase
from sys import path
import json

path.append(path.append(".."))

import RestApi
rest = RestApi.RestApi()
template_ids = []

@When ('User see templates')
def get_templates(context):
    global status_code
    global res_content
    res = rest.get_templates()
    status_code = res.status_code
    if status_code == 200:
        res_content = json.loads(res.content)
        loop = res_content['node_templates']
        print (loop)
        for x in loop:
            template_ids.append(x.pop(u'id'))

@When ('User see template with id:"{n}"')
def get_template(context, n):
    global status_code
    global res_content
    res = rest.get_template(template_ids[n])
    status_code = res.status_code
    if status_code == 200:
        res_content = eval(res.content)

@When ('User create template')
def add_template(context):
    global status_code
    global res_content
    data = json.dumps(dict(
        node_template = dict(
            name = 'QA_template_%d' % randint(0, 100),
            node_type = 'JT+NN',
            flavor_id = 'm1.medium',
            job_tracker = {
        	'heap_size': '384',
		'max_map_tasks': '3',
		'max_reduce_tasks': '1',
		'task_heap_size': '640'
	        },
                name_node = {
                    'heap_size': '2345'
                }
    )))
    res=rest.create_template(data)
    status_code = res.status_code
    if status_code == 202:
        #data = json.loads(res.data)
        res_content = eval(res.content)
        #temp_id = res_content.pop(u'id')
        #template_ids.append(temp_id)
        template_ids.append(res_content.pop(u'id'))


    
@When ('User delete template with id:"{n}"')
def del_template(context, n):
    global status_code
    #temp_id = template_ids[n]
    res=rest.delete_template(template_ids[n])
    status_code = res.status_code

@When ('User put template with id:"{n}"')
def put_template(context, n):
    global status_code
    global res_content
    data = json.dumps(dict(
        node_template = dict(
            name = 'QA_template_%d' % randint(0, 100),
            node_type = 'JT+NN',
            flavor_id = 'm1.medium',
            job_tracker = {
            'heap_size': '384',
            'max_map_tasks': '3',
            'max_reduce_tasks': '1',
            'task_heap_size': '640'
            },
            name_node = {
                'heap_size': '2345'
            }
        )))
    res=rest.create_template(data, template_ids[n])
    status_code = res.status_code
    if status_code == 202:
        res_content = eval(res.content)
