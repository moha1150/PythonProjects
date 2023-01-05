from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Open a Chrome browser and navigate to the website
driver = webdriver.Chrome()
driver.get('http://www.example.com/drag-and-drop-page')

# Locate the draggable element
draggable_element = driver.find_element_by_id('draggable')

# Locate the drop zone
drop_zone = driver.find_element_by_id('drop-zone')

# Use ActionChains to perform the drag-and-drop action
actions = ActionChains(driver)
actions.drag_and_drop(draggable_element, drop_zone).perform()
