from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import random
from random import randint


def ran_time():
    run = random.uniform(10, 40)
    print("waiting ", run, "sec")
    time.sleep(run)  # sleep between milliseconds and second


def ran_time_small():
    run = random.uniform(1, 6)
    print("waiting ", run, "sec")
    time.sleep(run)  # sleep between milliseconds and second


# def delayed_input(text, query): # input query one by one
#     for letter in text:
#         query.send_keys(letter)
#         ran_time()
#     query.submit()

# ran_time()
# text = "Manchester United"
# query = d.find_element_by_name("q")
# delayed_input(text, query)

url = ["https://techforhack.com/84-woocommerce-extensions-updates/",
       "https://techforhack.com/56-woocommerce-extensions-updates/",
       "https://techforhack.com/newspaper-v10-3-7-wordpress-news-theme/",
       "https://techforhack.com/elementor_pro_3-0-4_nulled/",
       "https://techforhack.com/adobe-cc-2020-universal-crack-for-adobe-cc-2020-full-version/",
       "https://techforhack.com/wireshark-termux/",
       "https://techforhack.com/windows-10-kali-linux-subsystem-full-tutorial/",
       "https://techforhack.com/tool-x/",
       "https://techforhack.com/routersploit/",
       "https://techforhack.com/newspaper-v10-3-7-wordpress-news-theme/",
       "https://techforhack.com/networkingfundamentals/",
       "https://techforhack.com/networkdevices/",
       "https://techforhack.com/portable_hacking_device/",
       "https://techforhack.com/tbomber/",
       "https://techforhack.com/metasploit-termux/",
       "https://techforhack.com/lazy_script/",
       "https://techforhack.com/nethunter-on-android/",
       "https://techforhack.com/install-hidden-eye-advanced-phishing-tool-full-guide/",
       "https://techforhack.com/instagram-tools-hack-insta-from-termux/",
       "https://techforhack.com/black_hydra/",
       "https://techforhack.com/nmap/",
       "https://techforhack.com/hackpro/",
       "https://techforhack.com/fix-any-android-game-lag-in-few-minutes/",
       "https://techforhack.com/elementor_pro_3-0-4_nulled/",
       "https://techforhack.com/ddos-termux/",
       "https://techforhack.com/databasetechnology/",
       "https://techforhack.com/database-models-all-you-need-to-know/",
       "https://techforhack.com/metasploit-payload-termux/"]


def web():
    profile = webdriver.FirefoxProfile()
    options = Options()
    options.headless = True
    options.add_argument('--incognito')
    options.add_argument('Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--ref')

    profile.set_preference('excludeSwitches', 'enable-automation')
    profile.set_preference("dom.webserver.enabled", False)
    profile.set_preference('useAutomationExtension', False)

    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.socks", "127.0.0.1")
    profile.set_preference("network.proxy.socks_port", 9050)
    profile.set_preference("network.proxy.socks_version", 5)

    profile.update_preferences()
    options.add_argument('--disable-blink-features')

    d = webdriver.Firefox(firefox_profile=profile, options=options, executable_path='geckodriver')

    # d.get("https://www.google.com/search?client=firefox-b-e&q=whats+my+ip")
    # time.sleep(5)
    # d.refresh()
    # time.sleep(5)
    # d.refresh()

    i = randint(100, 300)
    visitor = int(0)

    d.get('https://techforhack.com/')
    print(i)
    print("-----------------------------------")

    while i > 0:
        d.get(random.choice(url))
        print("Page Open")
        print(d.title)
        d.maximize_window()
        ran_time_small()
        d.execute_script("window.scrollTo(10, document.body.scrollHeight);")
        print("Scroll Down")
        ran_time()
        i -= 1
        visitor += 1
        print(visitor, "View Completed")
        print("-----------------------------------")

    d.quit()
    print("you got", visitor, "views")


if __name__ == '__main__':
    web()
