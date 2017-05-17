# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from bs4 import BeautifulSoup
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import user_agents
import random

def get_picture_url(url):
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["PhantomJS.page.settings.userAgent"] = (random.choice(user_agents.user_agent_list))#加上随机文件头，调用浏览器访问
    driver = webdriver.PhantomJS(desired_capabilities=dcap)#这里使用PhantomJS浏览
    driver.implicitly_wait(10)
    driver.get(url)
    #调用无界面浏览器访问
    pic_list = []
    count = 0
    for i in range(2,100):
        try:
            pic = driver.find_element_by_xpath('//*[@id="altImages"]/ul/li['+str(i)+']')  # 鼠标移动到此元素
            count = count + 1
            pic_list.append(pic)
        except:
            break

        #把这个动作存入列表中（组成一个动作列表）

    action = ActionChains(driver)
    for i in pic_list:
        action.move_to_element(i).perform()  #轮流执行列表中的鼠标移动悬停操作
        sleep(1)#每次悬停间隔一秒

    result_list = [(driver.find_element_by_xpath('//*[@id="landingImage"]')).get_attribute('src')]
    for i in range(7,100):
        try:
            url = driver.find_element_by_xpath('//*[@id="main-image-container"]/ul/li['+str(i)+']/span/span/div/img')
            pic_link = url.get_attribute('src')
            result_list.append(pic_link)
        except:
            break
        #把结果url存入列表中
    sleep(2)
    driver.quit()
    return result_list





