# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from tests.pageobjects.common import CommonPageObject
from toolium.pageelements import *

class LoginPageObject(CommonPageObject):
    def init_page_elements(self):
        return self;

    def setElements(self):
        self.User = InputText(By.ID, "ember456");
        self.password = InputText(By.ID, "ember468");

    def waitToDrawSection(self):
        self.utils.wait_until_element_present(PageElement(By.ID, "ember456"));
        self.utils.wait_until_element_present(PageElement(By.ID, "ember468"));
        return self

    def getUserName(self):
        return Text(By.ID, "user-header")

    def resetForm(self):
        self.User.clear();
        self.password.clear();
        return self;
