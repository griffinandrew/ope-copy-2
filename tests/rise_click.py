from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import platform
import sys

if len(sys.argv) <= 1:
    print("Invalid number of arguments")
    exit(1)

token = sys.argv[1]
url = "http://127.0.0.1:8888/lab?token=" + token
chrome_options = Options()

if platform.system() == 'Windows' or platform.system() == 'Darwin':
    chrome_options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()), options=chrome_options)
elif platform.system() == 'Linux':
    chrome_options.add_argument('--headless') # Inorder for Action to run, it needs to be headless
    driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), options=chrome_options)
else:
    print("Unknown OS")
    exit(1)

driver.get(url)

driver.implicitly_wait(10)

new_nb_button = driver.find_element(By.XPATH, '//div[@data-category="Notebook"]')
new_nb_button.click()


rise_button = driver.find_element(By.XPATH, '//button[@data-command="RISE:preview"]')
rise_button.click()

print("Rise Extension is working!")


#experimenting with adding to Ke's test

#testing slideshow
#slide_button = driver.find_element(By.XPATH, '//button[@data-command="RISE:slideshow"]')
#slide_button.click()

#print("slideshow")

#help
#help_button = driver.find_element(By.XPATH, '//button[@data-command="RISE:riseHelp"]')
#help_button.click()

print("help")
#experimenting with adding to Ke's test

first_slide_button = driver.find_element(By.XPATH, '//li[@data-command="RISE:firstSlide"]')
first_slide_button.click()

print("first slide")


last_slide_button = driver.find_element(By.XPATH, '//button[@data-command="RISE:lastSlide"]')
last_slide_button.click()

print("last slide")


chlk_clear_button = driver.find_element(By.XPATH, '//button[@data-command="RISE:chalkboard-clear"]')
chlk_clear_button.click()


chlk_next_button = driver.find_element(By.XPATH, '//button[@data-command="RISE:chalkboard-clear"]')
chlk_next_button.click()

slide_button = driver.find_element(By.XPATH, '//button[@data-command="RISE:chalkboard-clear"]')
slide_button.click()




# Test 3: Verify entering and exiting the RISE slideshow mode
#enter_slideshow_button = driver.find_element(By.XPATH, '//button[@data-command="RISE:start_slideshow"]')
#exit_slideshow_button = driver.find_element(By.XPATH, '//button[@data-command="RISE:stop_slideshow"]')

# Click enter slideshow button and verify the slideshow is active
#enter_slideshow_button.click()
#assert driver.find_element(By.XPATH, '//div[@class="rise-slides-container"]').is_displayed()

# Click exit slideshow button and verify the slideshow is no longer active
#exit_slideshow_button.click()
#assert not driver.find_element(By.XPATH, '//div[@class="rise-slides-container"]')

# Test 4: Verify customizing RISE settings
#settings_button = driver.find_element(By.XPATH, '//button[@data-command="RISE:settings"]')
#settings_button.click()

# Perform further assertions to verify the expected behavior of the settings menu

print("RISE extension functionality tests passed!")

#driver.quit()
