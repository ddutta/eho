from behave import *
from re import match, search

@Then('Response is "{res_code}"')
def chkStatus(context, res_code):
    global status_code
    print("%s == %s" % (status_code, res_code))
    assert status_code == int(res_code.strip())

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
