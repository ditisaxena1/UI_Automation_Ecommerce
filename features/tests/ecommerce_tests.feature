# Created by ditis at 25-10-2024
Feature: [UI] - Automation Test Store

  Scenario: E2E Flow - Verify that user is able to add a product to the cart and remove it
    Given User is on Automation Test Store Website
    When User search for product - Men and optional category - None
    And User clicks on Go button
    And User selects the product 'ck One Gift Set'
    Then Verify that user is navigated to ck One Gift Set page
    When User add 3 product
    And User click on add to cart button
    Then Verify that user is navigated to Shopping Cart page
    When User selects the category - Makeup and optional sub category - Cheeks
    And User selects the product 'Skinsheen Bronzer Stick'
    Then Verify that user is navigated to Skinsheen Bronzer Stick page
    And User click on add to cart button
    Then Verify that user is navigated to Shopping Cart page
    When User removes the product - Skinsheen Bronzer Stick
    Then Product - Skinsheen Bronzer Stick is removed from the cart
    And User removes the product - ck One Gift Set
    Then Verify that cart is empty is displayed


  Scenario: Verify that user is able to select the product from category drop down
    Given User search for product - Men and optional category - None
    And User clicks on Go button
    And User clicks on Category drop down
    And User selects the category Skincare
    And User clicks on Search
