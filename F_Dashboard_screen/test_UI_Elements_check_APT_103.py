import sys
sys.path.append('/home/nagendra/code/automation/careappandroid/src/tests/')
from base_test  import *
from unittest.suite import BaseTestSuite
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By 
from wheel.signatures import *
import time

@on_platforms(browsers)
class dashboard_screen_functional(BaseTest):
    def test_coentiarrect_credls(self):
        print "Present running test - test_UI_Elements_check_APT_103"
             
        el_email = self.driver.find_element_by_id('com.stacklighting.care.staging:id/intro_email')
        el_email.clear()
        el_email.set_value("sreeja@stacklighting.com")
            
        e2_pass = self.driver.find_element_by_id('com.stacklighting.care.staging:id/intro_password')
        e2_pass.clear()
        e2_pass.set_value("Abcd1234@")
         
        el_login = self.driver.find_element_by_id('com.stacklighting.care.staging:id/intro_log_in')
        el_login.click()
        time.sleep(3)
        
        e1_drawer=self.driver.find_element_by_accessibility_id("Open drawer").click()
        time.sleep(3)
        
        e1_community_bar1=self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.support.v7.widget.ap[1]")
        e1_community_bar1.click()
        time.sleep(2)
        
        
        
        
        e1_status=self.driver.find_element_by_xpath("//android.widget.TextView[@index=2]")
        e1_status.click()
        time.sleep(2)
        
        #e1_text0=self.driver.find_element_by_class_name("//android.support.v7.app.a$c")
        #print e1_text0[1].get_attribute("text")
        
        
        
            
        
        
        
            
        text2=[]
        e1_text4=self.driver.find_elements_by_id("com.stacklighting.care.staging:id/unit_users")
        self.assertIsNotNone(e1_text4)
        for i in e1_text4:
            print i.text
        #self.assertEqual('Apt 103', e1_text4.text)
        
        
        text1=[]
        e1_text0=self.driver.find_elements(By.XPATH,"//android.widget.TextView")
        self.assertIsNotNone(e1_text0)
        for i in e1_text0:
            print i.text
            
        
        
        
        
        
        
        