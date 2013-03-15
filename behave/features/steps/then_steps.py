from behave import *
from re import match, search

@Then('Response is "{res_code}"')
def chkStatus(context, res_code):
    global status_code
    print("%s == %s" % (status_code, res_code))
    assert status_code == int(res_code.strip())

@Then('Response list of list clusters:"{list}"')
def response_list_clusters(context, list):
    global res_content_list_clusters
    names = []
    loop = res_content_list_clusters['clusters']
    for x in loop:
        names.append(x.pop(u'name'))
    print("%s == %s" % (names, list))
    assert str(names) == str(list)

@Then('Response for list cluster by id is:"{list}"')
def response_get_cluster(context, list):
    global res_content_get_cluster
    cluster = res_content_get_cluster['cluster']
    id = cluster.pop(u'id')
    print("%s == %s" % (cluster, list))
    assert str(cluster) == str(list)

#@Then('"{first}" is "{second}"')
#def chkStatus(context, first, second):
#    global res1, res2
#    print("%s == %s" % (res1, res2))
#    assert res1 == res2
#
#@Then ('API returns "{access_token}"')
#def impl(context, access_token):
#    print("access_token = %s" % access_token)
#    assert (match("[\w|\d]+-[\w|\d]+-[\w|\d]+-[\w|\d]+-[\w|\d]+", access_token) != '')
