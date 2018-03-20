import os
import sys
sys.path.append('/home/nagendra/code/automation/careappandroid/src/tests/')
from base_test  import *
from wheel.signatures import assertTrue
import time

@on_platforms(browsers)
class log_out(BaseTest):
    
    def test_logout(self):
        print "Present running test--test_fun_logout_check"
        el_email = self.driver.find_element_by_id('com.stacklighting.care.staging:id/intro_email')
        el_email.clear()
        el_email.set_value("sreeja@stacklighting.com")
            
        e2_pass = self.driver.find_element_by_id('com.stacklighting.care.staging:id/intro_password')
        e2_pass.clear()
        e2_pass.set_value("Abcd1234@")
         
        el_login = self.driver.find_element_by_id('com.stacklighting.care.staging:id/intro_log_in')
        el_login.click()
        time.sleep(2)
        
        e1_drawer=self.driver.find_element_by_accessibility_id("Open drawer").click()
        time.sleep(3)
        logout_click=self.driver.find_elements_by_class_name("android.support.v7.widget.ap")
        logout_click[4].click()
        
        ele=[]
        ele1=['Are you sure you want to log out?', 'Cancel', 'Log Out']
        elements=self.driver.find_elements_by_class_name("android.widget.TextView")
        for i in elements:
            ele.append(i.text)
        print[x.encode('ascii') for x in ele]
        self.assertEqual(ele,ele1) 
        
        log_out=self.driver.find_element_by_id("com.stacklighting.care.staging:id/positive")
        log_out.click()
        
        
        
  
                   
            
            
            