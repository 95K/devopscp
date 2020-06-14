# import all required frameworks 
import unittest 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 

# inherit TestCase Class and create a new test class 
class DOCPVerifyAbout(unittest.TestCase): 

	# initialization of webdriver 
	def setUp(self): 
		self.driver = webdriver.Chrome() 

	# Test case method. It should always start with test_ 
	def test_about_page(self): 
		
		# get driver 
		driver = self.driver 
		# get website using selenium 
		driver.get("http://172.17.0.2") 

		# find the 'About Us' button by id
		button = driver.find_element_by_id("About Us")

		# click the 'About Us' button
		button.click()

		# the text we are searching for
		text="This is <b>about</b> page. Lorem Ipsum Dipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

		# check if the text is in the page
		self.assertTrue (text in driver.page_source) 

	# cleanup method called after every test performed 
	def tearDown(self): 
		self.driver.close() 

# execute the script 
if __name__ == "__main__": 
	unittest.main()

