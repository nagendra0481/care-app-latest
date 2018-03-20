import sys
sys.path.append('/home/nagendra/code/automation/careappandroid/src/tests/')
from base_test import *
from utilityfile import *
from unittest.suite import BaseTestSuite
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
from dateutil import parser
from dateutil import relativedelta as relativedelta


@on_platforms(browsers)
class dashboard_screen_functional(BaseTest):
    def test_Dashboard_History_popup_settings(self):
        print "Present running test--test_dashboard_status_screen"
             
        Care_App_login(self,username,password);
        time.sleep(2)
        
        e1_drawer=self.driver.find_element_by_accessibility_id("Open drawer").click()
        
        e1_community_bar1=self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.support.v7.widget.ap[1]")
        e1_community_bar1.click()
        time.sleep(2)
        
        
        dashboard_status_list =self.driver.find_elements_by_class_name("android.support.v7.app.a$c")
        dashboard_status_list[0].click()  # Click on the status 
        
        l2=self.driver.find_element_by_id("com.stacklighting.care.staging:id/overflow")
        l2.click()
        
        
        
        Custom_popup=self.driver.find_elements_by_id("com.stacklighting.care.staging:id/custom_popup_item")
            
        Custom_popup[0].click()      #sort_by_name
        
        Sort_by_name_appartments=self.driver.find_elements_by_id("com.stacklighting.care.staging:id/unit_users")
        for i in Sort_by_name_appartments:
            print "Sort_by_name_appartments:",i.text
        l2.click()
        
        Custom_popup[1].click()   #Sort by notification
        
        #e2_text0=self.driver.find_elements_by_id("com.stacklighting.care.staging:id/event_name")
        Sort_by_notification_appartments=self.driver.find_elements_by_id("com.stacklighting.care.staging:id/unit_users")
        for i in Sort_by_notification_appartments:
            print "Sort_by_notifications_appartments:",i.text
            
        if Sort_by_name_appartments!=Sort_by_notification_appartments:
            print "success" 
            
        
            
           
           


            
            
           
            
        
        
            
            
         
            
            
            
    
        

        
        
        
        
        
        
        
        