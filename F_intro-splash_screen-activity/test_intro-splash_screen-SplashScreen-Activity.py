'''
Created on 02-Dec-2017

@author: parth
'''
import os
import sys
sys.path.append('/home/nagendra/code/automation/careappandroid/src/tests/')
from utilityfile import *

from base_test  import *
from wheel.signatures import assertTrue
import time
import xlrd

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

@on_platforms(browsers)
class IntroSplash_screenSplashScreenActivity(BaseTest):
    
    
    
         
    def test_login_correct_credentials(self):
        print "test 1 : test_login_correct_credentials"     
        el_email = self.driver.find_element_by_id('com.stacklighting.care.staging:id/intro_email')
        el_email.clear()
        el_email.set_value("sreeja@stacklighting.com")
            
        el_pass = self.driver.find_element_by_id('com.stacklighting.care.staging:id/intro_password')
        if el_pass.is_displayed():
            el_pass.clear()
            el_pass.set_value("Abcd1234@")
         
        el_login = self.driver.find_element_by_id('com.stacklighting.care.staging:id/intro_log_in')
        el_login.click()
        #assertTrue(self.driver.wait_activity("com.stacklighting.stackcare.MainActivity", 3))             
            
    def test_login_incorrect_credentials_incorrect_email_password_xlrd(self):
        print "test 2 : login failed due to e-mail or password you entered is incorrect"
        Care_App_login_xlrd(self,0);
        e1_login_status = self.driver.find_element_by_id("com.stacklighting.care.staging:id/snackbar_text")
        self.assertIsNotNone(e1_login_status)
        print e1_login_status.text
        self.assertEqual('The e-mail or password you entered is incorrect', e1_login_status.text)
        
    def test_login_incorrect_credentials_textinput_error_xlrd(self):
        print "test 3 : login failed due to textinput_error -Use .com/.care"
        Care_App_login_xlrd(self,1);
        e1_login_status = self.driver.find_element_by_id("com.stacklighting.care.staging:id/textinput_error")
        self.assertIsNotNone(e1_login_status)
        print e1_login_status.text
        self.assertEqual('Please use standard format (eg. name@site.com)', e1_login_status.text)
        
        
            
        
        
            
            
    
            
    
        
                  
            
            
            
    
            
            
                 
            
                    
               

    #
if __name__ == '__main__':
    unittest.main()
