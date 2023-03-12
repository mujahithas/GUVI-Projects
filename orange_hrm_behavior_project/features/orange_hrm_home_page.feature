Feature: Orange HRM Admin page
  Background:
    Given Launch Chrome Browser
    When Open the Orange HRM home Page
    And Enter Username "Admin" Password "admin123"
    And Click On Login Button
  Scenario: Validate admin Search Box
    And Enter the value on admin search box
    Then The user Should be able to Search the Home page and the Individual Menu
