from behave import *
from random import choice, randint
from string import ascii_lowercase
from sys import path
from time import sleep

path.append(path.append(".."))

import RestApi
import json
rest = RestApi.RestApi()
cluster_ids = []

@When ('User see clusters')
def get_clusters(context):
    global status_code
    global res_content_list_clusters
    global cluster_ids
    res_content_list_clusters = []
    cluster_ids = []
    res = rest.get_clusters()
    status_code = res.status_code
    if status_code == 200:
        res_content_list_clusters = json.loads(res.content)
        loop = res_content_list_clusters['clusters']
        for x in loop:
            cluster_ids.append(x.pop(u'id'))

@When ('User see cluster with id:"{n}"')
def get_cluster(context, n):
    global status_code
    global res_content_get_cluster
    global cluster_ids
    res = rest.get_cluster(cluster_ids[int(n)])
    status_code = res.status_code
    if status_code == 200:
        res_content_get_cluster = json.loads(res.content)

@When('User add cluster name:"{name}" and image_id:"{im_id}"')
def create_cluster_body(context, name, im_id):
    global cluster_body
    data=json.dumps(dict(
        cluster = dict(
            name = '%s' % (name),
            base_image_id = '%s' % (im_id),
            node_templates = {
                'jt_nn.small': 1,
                'tt_dn.small': 1
            }
        )))
    cluster_body = data

@When ('User create cluster')
def add_cluster(context):
    global cluster_body
    global status_code
    global res_content
    res = rest.create_cluster(cluster_body)
    #sleep(60)
    status_code = res.status_code
    #if status_code == 202:
    #    res_content = eval(res.content)
    #    cluster_ids.append(res_content.get(u'id'))
    
@When ('User delete cluster with id:"{n}"')
def del_cluster(context, n):
    global status_code
    res = rest.delete_cluster(cluster_ids[int(n)])
    status_code = res.status_code

@When ('User put cluster with id:"{n}"')
def put_cluster(context, n):
    global status_code
    global res_content
    data=json.dumps(dict(
        cluster = dict(
            name = 'QA_cluster_%d' % randint(0,100),
            base_image_id = 'd9342ba8-4c51-441c-8d5b-f9e14a901299',
            node_templates = {
                'jt_nn.medium': 1,
                'tt_dn.small': 5
            }
        )))
    res=rest.create_cluster(data, cluster_ids[n])
    status_code = res.status_code
    if status_code == 202:
        res_content = eval(res.content)
