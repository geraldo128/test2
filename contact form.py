#import the selenium webdirver and other things
from selenium import webdriver

# open website with chrome
driver = webdriver.Chrome("/Users/robbie/Downloads/chromedriver")
driver.get("https://caktus:pointy@staging.caktusgroup.com")


# navigate to contact page
driver.find_element_by_class_name("contact").click()

# define the fields of the contact form
first_name = driver.find_element_by_name("firstname")
last_name = driver.find_element_by_name("lastname")
email = driver.find_element_by_name("email")

# enter data in fields
first_name.send_keys("first")
last_name.send_keys("last")

# submit the from
# driver.find_by_type("submit").click()

# driver.quit()