from selenium.webdriver.common.by import By


class LoginPage:
    #locators

    def __init__(self, driver):
        self.driver=driver

    def typeUserName(self, username):
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").clear()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys(username)

    def typePassword(self, password):
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").clear()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()

    def isErrorContainerVisible(self):
       return self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[3]/h3")
