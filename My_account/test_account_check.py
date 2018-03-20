import sys
sys.path.append('/home/nagendra/code/automation/careappandroid/src/tests/')
from base_test import *
from wheel.signatures import assertTrue
from time import sleep
from utilityfile import *
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

@on_platforms(browsers)
class community_check(BaseTest):
    #element check on community screen staff groups
    def test_commuinity_staff_groups_element_check(self):
        group_names=[]
        print "Test_Name : Element_check_Community_Screen_staff_groups"
        Care_App_login(self,"sreeja@stacklighting.com","Abcd12345@");                                       #login 
        community_screen_open(self);                                                                        #open drawer 
        staff_groups_click=self.driver.find_elements_by_class_name("android.support.v7.app.a$c")
        #staff_groups_icon_check=self.driver.find_elements_by_class_name("android.widget.TextView")
        #self.assertEqual('STAFF GROUPS',staff_groups_icon_check[4].encode('ascii'))
        staff_groups_click[3].click()
        Group_Names=self.driver.find_elements_by_id("com.stacklighting.care.staging:id/group_name")
        for i in Group_Names:
            group_names.append(i.text)
        group_names1=[x.encode('ascii') for x in group_names]
        print group_names1   
        print len(group_names1)
            
            
            
            
            
            
        
        
            
        
        
        
