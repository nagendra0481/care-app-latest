'''
Created on 02-Dec-2017

@author: parth
'''
import sys
sys.path.append('/home/nagendra/code/automation/careappandroid/src/tests/')
from base_test  import *
from wheel.signatures import assertTrue




@on_platforms(browsers)
class IntroSplash_screenSplashScreenActivity(BaseTest):
    
    def test_ui_elements(self):
        print "Running-test_intro-splash_screen-activity-UI-elements"
        uiElement = self.driver.find_element_by_id('com.stacklighting.care.staging:id/imageView3')
        self.assertIsNotNone(uiElement)
        uiElement = self.driver.find_element_by_id('com.stacklighting.care.staging:id/intro_header_logo')
        self.assertIsNotNone(uiElement)
        uiElement = self.driver.find_element_by_id('com.stacklighting.care.staging:id/input_email')
        self.assertIsNotNone(uiElement)
        self.assertEqual('Email', uiElement.text) 
        uiElement = self.driver.find_element_by_id('com.stacklighting.care.staging:id/intro_email')
        self.assertIsNotNone(uiElement)
        uiElement = self.driver.find_element_by_id('com.stacklighting.care.staging:id/input_password')
        self.assertIsNotNone(uiElement)
        self.assertEqual('Password', uiElement.text)
        uiElement = self.driver.find_element_by_id('com.stacklighting.care.staging:id/intro_password')
        self.assertIsNotNone(uiElement)
        uiElement = self.driver.find_element_by_id('com.stacklighting.care.staging:id/intro_log_in')
        self.assertIsNotNone(uiElement)
        self.assertEqual('Log In', uiElement.text)
        uiElement = self.driver.find_element_by_id('com.stacklighting.care.staging:id/intro_forgot_password')
        self.assertIsNotNone(uiElement)
        self.assertEqual('Forgot Password?', uiElement.text)
        uiElement = self.driver.find_element_by_id('com.stacklighting.care.staging:id/intro_create_account')
        self.assertIsNotNone(uiElement)
        self.assertEqual('Create Account', uiElement.text)
     
     
     
     
if __name__ == '__main__':
    unittest.main()
     