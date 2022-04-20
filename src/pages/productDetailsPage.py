from selenium.webdriver.common.by import By

class ProductPage:
    #locators

    def __init__(self, driver):
        self.driver=driver

    def goToProductPage(self):
        self.driver.find_element(By.CSS_SELECTOR, "#item_4_title_link > .inventory_item_name").click()

    def addBackpackToCart(self):
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
  
    def removeBackpackFromCart(self):
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-backpack\"]").click()

    def goBackToMainPage(self):
       self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"back-to-products\"]").click()

    def getShoppingCartBadge(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container > a > span")