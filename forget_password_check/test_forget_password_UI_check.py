import os
import sys
sys.path.append('/home/nagendra/code/automation/careappandroid/src/tests/')
from base_test  import *



@on_platforms(browsers)
class forget_password_check(BaseTest):
    def test_forget_password_element_check(self):
        print "Present running test--test_forget_password_UI_check"
        uiElement = self.driver.find_element_by_id("com.stacklighting.care.staging:id/intro_forgot_password")
        l=uiElement.text
        self.assertEqual('Forgot Password?',l.encode('ascii'))
        uiElement.click()
            
        ele=[]
        ele1=[u'Forgot Password', u'No problem! Enter your email address below and we\u2019ll send you a code you can use to reset your password.']
        ele_on_forget_screen=self.driver.find_elements_by_class_name("android.widget.TextView")
            
        for i in ele_on_forget_screen:
            ele.append(i.text)
            self.assertEqual(ele1,ele)