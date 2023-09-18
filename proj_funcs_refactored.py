import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import POMProjectFile

# Constants
WEBSITE_URL = 'https://www.linkedin.com/'
VALID_USERNAME = 'sapalb01@gmail.com'
VALID_PASSWORD = 'SapAlb07'
FAKE_USERNAME = 'fakeemail@gmail.com'
FAKE_PASSWORD = '1234567'
LOG_FILES = {
    "success": 'Login_successful_Log.txt',
    "invalid_username": 'Fake_user_Name_Log.txt',
    "invalid_password": 'Fake_Password_Log.txt',
    "results": 'Results_Log.txt'
}

# Initialize webdriver
driver = webdriver.Chrome()


def write_to_log(log_type, message):
    """Writes a message to the specified log."""
    try:
        with open(LOG_FILES[log_type], 'a') as f:
            timestamp = str(datetime.datetime.now())
            f.write(f"{timestamp} {message}\n")
    except:
        print(f"Could not write to the {LOG_FILES[log_type]}")


def find_element(by_type, value, timeout=30):
    """Find and return an element using the provided method and value."""
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by_type, value)))


def send_keys_to_element(by_type, value, keys, clear_first=True):
    """Send keys to an element identified by its locator."""
    try:
        elem = find_element(by_type, value)
        if clear_first:
            elem.clear()
        elem.send_keys(keys)
        return True
    except Exception as e:
        return False


def load_url(url):
    """Load a URL in the browser."""
    try:
        driver.get(url)
        driver.maximize_window()
        print('Website loaded successfully.')
    except:
        for log_type in LOG_FILES:
            write_to_log(log_type, 'Website could not load - FAIL')
        print('Website could not load.')


def click_element(by_type, value):
    """Click on an element identified by its locator."""
    try:
        elem = find_element(by_type, value)
        elem.click()
        return True
    except Exception as e:
        return False


def take_screenshot(log_type):
    """Take a screenshot and save it based on the log type."""
    filenames = {
        "success": "valid_details_test_screenshot.png",
        "invalid_username": "invalid_username_test_screenshot.png",
        "invalid_password": "invalid_password_test_screenshot.png"
    }
    try:
        driver.get_screenshot_as_file(filenames[log_type])
        write_to_log(log_type, 'Screenshot was taken successfully')
        print('Screenshot was taken.')
    except:
        write_to_log(log_type, 'Could not take screenshot - FAIL')
        print('Error occurred and was not able to take screenshot - FAIL')



def quit_driver():
    """Quit the Selenium driver."""
    try:
        driver.quit()
    except:
        print('Could not quit from Driver')


# Example usage:
# load_url(WEBSITE_URL)
# if send_keys_to_element(By.ID, POMProjectFile.UserNameFieldByID, VALID_USERNAME):
#     print("Username sent successfully.")
# else:
#     write_to_log("success", "Failed to send username.")
