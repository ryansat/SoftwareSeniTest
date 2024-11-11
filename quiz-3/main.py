from playwright.sync_api import Page, expect

# --- Page Object Model ---

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_field = page.locator("#user-name")
        self.password_field = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def goto(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.product_items = page.locator(".inventory_item")

    def add_to_cart(self, item_index):
        self.product_items.nth(item_index).locator("button").click()

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.remove_button = page.locator("button:has-text('Remove')")
        self.checkout_button = page.locator("#checkout")

    def goto(self):
        self.page.goto("https://www.saucedemo.com/cart.html")

    def remove_item(self, item_index):
        self.cart_items.nth(item_index).locator("button:has-text('Remove')").click()

    def checkout(self):
        self.checkout_button.click()

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_field = page.locator("#first-name")
        self.last_name_field = page.locator("#last-name")
        self.postal_code_field = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")

    def fill_form(self, first_name, last_name, postal_code):
        self.first_name_field.fill(first_name)
        self.last_name_field.fill(last_name)
        self.postal_code_field.fill(postal_code)

    def continue_checkout(self):
        self.continue_button.click()

    def finish_checkout(self):
        self.finish_button.click()


# --- Test Cases ---

def test_login(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_select_items(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    products_page = ProductsPage(page)
    
    # Select 2 items
    products_page.add_to_cart(0) 
    products_page.add_to_cart(1) 
    
    # Select 3 items
    products_page.add_to_cart(2) 

    # Select 4 items
    products_page.add_to_cart(3) 

def test_full_flow(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(page)
    import random
    for _ in range(random.randint(1, 4)):  # Add 1 to 4 random items
        products_page.add_to_cart(random.randint(0, 5))

    cart_page = CartPage(page)
    cart_page.goto()
    cart_page.remove_item(0)  # Remove the first item
    cart_page.checkout()

    checkout_page = CheckoutPage(page)
    checkout_page.fill_form("John", "Doe", "12345")
    checkout_page.continue_checkout()
    checkout_page.finish_checkout()

    # Add assertion to check for successful checkout (e.g., order confirmation message)
    expect(page.locator("h2:has-text('Thank you for your order!')")).to_be_visible()