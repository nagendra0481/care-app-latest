from base_test  import *
sys.path.append('/home/nagendra/code/automation/careappandroid/src/tests/')
from unittest.suite import BaseTestSuite
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By 
from wheel.signatures import *
import time
from dateutil import parser
from dateutil import relativedelta as relativedelta
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from utilityfile import *

@on_platforms(browsers)
class dashboard_screen_functional(BaseTest):
    Appartments_count=[]
    def test_dashbard_sort_by_name(self):
        print "test_dashboard_sort_by_name"
        
        Care_App_login(self,"sreeja@stacklighting.com","Abcd1234@");
        e1_drawer=self.driver.find_element_by_accessibility_id("Open drawer").click()
        e1_community_bar1=self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.support.v7.widget.ap[1]")
        e1_community_bar1.click()
        
        dashboard_status_list =self.driver.find_elements_by_class_name("android.support.v7.app.a$c")
        dashboard_status_list[0].click()  # Click on the status
        
        e1_over_flow=self.driver.find_element_by_id("com.stacklighting.care.staging:id/overflow")
        e1_over_flow.click()
        
        e1_sort_by_last_motion=self.driver.find_elements_by_id("com.stacklighting.care.staging:id/custom_popup_item")
        e1_sort_by_last_motion[0].click()  #click on the sort_by_Name 
        
        Sort_by_name_appartments=self.driver.find_elements_by_id("com.stacklighting.care.staging:id/unit_users")
        
        time.sleep(2)
        action = TouchAction(self.driver)
        e1=Sort_by_name_appartments[3]
        e2=Sort_by_name_appartments[5]
        
  
        Scroll_the_status_screen(self,action,e1, e2,Sort_by_name_appartments);
        
        Scroll_the_status_screen(self,action,e1, e2,Sort_by_name_appartments);
    
        
        Scroll_the_status_screen(self,action,e1,e2,Sort_by_name_appartments);
        
    
        Scroll_the_status_screen(self,action,e1,e2,Sort_by_name_appartments);
        
        
        
       
        
        
    def test_dashboard_sort_by_last_motion(self):
        print "test_dashboard_sort_by_last_motion"
        Care_App_login(self);
        e1_drawer=self.driver.find_element_by_accessibility_id("Open drawer").click()
        e1_community_bar1=self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.support.v7.widget.ap[1]")
        e1_community_bar1.click()
        
        dashboard_status_list =self.driver.find_elements_by_class_name("android.support.v7.app.a$c")
        dashboard_status_list[0].click()  # Click on the status 
        
        e1_over_flow=self.driver.find_element_by_id("com.stacklighting.care.staging:id/overflow")
        e1_over_flow.click()
        
        e1_sort_by_last_motion=self.driver.find_elements_by_id("com.stacklighting.care.staging:id/custom_popup_item")
        e1_sort_by_last_motion[1].click()  #click on the sort_by_last_motion
        Sort_by_name_appartments=self.driver.find_elements_by_id("com.stacklighting.care.staging:id/unit_users")
        
        time.sleep(2)
        action = TouchAction(self.driver)
        
        
        e1=Sort_by_name_appartments[3]
        e2=Sort_by_name_appartments[5]
           
        
        Scroll_the_status_screen(self,action,e1, e2,Sort_by_name_appartments);
        
        Scroll_the_status_screen(self,action,e1, e2,Sort_by_name_appartments);
        
        Scroll_the_status_screen(self,action,e1,e2,Sort_by_name_appartments);
        
        Scroll_the_status_screen(self,action,e1,e2,Sort_by_name_appartments);
        
    
        

       
                   


        
        
           


            
            
           
            
        
        
            
            
         
            
            
            
    
        

        
        
        
        
        
        
        
        