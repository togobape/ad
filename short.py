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

# url = "https://ouo.io/idvRmi"
# url = "http://theinfogiver.elementfx.com/tutorial/news-1.html"

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

for url in url_list:

    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    wait = WebDriverWait(browser, 20)
    print("New Browser Opened")

    browser.get(url)
    time.sleep(1)
    parentGUID = browser.current_window_handle

    try:
        # First One
        # time.sleep(10)
        # wait.until(EC.element_to_be_clickable((By.ID, "btn-main")))
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-main']")))
        time.sleep(3)
        body = browser.find_element_by_id('btn-main')
        ActionChains(browser).move_to_element(body).click().perform()
        print("First Button clicked")

        # Check for another window

        # allGUID = browser.window_handles;
        # print(allGUID)
        # browser.switch_to.window(parentGUID);

        # Second One
        time.sleep(5)
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-main']")))
        body = browser.find_element_by_id('btn-main')
        ActionChains(browser).move_to_element(body).click().perform()
        print("Second Button clicked")

        time.sleep(3)
        if (len(browser.window_handles) > 1):
            try:
                browser.switch_to.window(browser.window_handles[1])
                print("Tab switched")
                browser.close()
                print("Tab Closed")
            except Exception as err2:
                print(f"[+] ERROR2: {err2}")

        browser.switch_to.window(parentGUID)

        print(Fore.GREEN+Style.BRIGHT+" >> Success"+Style.RESET_ALL)
    except Exception as err:
        print(Fore.RED+Style.BRIGHT+" >> Failed"+Style.RESET_ALL)
        print(f"[+] ERROR1: {err}")
        pass

    time.sleep(3)

    while (len(browser.window_handles) > 1):
        try:
            browser.switch_to.window(browser.window_handles[1])
            print("Tab switched")
            browser.close()
            print("Tab Closed")
        except:
            pass

        browser.switch_to.window(parentGUID)

    browser.delete_all_cookies()
    print("All Cookie Deleted")

    time.sleep(2)
    
browser.quit()
print("Browser Closed")
