import os
import sys
sys.path.append('/home/nagendra/code/automation/careappandroid/src/tests/')
from base_test  import *
from wheel.signatures import assertTrue
import time



@on_platforms(browsers)
class Create_account_UI_check(BaseTest):
    
    def test_click_create_account(self):
        print "test_create_account_screen_UI_check"
        uiElement = self.driver.find_element_by_id('com.stacklighting.care.staging:id/intro_create_account')
        self.driver.implicitly_wait(5)
        self.assertIsNotNone(uiElement)
        self.assertEqual('Create Account', uiElement.text)
        uiElement.click()
        time.sleep(2)
        
    def test_ui_elements(self):
        
        uiElement = self.driver.find_element_by_id('com.stacklighting.care.staging:id/intro_create_account')
        self.driver.implicitly_wait(2)
        uiElement.click()
        
        uiElement = self.driver.find_elements_by_class_name('android.widget.TextView')
        ele=[]
        for x in uiElement:
            ele.append(x.text)
        print ele
            
        uiElement = self.driver.find_element_by_id('com.stacklighting.care.staging:id/edit_first_name')    
        self.assertEqual('First Name', uiElement.text) 
        uiElement = self.driver.find_element_by_id('com.stacklighting.care.staging:id/edit_last_name')
        self.assertIsNotNone(uiElement)
        self.assertEqual('Last Name',uiElement.text)
        uiElement = self.driver.find_element_by_id('com.stacklighting.care.staging:id/edit_email')
        self.assertIsNotNone(uiElement)
        self.assertEqual('Email', uiElement.text)
        uiElement = self.driver.find_element_by_id('com.stacklighting.care.staging:id/edit_password')
        self.assertIsNotNone(uiElement)
        self.assertEqual('Password', uiElement.text)
        uiElement = self.driver.find_element_by_id('com.stacklighting.care.staging:id/edit_password_confirm')
        self.assertIsNotNone(uiElement)
        self.assertEqual('Confirm Password ', uiElement.text)
        uiElement = self.driver.find_element_by_id('com.stacklighting.care.staging:id/edit_invitation_code')
        self.assertIsNotNone(uiElement)
        self.assertEqual('Invitation Code(optional)', uiElement.text)
        uiElement = self.driver.find_element_by_id('com.stacklighting.care.staging:id/save')
        self.assertIsNotNone(uiElement)
        self.assertEqual('CREATE', uiElement.text)
    
if __name__ == '__main__':
    unittest.main() 
    
    
    
    
    

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    