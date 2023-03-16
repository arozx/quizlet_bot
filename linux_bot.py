from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random, argparse
from selenium.webdriver import ActionChains

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--mins", dest="minutes", help="time in minutes")
parser.add_argument("-url", "--url", dest="url", help="url")
parser.add_argument("-p", "-pass", dest="password", help="quizlet password")
parser.add_argument("-u", "-user", dest="user", help="quizlet username")
args = parser.parse_args()

password, username, mins, url = args.password, args.user, int(args.minutes), args.url
# set path
service = Service(
    executable_path="home/user/.cache/selenium/geckodriver/linux64/0.32.0/geckodriver"
)
# start session
driver = webdriver.Firefox()


def login(username, password):  # Logs in the user
    driver.get("https://quizlet.com/login")

    time.sleep(2)
    user = driver.find_element(By.NAME, "username")
    for i in username:
        user.send_keys(i)
        time.sleep(random.uniform(0.1, 0.4))
    time.sleep(3)

    passw = driver.find_element(By.NAME, "password")
    passw.send_keys(password, Keys.ENTER)
    time.sleep(2)


def quizletFlashcard(mins, url):
    driver.get(url)
    for x in range(mins * 30):
        keyType = random.randint(0, 9)
        if keyType == 0:
            # back
            ActionChains(driver).send_keys(Keys.ARROW_LEFT).perform()
            time.sleep(2)
        else:
            # forwards
            ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
            time.sleep(0.25)
            ActionChains(driver).send_keys(Keys.SPACE).perform()
            time.sleep(0.25)
        time.sleep(1.5)
    driver.close()


login(username, password)
quizletFlashcard(mins, url)
