from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


@given("I am on the login page")
def step_given_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")


@when("I enter a valid username and password")
def step_when_enter_credentials(context):
    context.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    context.driver.find_element(By.ID, "password").send_keys("secret_sauce")


@when("I click the login button")
def step_when_click_login(context):
    context.driver.find_element(By.ID, "login-button").click()


@then("I should be logged in successfully")
def step_then_logged_in(context):
    assert "logged in" in context.driver.page_source