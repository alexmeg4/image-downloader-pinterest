from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import time
from selenium.webdriver.common.by import By

# login data for Pinterest
username = "your_email"
password = "your_password"

# create an instance of the browser driver
driver = webdriver.Firefox()

# go to website
driver.get("https://www.pinterest.com/")

# find login button and click on it
time.sleep(5)
login_btn = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[2]/button')
# login_btn = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/div[2]/button/div/div")
login_btn.click()

# Find username and password fields and fill them in
username_field = driver.find_element(By.NAME,"id")
password_field = driver.find_element(By.NAME,"password")
username_field.send_keys(username)
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)

# Wait for login process to finish
time.sleep(10)

# links list
links = ['https://pin.it/3U74GFqav']

error_list = []

# loop through links list
for link in links:
    # visit the link from the list
    driver.get(link)

    # wait for page to be fully loaded
    time.sleep(10)
    img_src = ''
    
    # name of the image file that will be created
    file_name = "image-" + link.split("https://pin.it/")[1] + ".jpg"

    # download the file locating the image using xpath
    # tries three times because images can be in different xpaths, so each try has a different xpath
    success = False
    tryNumber = 1
    paths = [
        "/html/body/div[1]/div[1]/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/div/img",
        "/html/body/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div/div[1]/div/div/img",
        "/html/body/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/div/img",
        "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/div/img",
        "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/div/img"
    ]
    tryNumber = 1
    for path in paths:
        if not success:
            try:
                img_element = driver.find_element(By.XPATH, path)
                img_src = img_element.get_attribute("src")
                urllib.request.urlretrieve(img_src, file_name)
                success = True
                print('SUCCESS -> ', tryNumber)
            except  Exception as e:
                print('FAIL -> ', tryNumber)
                tryNumber += 1
    if not success:
        error_list.append(link)
        
    # try:
    #     print('Downloading - Try count 1 ' + link)
    #     img_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/div/img")
    #     img_src = img_element.get_attribute("src")
    #     urllib.request.urlretrieve(img_src, file_name)
    # except Exception as e:
    #     print('Downloading - Try count 2 ' + link)
    #     try:
    #         img_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div/div[1]/div/div/img")
    #         img_src = img_element.get_attribute("src")
    #         urllib.request.urlretrieve(img_src, file_name)
    #     except Exception as e:
    #         print('Downloading - Try count 3 ' + link)
    #         try:
    #             img_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/div/img")
    #             img_src = img_element.get_attribute("src")
    #             urllib.request.urlretrieve(img_src, file_name)
    #         except Exception as e:
    #             print('ERROR - cant download ' + link + ' trace ' + str(e))
    #             error_list.append(link)
    #         else:
    #             print('Successfully downloaded: ' + link)
    #     else:
    #         print('Successfully downloaded: ' + link)
    # else:
    #     print('Successfully downloaded: ' + link)


print('List of failed links')
print(error_list)

# closes the browser
driver.quit()
