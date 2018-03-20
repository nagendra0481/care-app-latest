import sys
sys.path.append('/home/nagendra/code/automation/careappandroid/src/tests/')
from base_test import *
from wheel.signatures import assertTrue
from time import sleep




@on_platforms(browsers)
class Drawer_layout_element_check(BaseTest):
    def test_check_elements_on_Drawer_layout_screen(self):
        el_email = self.driver.find_element_by_id('com.stacklighting.care.staging:id/intro_email')
        el_email.clear()
        el_email.set_value("sreeja@stacklighting.com")
            
        e2_pass = self.driver.find_element_by_id('com.stacklighting.care.staging:id/intro_password')
        e2_pass.set_value("Abcd12345@")
        
        el_login = self.driver.find_element_by_id('com.stacklighting.care.staging:id/intro_log_in')
        el_login.click() 
        sleep(2)    
        e1_drawer=self.driver.find_element_by_accessibility_id("Open drawer").click()
        sleep(2)
        Drawer_Screen_elements=self.driver.find_element_by_id("com.stacklighting.care.staging:id/navigation_user_name")
        print Drawer_Screen_elements.text
        self.assertEqual('Sreeja Paniker',Drawer_Screen_elements.text)
        ele1=['Dashboard', 'Community Settings', 'My Account', 'Support', 'Log Out']
        ele=[]
        Drawer_Screen_elements=self.driver.find_elements_by_id("com.stacklighting.care.staging:id/design_menu_item_text")
        for i in Drawer_Screen_elements:
            ele.append(i.text)
        print [x.encode('ascii') for x in ele]
        self.assertEqual(ele1,ele)