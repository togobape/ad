import time
from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


# url = "https://ouo.io/idvRmi"
url = "http://theinfogiver.elementfx.com/tutorial/news-1.html"


chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=%s' % proxy)
# chrome_options.headless=True

browser = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(browser, 20)

browser.get(url)
time.sleep(1)
parentGUID = browser.current_window_handle


while True:

    ad_button = browser.find_element_by_name("first_button")
    ad_button.click()
    print("Ad Button Clicked")

    browser.switch_to.window(browser.window_handles[1])
    print("Switched to AD Window.!")

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
                browser.switch_to.window(browser.window_handles[2])
                print("Tab switched")
                browser.close()
                print("Tab Closed")
            except Exception as err2:
                print(f"[+] ERROR2: {err2}")

        browser.switch_to.window(browser.window_handles[1])

        print(Fore.GREEN+Style.BRIGHT+" >> Success"+Style.RESET_ALL)
    except Exception as err:
        print(Fore.RED+Style.BRIGHT+" >> Failed"+Style.RESET_ALL)
        print(f"[+] ERROR1: {err}")
        pass

    time.sleep(5)

    while (len(browser.window_handles) > 1):
        try:
            browser.switch_to.window(browser.window_handles[1])
            print("Tab switched")
            browser.close()
            print("Tab Closed")
        except:
            pass

    browser.switch_to.window(parentGUID)

    next_button = browser.find_element_by_name("second_button")
    next_button.click()
    print("Next Button Clicked")
    time.sleep(2)

    browser.delete_all_cookies()
    print("All Cookie Deleted")

browser.quit()

