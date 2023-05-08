from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random, argparse, time
from selenium.webdriver import ActionChains

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--mins", dest="minutes", help="time in minutes")
parser.add_argument("-url", "--url", dest="url", help="url")
parser.add_argument("-p", "-pass", dest="password", help="quizlet password")
parser.add_argument("-u", "-user", dest="user", help="quizlet username")
args = parser.parse_args()

password, username, mins, url = args.password, args.user, int(args.minutes), args.url
# set path
service = Service(
    executable_path="/home/user/webdriver/geckodriver"
    #executable_path="home/user/.cache/selenium/geckodriver/linux64/0.32.0/geckodriver"
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
    startTime=float(time.time())
    if url=="multi":
        numUrl=int(input("Number of urls: "))            
        while numUrl <1:
                numUrl=int(input("Number of urls: "))            
        for x in range (numUrl):
            url=str(input("enter url: "))
            driver.get(url)
            num = driver.find_element(By.CLASS_NAME, 't27kl0s').text
            num=num.split()
            print(num)
            time.sleep(0.1)
            while float(time.time())/numUrl < startTime+mins:
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
    else:
        driver.get(url)
        while float(time.time()) <= float(startTime):
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
