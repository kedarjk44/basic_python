Feature: Login functionality

Scenario: Successful login
    Given I am on the login page
    When I enter a valid username and password
    And I click the login button
    Then I should be logged in successfully

#to execute on command line - behave features/your_feature.feature