import sys
sys.path.append('/home/nagendra/code/automation/automation/careappandroid/src/tests')
from base_test import *
from unittest.suite import BaseTestSuite
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By 
from wheel.signatures import *
import time
from dateutil import parser
from dateutil import relativedelta as relativedelta

@on_platforms(browsers)
class dash_board_history_screen(BaseTest):
    def test_Dashboard_History_popup_settings(self):
        print "Present running test--test_dashboard_history_screen"
             
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
        
        e1_community_bar1=self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.support.v7.widget.ap[1]")
        e1_community_bar1.click()
        time.sleep(2)
        
        
        Status_History_list =self.driver.find_elements_by_class_name("android.support.v7.app.a$c")
        Status_History_list[1].click()  # Click on the History 
        
        l2=self.driver.find_element_by_id("com.stacklighting.care.staging:id/overflow")
        l2.click()
        
        
        
        Custom_popup=self.driver.find_elements_by_id("com.stacklighting.care.staging:id/custom_popup_item")
            
        Custom_popup[0].click()      #Change by notification
        
        Notification_appartments=self.driver.find_elements_by_id("com.stacklighting.care.staging:id/event_name")
        for i in Notification_appartments:
            print "Sort_by_notifications_appartments:",i.text
        l2.click()
        
        Custom_popup[1].click()   #Sort by name
        
        #e2_text0=self.driver.find_elements_by_id("com.stacklighting.care.staging:id/event_name")
        Sort_by_name_appartments=self.driver.find_elements_by_id("com.stacklighting.care.staging:id/event_name")
        for i in Sort_by_name_appartments:
            print "Sort_by_name_appartments:",i.text
            
        #if Notification_appartments!=Sort_by_name_appartments:
           # print "success" 
            
        l2.click()
        Custom_popup[2].click()
        Sort_by_date_appartments=self.driver.find_elements_by_id("com.stacklighting.care.staging:id/event_name")
        for L in Sort_by_date_appartments:
            
            print "Sort by date Appartments:",L.text
            
        if Notification_appartments!=Sort_by_name_appartments!=Sort_by_date_appartments:
            print "Pass"
        #time_info=[] 
        #Sort_by_date_appartments=self.driver.find_elements_by_id("com.stacklighting.care.staging:id/event_time")
        #for q in Sort_by_date_appartments:
         #   print "Sort by Appartments using time:",q.text
          #  dt = parser.parse(q.text)
           # time_info.append(dt)
        #print time_info
        #a=time_info[0]
        #b=time_info[-1]
        
        #c=a-b
        #if c>-1:
         #   print "success"
        
         
            
            
           
           


            
            
           
            
        
        
            
            
         
            
            
            
    
        

        
        
        
        
        
        
        
        