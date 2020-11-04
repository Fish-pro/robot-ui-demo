from hyrobot.common import *
from selenium import webdriver
import time


class TestLogin:
    cases = [
        ('登录 - c00101', 'byhy1','888888'),
        ('登录 - c00102', 'byh','888888'),
        ('登录 - c00103', '','888888'),
    ]

    def teststeps(self, para_index):
        # 取出参数
        username, password = self.cases[para_index][1:]
        # 下面写登录流程

        driver = webdriver.Chrome()
        driver.implicitly_wait(10)

        driver.get('http://127.0.0.1/mgr/sign.html')

        driver.find_element_by_id('username').send_keys(username)
        driver.find_element_by_id('password').send_keys(password)
        driver.find_element_by_css_selector('button[type="submit"]').click()

        time.sleep(2)
        alterText = driver.switch_to.alert.text
        print(alterText)
        CHECK_POINT('弹出提示', alterText == '登录失败 : 用户名或者密码错误')


        driver.quit()
