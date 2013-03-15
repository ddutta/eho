@tags @tag
Feature: Test of cluster section

    Scenario: User can get clusters
        When  User see clusters
        Then  Response is "200"

#    Scenario: User can create clusters
#        When  User create clusters
#        Then  Response is "202"
