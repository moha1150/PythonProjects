from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

# Open the Google homepage in a Chrome browser
url = 'https://www.google.com'
driver = webdriver.Chrome()
driver.get(url)

# Try to find the search field on the Google homepage
try:
    search_field = driver.find_element_by_name("q")
except NoSuchElementException:
    # If the element is not found, print an error message and exit
    print("Unable to find search field on Google homepage")
    driver.quit()
    exit()

# Enter the search query "What is the quote of the day"
search_field.send_keys("What is the quote of the day")

# Submit the search form
search_field.submit()
