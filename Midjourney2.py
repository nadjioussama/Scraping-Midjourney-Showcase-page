import random
import string
import requests
from selenium import webdriver 
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By

imgLinks = []

# Replace /top/ with /recent/ to get newest pictures
searchUrl = "https://midjourney.com/showcase/top/"

# Add your webdriver path here
webdriver_service = service.Service(r"Path\to\chrome or opera webDriver.exe...")
webdriver_service.start()

options = webdriver.ChromeOptions()
options.add_experimental_option('w3c', True)

# Add your chrome-based applicaion path here
options.binary_location = r"Path\to\Chrome.exe\Opera.exe.."


driver = webdriver.Remote(webdriver_service.service_url, options=options)

# Timeout for the page to completly load, if your page doesnt load quick, increase the value
driver.implicitly_wait(5)
driver.get(searchUrl)

links = driver.find_elements(By.CSS_SELECTOR, "link.hidden")


# The images shown arent full quality, this part gets the links for the original format files
for elem in links:
    link = elem.get_attribute('href')
    link = link.replace("0_0_32_N.webp", "0_0.png")
    link = link.replace("0_1_32_N.webp", "0_0.png")
    link = link.replace("0_2_32_N.webp", "0_0.png")
    link = link.replace("0_3_32_N.webp", "0_0.png")
    link = link.replace("grid_0_32_N.webp", "0_0.png")
    imgLinks.append(link)

driver.quit()


for elem in imgLinks:
    img_link = elem
    img_data = requests.get(img_link).content
    # Random name genrator
    img_name = ''.join(random.choices(string.ascii_letters, k=5)) + ".png"
    print(img_name)
    with open("./Midjourney/" + img_name, 'wb') as handler:
        handler.write(img_data)

