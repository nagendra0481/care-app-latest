# -*- coding: utf-8 -*-
import sys
#sys.path.append('C:/Python27/code/automation/careappandroid/src/tests')
sys.path.append('/home/nagendra/code/automation/careappandroid/src/tests/')
from base_test import *
from utilityfile import *
from time import sleep
from appium.webdriver.common.touch_action import TouchAction


@on_platforms(browsers)
class Create_Staff(BaseTest):
    def test_Create_Staff(self):
        Care_App_login(self,"sreeja@stacklighting.com","Abcd1234@")
        #def Create_staff(self):
        e1_drawer=self.driver.find_element_by_accessibility_id("Open drawer").click()
        sleep(2)
        e2_community_bar=self.driver.find_element_by_xpath("//android.widget.FrameLayout[@index=1]")
        e2_community_bar.click()
        sleep(2)
        s=self.driver.find_elements_by_class_name("android.support.v7.app.a$c")
        print s[2].text
        s[2].click()
        sleep(3)
        icon=self.driver.find_element_by_id("com.stacklighting.care.staging:id/overflow").click()
        addstaff=self.driver.find_element_by_id("com.stacklighting.care.staging:id/custom_popup_item")
        addstaff.click()
        sleep(3)                   
        el_email = self.driver.find_element_by_id('com.stacklighting.care.staging:id/edit_email')
        el_email.clear()
        el_email.set_value("nag.nagi1@stack.care")
        sleep(5)
        el_role=self.driver.find_elements_by_class_name("android.widget.ImageView")
        el_role[0].click()
        sleep(3)
        role=self.driver.find_elements_by_class_name("android.widget.TextView")
        role[1].click()
        sleep(3)
        el_icon=self.driver.find_elements_by_class_name("android.widget.ImageView")
        el_icon[1].click()
        sleep(3)
        group1=self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.FrameLayout[1]/android.widget.CheckBox")
        group1.click()
        sleep(1)
        group2=self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.FrameLayout[2]/android.widget.CheckBox")
        group2.click()
        sleep(2) 
        touch=TouchAction(self.driver)
        touch.press(x=500,y=600).release().perform()
        sleep(2)    
        el_add=self.driver.find_element_by_id("com.stacklighting.care.staging:id/submit_button")
        el_add.click()
        sleep(1)                           
        UI_error=self.driver.find_element_by_id("com.stacklighting.care.staging:id/snackbar_text")
        a = "‘Add Staff’ failed due to an internal error. If this issue continues, please contact support"
        self.assertTrue(a,UI_error.text) 
        print("Email already exists",a)         
        sleep(3)
        
        
        
        test_community_settings_Add_new
        import sys
sys.path.append('C:/Python27/code/automation/careappandroid/src/tests')
from base_test import *
from utilityfile import *
from time import sleep
from appium.webdriver.common.touch_action import TouchAction


@on_platforms(browsers)
class Create_Staff(BaseTest):
    email_list=[]
    def test_Create_Staff(self):
        Care_App_login(self,"sreeja@stacklighting.com","Abcd1234@")
        e1_drawer=self.driver.find_element_by_accessibility_id("Open drawer").click()
        sleep(2)
        e2_community_bar=self.driver.find_element_by_xpath("//android.widget.FrameLayout[@index=1]")
        e2_community_bar.click()
        sleep(2)
        s=self.driver.find_elements_by_class_name("android.support.v7.app.a$c")
        print s[2].text
        s[2].click()
        sleep(3)
        icon=self.driver.find_element_by_id("com.stacklighting.care.staging:id/overflow").click()
        addstaff=self.driver.find_element_by_id("com.stacklighting.care.staging:id/custom_popup_item")
        addstaff.click()
        sleep(3)                   
        el_email = self.driver.find_element_by_id('com.stacklighting.care.staging:id/edit_email')
        text_email=[]
        el_email.clear()
        
        email = el_email.set_value("sree123456789@stack.care")
        text_email.append(email.text)
        sleep(5)
        el_role=self.driver.find_elements_by_class_name("android.widget.ImageView")
        el_role[0].click()
        sleep(3)
        role=self.driver.find_elements_by_class_name("android.widget.TextView")
        role[1].click()
        sleep(3)
        el_icon=self.driver.find_elements_by_class_name("android.widget.ImageView")
        el_icon[1].click()
        sleep(3)
        group1=self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.FrameLayout[1]/android.widget.CheckBox")
        group1.click()
        sleep(1)
        group2=self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.FrameLayout[2]/android.widget.CheckBox")
        group2.click()
        sleep(2) 
        touch=TouchAction(self.driver)
        touch.press(x=500,y=600).release().perform()
        sleep(2)    
        el_add=self.driver.find_element_by_id("com.stacklighting.care.staging:id/submit_button")
        el_add.click()
        sleep(5) 
        el_email_validate = self.driver.find_elements_by_id("com.stacklighting.care.staging:id/staff_email")
        global email_list
        email_list=[] 
                #for i in el_email_validate:
            #email_list.append(i.text)
        #view_name=self.driver.find_elements_by_id("com.stacklighting.care.staging:id/staff_email")
           
        #e1=view_name[3]
        #e2=view_name[5]    
        #action = TouchAction(self.driver)    
        #action.press(e2).move_to(e1).release().perform()
        #time.sleep(2)
        for i in el_email_validate:
            email_list.append(i.text)
        print [x.encode('ascii') for x in email_list]    
        for x in email_list:
            for j in text_email:
                if x==j:
                    print ("Email id exists", x)
                else:
                    print ("Email id does not exist")

                    
                    