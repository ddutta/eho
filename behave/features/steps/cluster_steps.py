from behave import *
from random import choice, randint
from string import ascii_lowercase
from sys import path
from time import sleep

path.append(path.append(".."))

import RestApi
import json
rest = RestApi.RestApi()
global cluster_ids
cluster_ids = []

@When ('User see clusters')
def get_clusters(context):
    global status_code
    global res_content_list_clusters
    res_content_list_clusters = []
    res = rest.get_clusters()
    status_code = res.status_code
    if status_code == 200:
        res_content_list_clusters = json.loads(res.content)

@When ('User see cluster with id:"{n}"')
def get_cluster(context, n):
    global status_code
    global res_content_get_cluster
    res = rest.get_cluster(cluster_ids[int(n)])
    status_code = res.status_code
    if status_code == 200:
        res_content_get_cluster = json.loads(res.content)

@When('name:"{name}" and im_id="{im_id}" and n_n="{n_n}" and count="{count_n_n}" and d_n="{d_n}" and count="{count_d_n}"')
def create_cluster_body(context, name, im_id, n_n, count_n_n, d_n, count_d_n):
    global cluster_body
    data=json.dumps(dict(
        cluster = dict(
            name = '%s' % (name),
            base_image_id = '%s' % (im_id),
            node_templates = {
                '%s' % str(n_n) : count_n_n,
                '%s' % str(d_n) : count_d_n,
            }
        )))
    cluster_body = data

@When ('User create cluster')
def add_cluster(context):
    global cluster_body
    global status_code
    global res_content
    res = rest.create_cluster(cluster_body)
    status_code = res.status_code
    if status_code == 202:
        sleep(60)
        res_content = json.loads(res.content)
        cluster_ids.append(res_content['cluster'].get(u'id'))
    
@When ('User delete cluster with id:"{n}"')
def del_cluster(context, n):
    global status_code
    res = rest.delete_cluster(cluster_ids[int(n)])
    status_code = res.status_code

@When ('User put cluster with id:"{n}"')
def put_cluster(context, n):
    global status_code
    global res_content
    global cluster_body
    res=rest.create_cluster(cluster_body, cluster_ids[int(n)])
    status_code = res.status_code
    if status_code == 202:
        res_content = json.loads(res.content)
