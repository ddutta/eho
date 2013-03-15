from behave import *
from random import choice, randint
from string import ascii_lowercase
from sys import path

path.append(path.append(".."))

import RestApi
rest = RestApi.RestApi()

@When ('User see clusters')
def get_clusters(context):
    global status_code
    res = rest.get_clusters()
    status_code = res.status_code
    #assert status_code == 200

@When ('User create clusters')
def create_cluster(context, cluster):
    global status_code
    res = rest.create_cluster(cluster)
    status_code = res.status_code
    #assert status_code == 200

