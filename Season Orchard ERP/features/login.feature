Feature: Login functionality

  Scenario: User logs in successfully in the Orchard dashboard
    Given I open the login page
    When I enter valid username and password
    And I click on login button
    Then I should be redirected to dashboard