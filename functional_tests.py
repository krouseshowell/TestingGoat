from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def  setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #There is a site, go to it!
        self.browser.get('http://localhost:8000')

        #Does the title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')


#There is a place to enter a to do item.
#Type a item inem into the test box
#when she hits enter, the page updates and the page lists:
#The item on the to-do lists
#there is still a text book
#enters another item.
#page updates and shows both items
#the site has generated a unique url and there is explanitory test
#visits that url -todo list is there
#leaves
if __name__ == '__main__':
    unittest.main(warnings='ignore')
