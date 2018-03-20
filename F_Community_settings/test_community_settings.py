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
    #element check on community screen
    def test_commuinity_element_check(self):
        print "Test_Name : test_community_screen_element_check"
        Care_App_login(self,"sreeja@stacklighting.com","Abcd1234@");
        community_screen_open(self);
        community_elements=['Karnataka Gardens','Notifications','Info','Staff','Staff Groups','Bathroom Anomaly NotificationOn','No Morning Motion NotificationOn','These settings will only apply to new units.']
        community_element_list=self.driver.find_elements_by_class_name("android.widget.TextView")
        for i in community_element_list:
            for j in community_elements:
                if i==j:
                    print 'Sccuess'
    # check the community name and pincode present on the Info screen               
    def test_commuinity_info_screen_element_check(self):
        print "Test_Name : Element_check_Community_Screen_INFO"
        Care_App_login(self,"sreeja@stacklighting.com","Abcd1234@");                                       #login 
        community_screen_open(self);                                                                        #open drawer 
        Info_click=self.driver.find_elements_by_class_name("android.support.v7.app.a$c")
        Info_click[1].click()
                                                                                                            #check the text of community name and Zip code
        Community_Name_on_screen=self.driver.find_elements_by_class_name("android.widget.TextView")
        Community_Name1=Community_Name_on_screen[0]
        Community_Details=self.driver.find_elements_by_class_name("android.widget.EditText")
        Community_Name=Community_Details[0]
        Community_PIN_Code=Community_Details[1]
        self.assertEqual(Community_Name1.text,Community_Name.text)
        self.assertEqual("Karnataka Gardens",Community_Name.text)
        self.assertEqual("560096",Community_PIN_Code.text)
        
    def test_community_info_screen_Default_lightining_plan_element_check(self):
        print "Test_Name:community_info_screen_Default_lightining_plan_element_check"
        lighting_plans=['Circadian Energize: Bluish tone throughout the day to energize you','Circadian Standard: Comfortable brightness and color changing throughout the day','Circadian Off: Neutral and bright all day']
        lighting_Plans=[]
        Care_App_login(self,"sreeja@stacklighting.com","Abcd1234@");                                       #login 
        community_screen_open(self);                                                                        #open drawer 
        Info_click=self.driver.find_elements_by_class_name("android.support.v7.app.a$c")
        Info_click[1].click()
        default_lightining_plan=self.driver.find_elements_by_class_name("android.widget.RadioButton")
        for i in default_lightining_plan:
            lighting_Plans.append(i.text)
            [x.encode('ascii') for x in lighting_Plans]
        self.assertEqual(lighting_plans,lighting_Plans)
        
        
    def test_commuinity_staff_groups_element_check(self):
        print "Test_Name : Element_check_Community_Screen_staff_groups"
        Care_App_login(self,"sreeja@stacklighting.com","Abcd1234@");                                       #login 
        community_screen_open(self);                                                                        #open drawer 
        staff_groups_click=self.driver.find_elements_by_class_name("android.support.v7.app.a$c")
        staff_groups_icon_check=self.driver.find_elements_by_class_name("android.widget.TextView")
        self.assertEqual('STAFF GROUPS',staff_groups_icon_check[4].text)
        staff_groups_click[3].click()
        Group_Names=self.driver.find_elements_by_id("com.stacklighting.care.staging:id/group_name")
        for i in Group_Names:
            print i.text
            
    #To check the elements on the of STAFF GROUP        
    def test_commuinity_staff_groups_element_check(self):
        group_names=[]
        print "Test_Name : Element_check_Community_Screen_staff_groups"
        Care_App_login(self,"sreeja@stacklighting.com","Abcd1234@");                                       #login 
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
           
             
    #Functional check on Create staff               
    def test_Create_Staff(self):
        print "Test_Name : Create Staff"
        Care_App_login(self,"sreeja@stacklighting.com","Abcd1234@");
        community_screen_open(self);
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
        el_email.set_value("sreeja@stack.care")
        sleep(5)
        el_role=self.driver.find_elements_by_class_name("android.widget.ImageView")
        el_role[0].click()
        sleep(3)
        role=self.driver.find_elements_by_class_name("android.widget.TextView")
        role[1].click()
        sleep(3)
        el_icon=self.driver.find_elements_by_class_name("android.widget.ImageView")
        el_icon[1].click()
        el_group=self.driver.find_element_by_class_name("android.widget.CheckBox")
        sleep(3)
        e1_flour_click=self.driver.find_elements_by_id("android:id/text1")
        e1_flour_click[0].click()
        e1_flour_click[1].click()
        touch = TouchAction(self.driver)
        touch.press(x=292, y=1000).release().perform()
        sleep(10)
                    
        el_add=self.driver.find_element_by_id("com.stacklighting.care.staging:id/submit_button")
        el_add.click()
        
        e1_status_of_Creating_staff=self.driver.find_element_by_id("com.stacklighting.care.staging:id/snackbar_text")
        self.assertEqual(u'\u2018Add Staff\u2019 failed due to an internal error. If this issue continues, please contact support',e1_status_of_Creating_staff.text)
        
        
        
        
                       
         
        
        
        
        
    
    
