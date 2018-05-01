from selenium import webdriver

class TopNav(object):

    def __init__(self, driver):
        self.driver = driver

    def nav_to_blog(self):
        self.driver.find_element_by_class_name("posts").click()

    def nav_to_services(self):
        self.driver.find_element_by_class_name("service-page").click()

    def nav_to_ourwork(self):
        self.driver.find_element_by_class_name("our-work").click()

    def nav_to_aboutus(self):
        self.driver.find_element_by_class_name("about-us").click()

    def nav_to_contact(self):
        self.driver.find_element_by_class_name("contact").click()

class ContactForm(object):

    def __init__(self, driver):
        self.driver = driver

    def first_name(self, first_name):
        self.driver.find_element_by_name("firstname").send_keys(first_name)

    def last_name(self, last_name):
        self.driver.find_element_by_name("lastname").send_keys(last_name)

    def email(self, email):
        self.driver.find_element_by_name("email").send_keys(email)
