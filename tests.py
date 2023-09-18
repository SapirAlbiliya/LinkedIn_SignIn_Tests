import time
import POMProjectFile
import ProjectFuctions
from ProjectFuctions import (
    write_to_log, load_url, send_keys_to_element, click_element, take_screenshot, quit_driver
)

def run_test(username, password, log_type, test_num):
    try:
        print(f'Starting to run the test {test_num}, GOOD LUCK!')
        time.sleep(2)
        load_url(WebsiteURl)
        write_to_log(log_type, 'Linkedin website uploaded successfully')

        if send_keys_to_element(By.ID, POMProjectFile.UserNameFieldByID, username):
            write_to_log(log_type, f'{username} has been sent to the user name field')
        else:
            write_to_log(log_type, 'Failed to send username.')

        if send_keys_to_element(By.NAME, POMProjectFile.PasswordFieldByNAME, password):
            write_to_log(log_type, f'{password} has been sent to the password field')
        else:
            write_to_log(log_type, 'Failed to send password.')

        if click_element(By.XPATH, POMProjectFile.SignInButtonByXPATH):
            write_to_log(log_type, 'Clicked on sign in button')
        else:
            write_to_log(log_type, 'Failed to click on sign in button.')

        take_screenshot(log_type)
        
        log_message = f'Welcome, sapir! was not found in the webpage, could not sign in, test {test_num} PASSED!'
        write_to_log(log_type, log_message)
        write_to_log("results", log_message)
        print(f'Finished with the test {test_num}, results are written into the logs')
    except Exception as e:
        write_to_log(log_type, str(e))
        print(f'Could not run the test {test_num}, test FAILED')

# Test 1: Valid Details
run_test(ProjectFuctions.VALID_USERNAME, ProjectFuctions.VALID_PASSWORD, "success", 1)

# Test 2: Invalid Username
run_test(ProjectFuctions.FAKE_USERNAME, ProjectFuctions.VALID_PASSWORD, "invalid_username", 2)

# Test 3: Invalid Password
run_test(ProjectFuctions.VALID_USERNAME, ProjectFuctions.FAKE_PASSWORD, "invalid_password", 3)

# Quit driver after all tests
quit_driver()
