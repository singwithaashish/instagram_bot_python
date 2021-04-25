from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from secrets import pw


path = "/home/aashish/Documents/chromedriver"
driver = webdriver.Chrome(path)
action = ActionChains(driver)
all_people = []


def login(username, password):
    driver.get("https://www.instagram.com")
    sleep(0.5)
    # un_field = driver.find_element_by_xpath('.//*[@id="loginForm"]/div/div[1]/div/label/input')
    un_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))
    # pw_field = driver.find_element_by_xpath('.//*[@id="loginForm"]/div/div[2]/div/label/input')
    pw_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')))
    un_field.send_keys(username)
    pw_field.send_keys(pw)
    login_button = driver.find_element_by_xpath('.//*[@id="loginForm"]/div/div[3]/button')
    login_button.click()
    t_now = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
    not_now = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))
    not_now.click()
    not_now_notif = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, './html/body/div[4]/div/div/div/div[3]/button[2]')))
    not_now_notif.click()
    see_all_sugg = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, './/*[@id="react-root"]/section/main/section/div[3]/div[2]/div[1]/a')))
    see_all_sugg.click() #we are now in suggestion
    check_and_follow()


def check_and_follow():
    #while endOfList, check if follower / following > 1 ? follow
    # sleep(2)
    scrl = 0
    max_scrl = driver.execute_script("return document.body.scrollHeight")
    while scrl < max_scrl:
        scrl = max_scrl
        sleep(2)
        driver.execute_script("scroll(0, document.body.scrollHeight)")
        max_scrl = driver.execute_script("return document.body.scrollHeight")
    sleep(2)
    all_people = driver.find_element_by_xpath('.//*[@id="react-root"]/section/main/div/div[2]/div/div').find_elements_by_tag_name("a")
    # print(all_people)
    driver.execute_script("scroll(0, 0)") #move to top again
    
    all_buttons = driver.find_elements_by_class_name("sqdOP, L3NKy, y3zKF")
    
    scrl = 0

    
    for p in all_people:
        # driver.execute_script("scroll(0, arguments[0].getBoundingClientRect().top)", p)
        action.move_to_element(p).perform()
        
        
        no_of_fol = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div[2]/div/div/div[2]')))
        following = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div[2]/div/div/div[3]')))
        foer_num = int(''.join(i for i in no_of_fol.text if i.isdigit())) #[int(word) for word in no_of_fol.text.split() if word.isdigit()].append()
        foing_num = int(''.join(i for i in following.text if i.isdigit())) #[int(word) for word in following.text.split() if word.isdigit()]
        try:
            # print(foer_num/foing_num)
            if foer_num > foing_num and foer_num < 1000:
                try:
                    follow_b = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div[4]/button')))
                    if(follow_b.text == "Follow"):
                        follow_b.click()
                    else:
                        print("Already followed")
                    print(f"followed {p.get_attribute('title')} who had {foer_num} followers and {foing_num} followings")
                except:
                    print("couldn't click follow button")
            else:
                print(f"didn't followed {p.get_attribute('title')} because {foer_num} followers and {foing_num} followings")
        finally:
            print("something went wrong", foer_num)
        # /html/body/div[5]/div/div/div[4]/button -> follow xpath
        # driver.execute_script("scroll(0, window.scrollY + 30)")
        # 
    
    # print(driver.find_elements_by_xpath('//*[class:"g47SY" or class:"l0XF2"]')[1].text)

login("ramro_keto_", pw)

