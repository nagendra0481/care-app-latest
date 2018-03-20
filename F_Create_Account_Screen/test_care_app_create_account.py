import os
import sys
sys.path.append('/home/nagendra/code/automation/careappandroid/src/tests/')

from base_test  import *
from utilityfile import *
from wheel.signatures import assertTrue
import time
import xlrd


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)





@on_platforms(browsers)

class Create_account(BaseTest):
    def test_create_acount_xlrd_account_in_use(self):
        Care_App_Create_Account(self,0);
        e1_element=self.driver.find_element_by_id("com.stacklighting.care.staging:id/snackbar_text")
        print e1_element.text
        self.assertEqual('‘nsingamsetti@stack.care’ is already in use', e1_login_status.text)

        
    def test_create_acount_xlrd_internal_error(self):
        Care_App_Create_Account(self,1);
        e1_element=self.driver.find_element_by_id("com.stacklighting.care.staging:id/snackbar_text")
        self.assertIsNotNone(e1_element)
        print e1_element.text
            
        
        
        
            
            
            
        
        

        
        
        
            
            
            

            
if __name__ == '__main__':
    unittest.main()            
            
            
            
            
            
            
            
            
            
            
            
            
