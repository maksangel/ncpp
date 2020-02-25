from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def login_user(driver, url, user_name, user_password):
    """
    @user_name logins to @url
    """
    driver.get(url)
    login_form = driver.find_element_by_id('link_text-2905-1210')
    login_form.click()
    login_id = driver.find_element_by_id('id_username')
    login_id.click()
    login_id.send_keys(user_name)
    login_pass = driver.find_element_by_id('id_password')
    login_pass.send_keys(user_password)
    login_btn = driver.find_element_by_class_name('btn-primary')
    login_btn.click()
    user_name_on_dashboard = (
        WebDriverWait(driver, 10)
        .until(
            EC.presence_of_element_located((By.CLASS_NAME, 'user-name-header'))
        )
    )
    if user_name_on_dashboard.text != user_name:
        raise AssertionError('logged user doesn\'t match {}'.format(user_name))
    