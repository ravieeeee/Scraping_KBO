from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os

default_date = "20171003"
teamSet = []
managerD = {}
coachD = {}
pitcherD = {}
catcherD = {}
infielderD = {}
outfielderD = {}

def find_dictionary(ctgC):
	if ctgC == 0 :
		return managerD
	elif ctgC == 1 :
		return coachD
	elif ctgC == 2 :
		return pitcherD
	elif ctgC == 3 :
		return catcherD
	elif ctgC == 4 :
		return infielderD
	else :
		return outfielderD


# driver = webdriver.Chrome(os.environ['chrome_driver_loc'])
driver = webdriver.PhantomJS(os.environ['phantomjs_loc'])
driver.get("https://www.koreabaseball.com/Player/RegisterAll.aspx")

# 대기 - 팀 목록
try :
	WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "fir")))
except TimeoutException :
	print("Time out!!!")
# 팀 목록
teams = driver.find_elements_by_class_name("fir")
for team in teams :
	teamSet.append(team.text)
print(teamSet)


# 현재 날짜
date = driver.find_element_by_id("cphContents_cphContents_cphContents_hfSearchDate").get_attribute("value")
ctgC = 0
teamC = 0
all_info = driver.find_element_by_tag_name("tbody").find_elements_by_tag_name("td")
for info in all_info :
	dic = find_dictionary(ctgC)
	tmpL = []

	for i in range(0, len(info.find_elements_by_tag_name("li"))) :
		tmpL.append(info.find_elements_by_tag_name("li")[i].text)
		dic[teamC] = tmpL

	if info.get_attribute("class") == "last" :
		teamC += 1

	ctgC = ctgC + 1 if (ctgC != 5) else 0
print(date)
for i in range(0, len(teamSet)) :
	print(teamSet[i])
	print(managerD[i])
	print(coachD[i])
	print(pitcherD[i])
	print(catcherD[i])
	print(infielderD[i])
	print(outfielderD[i])
	print("----------")


# 대기 - 날짜 이동버튼 클릭가능까지
try :
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cphContents_cphContents_cphContents_btnPreDate")))			
except TimeoutException :
	print("Time out!!!")
# 이전 날짜로
driver.find_element_by_id("cphContents_cphContents_cphContents_btnPreDate").click()


date = default_date
# 요일을 locator로 잡기. call시 in으로 검사해서 가능
try :
	WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, "cphContents_cphContents_cphContents_lblGameDate"), "월"))
except TimeoutException :
	print("Time out!!!")
# while date == driver.find_element_by_id("cphContents_cphContents_cphContents_hfSearchDate").get_attribute("value") :
# 	driver.implicitly_wait(10)
date = driver.find_element_by_id("cphContents_cphContents_cphContents_hfSearchDate").get_attribute("value")
print(date)


driver.close()
