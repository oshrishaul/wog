# 1. test_scores_service(app_url) – Will test our web service.
# Will get the application URL as an input,
# open a browser to that URL
# select the score element in our web page
# check that it is a number between 0 to 1000
# and return a boolean value if it’s true or not.

from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:/Sel-drivers/chromedriver.exe")

app_url="http://127.0.0.1:8777"

def test_scores_service(app_url):
    driver.get(app_url)
    driver.implicitly_wait(2)
    score=int(driver.find_element_by_id("score").text)
    if score in range(1,1000):
        return True
    else:
        return False

# 2. main_function() –
# Will call our tests function.
# The main function will return -1 as an OS exit code if the tests failed, and 0 if it passed.

def main_function():
    test_app = test_scores_service(app_url)
    if test_app is True:
        print('0')
    else:
        print('1')
