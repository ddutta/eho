@tags @tag
Feature: Test of template section

    Scenario: User can get template
        When User see templates
        Then Response is "200"

   # Scenario: User can create template
    #    When User create template
     #   Then Response is "202"
     
    #Scenario: User can delete template
     #   When User delete template
      #  Then Response is "204"
