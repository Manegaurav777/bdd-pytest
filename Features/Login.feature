Feature: Test Webpage Functionality
  Scenario: Verify Homepage
    Given Launch the browser
    Then Verify homepage title
    And Close the browser

  Scenario: Verify Login Functionality
    Given Launch the browser
    When click on TestLogin
    Then Enter login Credentials
    Then Click on Submit
    Then Verify Page Title
    And Close the browser
