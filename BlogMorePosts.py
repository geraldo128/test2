import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from time import sleep
from selenium.webdriver.support.ui import Select
from Page.POM import TopNav
from Page.POM import ContactForm

# should find a way to make the links work for either environment if we are really going to use this
# what would it take it take to get selenium set up on CW?
# pushed?1234


class SmokeTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/robbie/Downloads/chromedriver")

    def tearDown(self):
        self.driver.quit()

    def test_1_verify_blog_page_title(self):
        # Navigates to the blog and verifies the title includes the word Blog
        driver = self.driver
        driver.get("https://caktus:pointy@staging.caktusgroup.com")
        driver.find_element_by_class_name("posts").click()
        self.assertIn("Blog", driver.title)

    def test_2_count_blog_cards(self):
        driver = self.driver
        driver.get("https://caktus:pointy@staging.caktusgroup.com")
        # use the page object to nav to blog page instead of find element here
        navigation = TopNav(driver)
        navigation.nav_to_blog()
        # click view more posts and wait(sleep)
        driver.find_element_by_id("next").click()
        sleep(3)
        # count the number of cards
        posts_count = driver.find_elements_by_class_name("card-common--image_container")
        # veify the number of posts that display
        assert (len(posts_count) == 12)

    def test_3_contact_form(self):
        driver = self.driver
        driver.get("https://caktus:pointy@staging.caktusgroup.com")
        # Use the POM class to navigate to contact page
        navigation = TopNav(driver)
        navigation.nav_to_contact()
        # Use the POM class to enter text in the contact form
        form = ContactForm(driver)
        form.first_name("MRtest")
        form.last_name("LastName")
        form.email("example@example.com")


class ContactFormTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/robbie/Downloads/chromedriver")

    def tearDown(self):
        self.driver.quit()

    def test_4(self):
        # test that events match drop down selection
        driver = self.driver
        driver.get("https://caktus:pointy@staging.caktusgroup.com/events/")
        # select an option from the drop down on events page by the visible text
        select = Select(driver.find_element_by_id("event-year"))
        select.select_by_value("2018")
        # verify the year in the date field
        event_date = driver.find_elements_by_class_name("call-out")
        self.assertIn("2018", event_date)


if __name__ == '__main__':
    unittest.main()
