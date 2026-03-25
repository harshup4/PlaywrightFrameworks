Feature: Order Transaction
  Tests related to Order Transactions
  Scenario Outline: Verify correct order id displayed at Order details page
    Given place order with <username> and <password>
    And user is on landing page
    When user login to portal with <username> and <password>
    And navigate to Orders page
    Then Select order and verify order id

    Examples:
    |username|password|
    |harshup1773920138@yopmail.com|Pass_1773920138%|
    |harshup1773920725@yopmail.com|Pass_1773920725%|