Feature: Orange HRM Login Page

  Scenario: Orange HRM Login Page with Valid Data
    Given Launch Chrome Browser
    When Open the Orange HRM home Page
    And Enter Username "Admin" Password "admin123"
    And Click On Login Button
    Then User Must Successfully Login to the Dashboard page

  Scenario Outline:Orange HRM Login Page with Invalid Data

    Given Launch Chrome Browser
    When Open the Orange HRM home Page
    And Enter Username "<username>" Password "<password>"
    And Click On Login Button
    Then User should not be login with invalid data
    Examples:
      | username | password |
      | Admin    | admin    |
      | admin    | admin123 |
