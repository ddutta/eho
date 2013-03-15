from behave import *
from random import choice, randint
from string import ascii_lowercase
from sys import path
import json

path.append(path.append(".."))

import RestApi
rest = RestApi.RestApi()

@When ('User see template')
def get_template(context): 
    global status_code
    res = rest.get_template() 
    status_code = res.status_code

@When ('User create template')
def add_template(context):
    global status_code
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
    
@When ('User delete template')
def del_template(context):
    global status_code
    data = json.dumps(dict(
        node_template = dict(
            name = 'QA_template_16',
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
    res=rest.delete_template(data)
    status_code = res.status_code
