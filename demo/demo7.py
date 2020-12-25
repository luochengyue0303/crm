# -*-coding:UTF-8 -*-
from time import sleep

from pymysql import connect
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome('../Chromdriver.exe/chromedriver.exe')
driver.get('http://192.168.1.4/ecshop/admin/privilege.php?act=login')
driver.maximize_window()

driver.find_element_by_name('username').send_keys('caichang')
driver.find_element_by_name('password').send_keys('caichang1')
driver.find_element_by_class_name('btn-a').click()

ActionChains(driver).move_to_element(driver.find_elements_by_link_text('个人设置')).perform()
dirver.find_element_by_link_text('退出').click()

driver.switch_to_frame('menu-frame')
driver.find_element_by_link_text('商品列表').click()
driver.switch_to.default_content()
driver.switch_to.frame('main-frame')


driver.find_element_by_name('keyword').send_keys('车')
driver.find_element_by_xpath("//input[@value=' 搜索 ']").click()
sleep(1)
webname = driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[2]/span').text
webname_total = driver.find_element_by_id('totalRecords').text

print(webname)
conn = connect(host='192.168.1.4',user='root',password='root',database='ecshop',port=3306)
cursor = conn.cursor()
cursor.execute("select goods_name from ecs_goods where goods_name like '%车%'")

rs = cursor.fetchall()
cursor.execute("select count(*) from ecs_goods where goods_name like '%车%'")
total = cursor.fetchone()

if webname ==rs[0][0] and int(webname_total) ==total[0] :
    print('测试通过')
else:
    print("测试不通过")
cursor.close()
conn.close()
