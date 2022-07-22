import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains

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

options = Options()
options.headless=True
browser = webdriver.Firefox(options=options, executable_path = r'bin/geckodriver')

# Google Chrome Version 83.0.4103.116 (Official Build) (64-bit)

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--no-sandbox")
# chrome_options.headless=True
# chrome_options.add_argument('--disable-gpu')
# chrome_options.binary_location = '/usr/bin/google-chrome'
# browser = webdriver.Chrome(options=chrome_options)
# browser = webdriver.Chrome(options=chrome_options, executable_path = r'bin/chromedriver')

for url in url_list:

    print("===============================================")
    print(f"Viewing Video {url}")

    browser.get(url)

    time.sleep(5)

    parentGUID = browser.current_window_handle

    video_frame = browser.find_element_by_tag_name("iframe")
    browser.switch_to.frame(video_frame)

    play_button = browser.find_element_by_xpath("//div[@aria-label='Play']")

    ActionChains(browser).move_to_element(play_button).click().perform()
    print("Clicked Play button..!")
    print(f"Number of running tab is {len(browser.window_handles)}")
    time.sleep(2)

    try:
        while True:

            if (len(browser.window_handles) > 1):
                try:
                    browser.switch_to.window(browser.window_handles[1])
                    print("Tab switched")
                    browser.close()
                    print("Tab Closed")
                except:
                    pass

            time.sleep(2)
            browser.switch_to.window(parentGUID)
            print("Switched to main tab..!")
            video_frame = browser.find_element_by_tag_name("iframe")
            browser.switch_to.frame(video_frame)
            print("Switched to iframe")
            print("Trying to click..!")
            ActionChains(browser).move_to_element(play_button).click().perform()
            print("Clicked Play button..!")
            time.sleep(2)
            print(f"Number of running tab is {len(browser.window_handles)}")
    except Exception as err:
        print(f"[+] ERROR: {err}")
        print("Video started playing")
        browser.switch_to.window(parentGUID)

    time.sleep(240) 

browser.quit()
