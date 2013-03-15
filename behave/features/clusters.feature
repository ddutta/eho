@tags @tag
Feature: Test of cluster section

    Scenario: User can get clusters
        When  User see clusters
        Then  Response is "200"
        And Response list of list clusters:"[u'hadoop']"

    Scenario: User can create cluster
        When User add cluster name:"QA_cluster_2" and image_id:"d9342ba8-4c51-441c-8d5b-f9e14a901299"
        And  User create cluster
        Then  Response is "202"

    Scenario: User can get clusters
        When  User see clusters
        Then  Response is "200"
        And Response list of list clusters:"[u'hadoop', u'QA_cluster_2']"

    Scenario: User can get cluster by ID
        When User see cluster with id:"0"
        Then  Response is "200"
        And Response for list cluster by id is:"{u'status': u'Active', u'service_urls': {u'namenode': u'http://172.18.79.193:50070', u'jobtracker': u'http://172.18.79.193:50030'}, u'name': u'hadoop', u'tenant_id': u'tenant-01', u'base_image_id': u'2f6acc36-02dc-4a21-9dce-e7c1f5322eed', u'node_templates': {u'jt_nn.small': 1, u'tt_dn.small': 5}, u'nodes': [{u'node_template': {u'id': u'1aceae318a2d452fa8e0f933a744988b', u'name': u'jt_nn.small'}, u'vm_id': u'c0447b26-3c8f-459c-b224-5748b5fd823d'}, {u'node_template': {u'id': u'd1baaec8429741b0bd5fffac5c0b3c6c', u'name': u'tt_dn.small'}, u'vm_id': u'92e039d2-0be5-4448-9bce-4fcaaf732904'}, {u'node_template': {u'id': u'd1baaec8429741b0bd5fffac5c0b3c6c', u'name': u'tt_dn.small'}, u'vm_id': u'7668ee5e-4576-4dae-9f94-9091ce1f9e9d'}, {u'node_template': {u'id': u'd1baaec8429741b0bd5fffac5c0b3c6c', u'name': u'tt_dn.small'}, u'vm_id': u'0dd97eb7-db19-44c7-83cc-3c36fed59b80'}, {u'node_template': {u'id': u'd1baaec8429741b0bd5fffac5c0b3c6c', u'name': u'tt_dn.small'}, u'vm_id': u'99e9dae4-6006-459c-8b31-68910ce7c2f3'}, {u'node_template': {u'id': u'd1baaec8429741b0bd5fffac5c0b3c6c', u'name': u'tt_dn.small'}, u'vm_id': u'7a23a97e-bd59-4586-8f98-143d7721ce51'}]}"

    Scenario: User can get cluster by ID
        When User see cluster with id:"1"
        Then  Response is "200"
        And Response for list cluster by id is:"{u'status': u'Starting', u'service_urls': {}, u'name': u'QA_cluster_2', u'tenant_id': u'tenant-01', u'base_image_id': u'd9342ba8-4c51-441c-8d5b-f9e14a901299', u'node_templates': {u'jt_nn.small': 1, u'tt_dn.small': 1}, u'nodes': []}"

    Scenario: User can delete cluster by ID
        When User delete cluster with id:"1"
        Then  Response is "204"

    Scenario: User can get clusters
        When  User see clusters
        Then  Response is "200"
        And Response list of list clusters:"[u'hadoop']"
