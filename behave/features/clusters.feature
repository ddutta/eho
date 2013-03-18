@tags @tag
Feature: Test of cluster section

    Scenario: User can get clusters
        When  User see clusters
        Then  Response is "200"
        And Response list of list clusters:"[]"

    Scenario: User can create cluster
        When name:"QAcluster" and im_id="d9342ba8-4c51-441c-8d5b-f9e14a901299" and n_n="jt_nn.medium" and count="1" and d_n="tt_dn.small" and count="1"
        And  User create cluster
        Then  Response is "202"

    Scenario: User can get clusters
        When  User see clusters
        Then  Response is "200"
        And Response list of list clusters:"[u'QAcluster']"

    Scenario: User can get cluster by ID
        When User see cluster with id:"0"
        Then  Response is "200"
        And Response for list cluster by id is:"{u'status': u'Starting', u'service_urls': {}, u'name': u'QAcluster', u'base_image_id': u'd9342ba8-4c51-441c-8d5b-f9e14a901299', u'node_templates': {u'jt_nn.medium': 1, u'tt_dn.small': 1}, u'nodes': []}"

    Scenario: User can delete cluster by ID
        When User delete cluster with id:"0"
        Then  Response is "204"

    Scenario: User can get clusters
        When  User see clusters
        Then  Response is "200"
        And Response list of list clusters:"[]"
