# SauceDemo Web Automation Test

This repository contains web automation tests for SauceDemo using Playwright.

## How to run the tests

1.  **Install dependencies:**

    ```bash
    pip install playwright
    playwright install
    ```

2.  **Run the tests:**

    ```bash
    pytest test_saucedemo.py
    ```

## Test Scenarios

- **Login:** Tests the login functionality with valid credentials.
- **Select Items:** Tests adding different numbers of items to the cart.
- **Full Flow:** Tests the complete flow from login to checkout, including adding random items, removing an item, and filling the checkout form.

## Page Object Model

The tests use a Page Object Model (POM) to structure the code and make it more maintainable. The POM includes classes for:

- `LoginPage`
- `ProductsPage`
- `CartPage`
- `CheckoutPage`

## Assertions

- The `test_login` case asserts that the URL is correct after login.
- The `test_full_flow` case asserts that the "Thank you for your order!" message is displayed after checkout.
