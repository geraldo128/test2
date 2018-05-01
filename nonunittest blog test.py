from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from time import sleep

driver = webdriver.Chrome("/Users/robbie/Downloads/chromedriver")
driver.get("https://caktus:pointy@staging.caktusgroup.com")

# navigate to blog page
driver.find_element_by_class_name("posts").click()

# click view more posts this will prob require some kind of wait
driver.find_element_by_id("next").click()
sleep(2)

# wait for URL to change
# wait =  WebDriverWait(driver, 15)
# element = wait.until(EC.url_changes)

# count the number of cards
posts_count = driver.find_elements_by_class_name("card-common--image_container")

# print the number of cards
# print ("Found " + str(len(posts_count)))

# veify the number of posts that display
try:
    assert(len(posts_count) == 12)
    print("Found " + str(len(posts_count)) + " Pass")
except Exception as e:
    print("Found " + str(len(posts_count)) + " Fail")
    screen_name = datetime.now()
    driver.get_screenshot_as_file("/Users/robbie/Desktop/%s.png" % screen_name)

driver.quit()
