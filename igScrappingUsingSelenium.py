import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create a requests session
session = requests.Session()
#make sure the chrome driver is compatible with the version of your chrome driver
driver = webdriver.Chrome("")
# Login to Instagram
url = "https://www.instagram.com/accounts/login/"
data = {
    "username": "yourUsername",
    "password": "YourPassword",
}
response = requests.post(url, data=data)
# print(response)

driver.get(url)
html = driver.page_source
# print(html)

# Check if the login was successful
if response.status_code == 200:
    # click on the profile button
    profile_button = "xnz67gz x14yjl9h xudhj91 x18nykt9 xww2gxu x9f619 x1lliihq x2lah0s x6ikm8r x10wlt62 x1n2onr6 x1ykvv32 xougopr x159fomc xnp5s1o x194ut8o x1vzenxt xd7ygy7 xt298gk x1xrz1ek x1s928wv x1n449xj x2q1x1w x1j6awrg x162n7g1 x1m1drc7"
    profile_elements = driver.find_element(By.CLASS_NAME, profile_button)
    profile_elements.click()
    time(20)
    if profile_elements.click() == True:

        # click on the followers button
        followers_button = "x9f619 xxk0z11 xii2z7h x11xpdln x19c4wfv xvy4d1p"
        followers_elements = driver.find_element(By.CLASS_NAME, followers_button)
        followers_elements.click()
        time(20)
        if followers_elements.click() == True:

            # parse the html to usernames class
            followers_class_name = "x9f619 xjbqb8w x1rg5ohu x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1"
            elements = driver.find_elements(By.CLASS_NAME, class_name)
            if elements == True:

                # loop through all of the text in that class
                # add the usernames to a list
                attributes = []
                for element in elements:
                    for attribute in element.attrib:
                        attributes.append((attribute, element.get_attribute(attribute)))
                print(attributes)
            else:
                print("Failed to access followers")
        else:
            print("Unable to click followers")
    else:
        print("Failed to click profile")
else:
    print("Unable to login")
