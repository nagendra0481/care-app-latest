'''
Created on 02-Dec-2017

@author: parth
'''
import os
import unittest
import sys
import new
from appium import webdriver

browsers = [
    #{
    #'appiumVersion': '1.7.1',
    #'platformName': 'Android',
    #'platformVersion': '5.0.2',
    #'deviceName': 'LGD7228668e443',
    #'name': 'careappandroid',
    #'unicodeKeyboard': 'true',
    #'resetKeyboard': 'true'},
    {
    'appiumVersion': '1.7.1',
    'platformName': 'Android',
    'platformVersion': '8.1.0',
    'deviceName': 'emulator-5554',
    'name': 'careappandroid',
    'unicodeKeyboard': 'true',
    'resetKeyboard': 'true'}
    ]
# This decorator is required to iterate over browsers
def on_platforms(platforms):

    def decorator(base_class):
        module = sys.modules[base_class.__module__].__dict__
        for i, platform in enumerate(platforms):
            d = dict(base_class.__dict__)
            d['desired_capabilities'] = platform
            name = "%s_%s" % (base_class.__name__, i + 1)
            module[name] = new.classobj(name, (base_class,), d)

    return decorator






class BaseTest(unittest.TestCase):

    # setUp runs before each test case
    def setUp(self):
        self.desired_capabilities['name'] = self.id()
        self.desired_capabilities['app'] = os.path.realpath(__file__ + "/../../../resources/app-staging-release.apk")
        self.desired_capabilities['appPackage'] = 'com.stacklighting.care.staging'
        self.desired_capabilities['appActivity'] = 'com.stacklighting.stackcare.intro.splash_screen.SplashScreenActivity'    

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_capabilities)
        self.driver.implicitly_wait(30)
        
        
    
      
    # tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()
        #test_name = "%s_%s" % (type(self).__name__, self.__name__)
        #with(open(test_name + '.testlog', 'w')) as outfile:
            #outfile.write("test-session-id=%s test-name=%s\n" % (self.driver.session_id, test_name))

















