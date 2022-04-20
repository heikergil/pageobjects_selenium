from itertools import product
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from src.pages.loginPage import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.pages.productDetailsPage import ProductPage

class TestProductsDetails():
  
  def setup_method(self, method):
    service = ChromeService(executable_path=ChromeDriverManager().install())
    self.driver = webdriver.Chrome(service=service)
    self.driver.get("https://www.saucedemo.com/")
    self.driver.implicitly_wait(10)
    self.vars = {
      'standard_user': 'standard_user',
      'locked_out_user' : 'locked_out_user',
      'problem_user' : 'problem_user',
      'performance_glitch_user' : 'performance_glitch_user',
      'password' : 'secret_sauce'}
    driver = self.driver
    Login = LoginPage(driver)
    ProductDetail = ProductPage(driver)
    Login.typeUserName(self.vars["standard_user"])
    Login.typePassword(self.vars['password'])
    Login.clickLoginButton()
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_visit_product_page(self):
    driver = self.driver
    ProductDetail = ProductPage(driver)
    # elements = driver.find_elements(By.CLASS_NAME ,  "inventory_item_label")
    # for element in elements:
    #   element.click()
    ProductDetail.goToProductPage()
    assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=4"
    

  def test_add_product_to_cart(self):
    driver = self.driver
    ProductDetail = ProductPage(driver)
    ProductDetail.goToProductPage()
    ProductDetail.addBackpackToCart()
    shopping_cart_badge = ProductDetail.getShoppingCartBadge()
    assert shopping_cart_badge.is_displayed()
    
  def test_remove_product_from_cart(self):
      driver = self.driver
      ProductDetail = ProductPage(driver)
      ProductDetail.goToProductPage()
      # wait = WebDriverWait(driver, 10)
      # element = wait.until(EC.url_changes("https://www.saucedemo.com/inventory.html"))
      ProductDetail.addBackpackToCart()
      ProductDetail.removeBackpackFromCart()
      
  def test_back_to_products(self):
      driver = self.driver
      ProductDetail = ProductPage(driver)
      ProductDetail.goToProductPage()
      assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=4"
      ProductDetail.goBackToMainPage()
      assert driver.current_url == "https://www.saucedemo.com/inventory.html"
