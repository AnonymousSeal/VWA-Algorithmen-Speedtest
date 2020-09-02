from selenium import webdriver
from time import sleep
import geckodriver_autoinstaller


geckodriver_autoinstaller.install()  # Check if the current version of geckodriver exists
                                     # and if it doesn't exist, download it automatically,
                                     # then add geckodriver to path

#options = FirefoxOptions()
#options.add_argument("--headless")
#driver = webdriver.Firefox(options=options)

def get_number(bit_len=128):
    binary_len = driver.find_element_by_id('prime')
    submit = driver.find_element_by_xpath('/html/body/div/div/div/div[4]/table/tbody/tr/td/form/p/input[2]')
    binary_len.clear()
    binary_len.send_keys(bit_len)
    submit.click()
    return driver.find_element_by_id('random3').get_property('value')

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('https://asecuritysite.com/encryption/random3')
    print(get_number())
    sleep(5)
    driver.quit()
