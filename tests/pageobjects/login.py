# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from tests.pageobjects.common import CommonPageObject
from toolium.pageelements import *

class LoginPageObject(CommonPageObject):
    def init_page_elements(self):
        return self;

    def setElements(self):
        self.tenant = InputText(By.NAME, 'tenant');
        self.name = InputText(By.NAME, 'name');
        self.password = InputText(By.NAME, 'password');
        self.loginBtn = Button(By.ID, 'loginFormSubmit');
        return self;

    def waitToDrawSection(self):
        self.utils.wait_until_element_visible(PageElement(By.NAME, "loginForm").locator)
        return self

    def getUserName(self):
        return Text(By.ID, "user-header")

    def resetForm(self):
        self.tenant.clear();
        self.name.clear();
        self.password.clear();
        return self;
