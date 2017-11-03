import time
from selenium import webdriver

url = "https://makershare.com/projects/makevember"
url2 = "https://makershare.com/projects/web-scraper-python-makevember-001"
url3 = "https://makershare.com/projects/urban-data-posts"

#choose browser (Firefox/Chrome) and import url (change url link above)
driver = webdriver.Firefox()
driver.get(url2)

#delay - since Maker Share has multi-stage JS loading
print("start")
time.sleep(5)

#grab project and author data
project_image = driver.find_element_by_class_name("img-responsive").get_attribute('src')
project_title = driver.find_element_by_class_name("card-title").text
project_description = driver.find_element_by_xpath("//p[@class='inner-html']").text
project_tags = driver.find_element_by_xpath("//*[@class='project-tag']/span").text
author_image = driver.find_element_by_class_name("card-owner-media").get_attribute('src')
author_link = driver.find_element_by_class_name("card-owner-link").get_attribute('href')
author_name = driver.find_element_by_class_name("card-owner-link").text
author_quote = driver.find_element_by_class_name("maker-description").text
#comment out next line when looking at url
author_location = driver.find_element_by_class_name("maker-city").text

#close browser
driver.quit()

#a heads up to let me know the code is finished running
print("project url:", url2)
print("project image:", project_image)
print("project title:", project_title)
print("project description:", project_description)
print("project tags:", project_tags)
print("author image:", author_image)
print("author link:", author_link)
print("author name:", author_name)
print("author quote:", author_quote)
#comment out next line when looking at url
print("author address:", author_location)
print("done")
