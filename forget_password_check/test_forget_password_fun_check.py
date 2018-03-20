import os
import sys
sys.path.append('/home/nagendra/code/automation/careappandroid/src/tests/')
from base_test  import *



@on_platforms(browsers)
class forget_password_fun_check(BaseTest):
    
    
    def test_forget_password_fun_check(self):
        print "Present running test--test_forget_password_fun_check"
        uiElement = self.driver.find_element_by_id("com.stacklighting.care.staging:id/intro_forgot_password")
        uiElement.click()
        uiElement = self.driver.find_element_by_id("com.stacklighting.care.staging:id/forgot_password_email")
        self.driver.implicitly_wait(2)
        uiElement.set_value("nsingamsetti@stacklighting.com")
        uiElement= self.driver.find_element_by_id("com.stacklighting.care.staging:id/forgot_password_reset") 
        uiElement.click()