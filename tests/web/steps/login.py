from behave import given, when, then
from tests.pageobjects.login import LoginPageObject
from nose.tools import assert_in, assert_equal, assert_true, assert_false

@given('goto homepage')
def step_impl(context):
    context.current_page = LoginPageObject()
    context.current_page.open().waitToDrawSection().setElements()

