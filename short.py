import time, sys
from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
# For Webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# url = "http://festyy.com/edQHIp"

url_list_file = sys.argv[1]
url_list = []
try:
    with open(url_list_file, 'r') as lf:
        url_list_n = lf.readlines()
        for n in url_list_n:
            url_list.append(n.strip())
except:
    print("Choose a correct URL list..!!")
    sys.exit(0)


chrome_options = webdriver.ChromeOptions()
chrome_options.headless=True

# browser = webdriver.Chrome(options=chrome_options)
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
wait = WebDriverWait(browser, 20)
print("New Browser Opened")

for url in url_list:

    try:
        browser.get(url)
        time.sleep(1)
        parentGUID = browser.current_window_handle


        wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='skip-btn show']")))
        time.sleep(3)
        skip_button = browser.find_element_by_xpath("//span[@class='skip-btn show']")
        # skip_button.click()
        while browser.current_url == url:
            ActionChains(browser).move_to_element(skip_button).click().perform()
            print("Button Clicked..!")
            time.sleep(2)
            browser.switch_to.window(parentGUID)
            print(browser.current_url)
            time.sleep(2)

        print(Fore.GREEN+Style.BRIGHT+" >> Success"+Style.RESET_ALL)

    except Exception as err:
        print(Fore.RED+Style.BRIGHT+" >> Failed"+Style.RESET_ALL)
        print(f"[+] ERROR: {err}")

    browser.delete_all_cookies()
    print("All Cookie Deleted")

browser.quit()
print("Browser Closed")

