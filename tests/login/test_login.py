from typing_extensions import Self
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from src.pages.loginPage import LoginPage


class TestLogin():
  
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
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_login(self):
    driver = self.driver
    Login = LoginPage(driver)
    Login.typeUserName(self.vars["standard_user"])
    Login.typePassword(self.vars['password'])
    Login.clickLoginButton()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    # buscar identificador unico de pagina



  def test_login_no_credentials(self):
    driver = self.driver
    Login = LoginPage(driver)
    Login.clickLoginButton()
    errorContainer = Login.isErrorContainerVisible()
    assert errorContainer.is_displayed()
    assert errorContainer.text == "Epic sadface: Username is required"

  def test_login_no_password(self):
      driver = self.driver
      Login = LoginPage(driver)
      Login.typeUserName(self.vars["standard_user"])
      Login.clickLoginButton()
      errorContainer = Login.isErrorContainerVisible()
      assert errorContainer.is_displayed()
      assert errorContainer.text == "Epic sadface: Password is required"

  def test_login_locked(self):
      driver = self.driver
      Login = LoginPage(driver)
      Login.typeUserName(self.vars['locked_out_user'])
      Login.typePassword(self.vars['password'])
      Login.clickLoginButton()
      errorContainer = Login.isErrorContainerVisible()
      assert errorContainer.is_displayed()
      assert errorContainer.text == "Epic sadface: Sorry, this user has been locked out."    