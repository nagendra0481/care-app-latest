#Test_community_settings_deleteStaff

import sys
#sys.path.append('C:/Python27/code/automation/careappandroid/src/tests')
sys.path.append('/home/nagendra/code/automation/careappandroid/src/tests/')
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
        el_email_validate = self.driver.find_elements_by_id("com.stacklighting.care.staging:id/staff_email")
        for i in el_email_validate:
            view_name=self.driver.find_elements_by_id("com.stacklighting.care.staging:id/staff_email")
            e1=view_name[6]
            action = TouchAction(self.driver)
            action.press(e1).move_to(e1).release().perform()
            time.sleep(2)
            el_icon=self.driver.find_element_by_id("com.stacklighting.care.staging:id/overflow").click()
            sleep(2)
            el_del=self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.TextView")
            el_del.click()
            sleep(3)
            del_popup=[]
            del_popup=["Are you sure you want to delete Pending Invite",'cancel','delete']
            ele=self.driver.find_elements_by_class_name("android.widget.TextView")
            for i in ele:
                del_popup.append(i.text)
                ele1=[x.encode('ascii') for x in del_popup]
                self.assertEqual(del_popup,ele1) 
                log_out_cancel=self.driver.find_element_by_id("com.stacklighting.care.staging:id/negative")
                log_out_cancel.click()
                el_icon=self.driver.find_element_by_id("com.stacklighting.care.staging:id/overflow").click()
                sleep(2)
                el_del=self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.TextView")
                el_del.click()
                sleep(3)
                log_out_delete=self.driver.find_element_by_id("com.stacklighting.care.staging:id/positive")
                log_out_delete.click()
                sleep(3)
                
                
                



                    
                    
        
        