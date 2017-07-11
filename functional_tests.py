from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    def  setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        #There is a site, go to it!
        self.browser.get('http://localhost:8000')

        #Does the title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #There is a place to enter a to do item.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        #Type a "Buy peacock feathers" into the test box
        inputbox.send_keys('Buy peacock feathers')


        #when she hits enter, the page updates and the page lists:
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy peacock feathers')
#The item on the to-do lists
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        #there is still a text box
        #enters another item.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        #page updates and shows both items
        self.check_for_row_in_list_table('1: Buy peackock feathers')
        self.check_for_row_in_list_table('2: Use peackock feathers to make a fly')
        
        #page updates and shows both items
        self.fail('Finish the test!')
#the site has generated a unique url and there is explanitory test
#visits that url -todo list is there
#leaves
if __name__ == '__main__':
    unittest.main(warnings='ignore')
