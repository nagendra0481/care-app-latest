import sys
import os
from selenium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
import xlrd


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

Appartments_count=[]
def Care_App_login(self,username,password):
    el_email = self.driver.find_element_by_id('com.stacklighting.care.staging:id/intro_email')
    el_email.clear()
    el_email.set_value(username)
            
    e2_pass = self.driver.find_element_by_id('com.stacklighting.care.staging:id/intro_password')
    e2_pass.clear()
    e2_pass.set_value(password)
         
    el_login = self.driver.find_element_by_id('com.stacklighting.care.staging:id/intro_log_in')
    el_login.click()
    time.sleep(2)
    
    
#Care_App_login using xlrd

def Care_App_login_xlrd(self,r):
    f_name = PATH(__file__ + "/../../../resources/email_ddt_test.xlsx")
    workbook = xlrd.open_workbook(f_name)
    sheet_names = workbook.sheet_names()
    sheet = workbook.sheet_by_name("Sheet1")
        
    el_email = self.driver.find_element_by_id('com.stacklighting.care.staging:id/intro_email')
    el_pass = self.driver.find_element_by_id('com.stacklighting.care.staging:id/intro_password')
    e6_login = self.driver.find_element_by_id('com.stacklighting.care.staging:id/intro_log_in')
        
                
        #for r in range(sheet.nrows):
    username = sheet.cell_value(r, 0)
    password = sheet.cell_value(r, 1)
    print (username)
    print (password)
    el_email.clear()
    el_pass.clear()
    el_email.set_value(username)
    el_pass.set_value(password)
    e6_login.click() 
    
    
def Care_App_Create_Account(self,r):
    f_name = PATH(__file__ + "/../../../resources/create_account.xlsx")
    workbook = xlrd.open_workbook(f_name)
    sheet = workbook.sheet_by_name("Create_Account_detials")
        
        #for r in range(sheet.nrows):
    first_name = sheet.cell_value(r, 0)
    last_name = sheet.cell_value(r, 1)
    email_input=sheet.cell_value(r,2)
    password_input=sheet.cell_value(r,3)
    Conform_password = sheet.cell_value(r,4)
    Reg_code=sheet.cell_value(r,5)       
            
    uiElement = self.driver.find_element_by_id('com.stacklighting.care.staging:id/intro_create_account')
    self.driver.implicitly_wait(1)
    uiElement.click()
    time.sleep(3)
        
    uiElement1 = self.driver.find_element_by_id('com.stacklighting.care.staging:id/edit_first_name')
    self.driver.implicitly_wait(2)
    uiElement1.clear()
    uiElement1.set_value(first_name)
        
    uiElement2 = self.driver.find_element_by_id('com.stacklighting.care.staging:id/input_last_name')
    self.driver.implicitly_wait(1)
    uiElement2.clear()
    uiElement2.set_value(last_name)

    uiElement3 = self.driver.find_element_by_id('com.stacklighting.care.staging:id/input_email')
    self.driver.implicitly_wait(2)
    uiElement3.clear()
    uiElement3.set_value(email_input)
        
    uiElement4 = self.driver.find_element_by_id('com.stacklighting.care.staging:id/input_password')
    self.driver.implicitly_wait(2)
    uiElement4.clear()
    uiElement4.set_value(password_input)
    
    uiElement5 = self.driver.find_element_by_id('com.stacklighting.care.staging:id/input_confirm_password')
    self.driver.implicitly_wait(2)
    uiElement5.set_value(Conform_password)
        
    uiElement6 = self.driver.find_element_by_id('com.stacklighting.care.staging:id/edit_invitation_code')
    self.driver.implicitly_wait(2)
    uiElement6.set_value(Reg_code)
        
        
    uiElement7 = self.driver.find_element_by_id('com.stacklighting.care.staging:id/save')
    uiElement7.click()       

def Scroll_the_status_screen(self,action,e1,e2,Sort_by_name_appartments):
    global Appartments_count
    Appartments_count=[]
    action.press(e2).move_to(e1).release().perform()
    time.sleep(2)
    count=0
    for i in Sort_by_name_appartments:
        print "Sort_by_name_appartments:",i.text
        count=count+1
    self.Appartments_count.append(count)
    print sum(self.Appartments_count)
    
    
#Community_settings_open_screen_function

def community_screen_open(self):
    e1_drawer=self.driver.find_element_by_accessibility_id("Open drawer").click()
    e1_Drawer_elements_list=self.driver.find_elements_by_class_name("android.support.v7.widget.ap")
    community_click=e1_Drawer_elements_list[1]
    community_click.click()
    
    
    
    
     

        
    