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
login_btn = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/div[2]/button/div/div")
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
links = [
"https://pin.it/1E4OurA",
"https://pin.it/3pjGEaw",
"https://pin.it/5k17T3s",
"https://pin.it/14tthSO",
"https://pin.it/5jNR8t0",
"https://pin.it/1h2UnPH",
"https://pin.it/6VLfX10",
"https://pin.it/29OV8VO",
"https://pin.it/6a2gr1c",
"https://pin.it/6K4xbCC",
"https://pin.it/5QaHNgu",
"https://pin.it/5okPMT6",
"https://pin.it/2B7sRHT",
"https://pin.it/4LM53j4",
"https://pin.it/3e3begr",
"https://pin.it/4sjjDIq",
"https://pin.it/6VmpPb9",
"https://pin.it/5SZxwhr",
"https://pin.it/2OCrr9m",
"https://pin.it/4l33PFD",
"https://pin.it/71wRLHL",
"https://pin.it/4Z2Z4uP",
"https://pin.it/6kjuIkI",
"https://pin.it/57U1lxX",
"https://pin.it/3REkC00",
"https://pin.it/49sLXQ7",
"https://pin.it/1qB7eOd",
"https://pin.it/2tkVWlu",
"https://pin.it/2sDvqMM",
"https://pin.it/BP37bxc",
"https://pin.it/1IXCotj",
"https://pin.it/4iq4aBR",
"https://pin.it/2VrUBmf",
"https://pin.it/24fDSP9",
"https://pin.it/34yzK09",
"https://pin.it/2GDfwjO",
"https://pin.it/47iZVhm",
"https://pin.it/3Qydz81",
"https://pin.it/3IbKfID",
"https://pin.it/4aA17wf",
"https://pin.it/2Ctsg6u",
"https://pin.it/6JCRWko",
"https://pin.it/4VmrNFz",
"https://pin.it/3RQAJkt",
"https://pin.it/1hvwVcE",
"https://pin.it/2HVx65p",
"https://pin.it/7z8MlRU",
"https://pin.it/5DIG1j7",
"https://pin.it/3LqGjtu",
"https://pin.it/5wbQ3nP",
"https://pin.it/2LguTOd",
"https://pin.it/4C0h0y7",
"https://pin.it/3BqPXso",
"https://pin.it/2WfUvzr",
"https://pin.it/2gOHO3K",
"https://pin.it/26k66Sx",
"https://pin.it/4g7TzGs",
"https://pin.it/7hrCNLq",
"https://pin.it/6msfnlc",
"https://pin.it/yE5im96",
"https://pin.it/1Vcqxcq",
"https://pin.it/2pAPCc9",
"https://pin.it/1ozS5Z5",
"https://pin.it/2ECgQjt",
"https://pin.it/6a2gr1c",
"https://pin.it/6K4xbCC",
"https://pin.it/5QaHNgu",
"https://pin.it/2OCrr9m",
"https://pin.it/4l33PFD",
"https://pin.it/4aA17wf",
"https://pin.it/4VmrNFz",
"https://pin.it/3RQAJkt",
"https://pin.it/6msfnlc",
]

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
    try:
        print('Downloading - Try count 1 ' + link)
        img_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/div/img")
        img_src = img_element.get_attribute("src")
        urllib.request.urlretrieve(img_src, file_name)
    except Exception as e:
        print('Downloading - Try count 2 ' + link)
        try:
            img_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div/div[1]/div/div/img")
            img_src = img_element.get_attribute("src")
            urllib.request.urlretrieve(img_src, file_name)
        except Exception as e:
            print('Downloading - Try count 3 ' + link)
            try:
                img_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/div/img")
                img_src = img_element.get_attribute("src")
                urllib.request.urlretrieve(img_src, file_name)
            except Exception as e:
                print('ERROR - cant download ' + link + ' trace ' + str(e))
                error_list.append(link)
            else:
                print('Successfully downloaded: ' + link)
        else:
            print('Successfully downloaded: ' + link)
    else:
        print('Successfully downloaded: ' + link)

print('List of failed links')
print(error_list)

# closes the browser
driver.quit()
