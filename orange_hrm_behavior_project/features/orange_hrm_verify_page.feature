Feature: valid orange HRM page
  Scenario:logo present on orange HRM page
    Given launch browser for chrome
    When open the browser launch the orange HRM website
    Then verify the logo has present
    And close the browser