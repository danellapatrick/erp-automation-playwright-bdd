Feature: Farmer Management

  Scenario: Admin creates a new farmer successfully
    Given I am logged in as an Supervisor and on the operational dashboard
    When I navigate to the farmers page
    And I click on the 'Add Farmer' button
    Then the Add New Farmer popup should appear