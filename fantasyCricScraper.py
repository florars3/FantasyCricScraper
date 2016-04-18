from selenium import webdriver
import time, math, random
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException



driver = webdriver.Chrome()
driver.get('http://www.espncricinfo.com/indian-premier-league-2016/engine/match/980919.html')

statu = driver.find_elements_by_xpath("//table[@class=\"bowling-table\"]/tbody/tr")
listOfElem = []
total_list = []

for elem in statu:
	blah = elem.text
	st = str(blah)
	listOfElem.append(st.split())
	listOfElem = [var for var in listOfElem if var]

for element in listOfElem:
	element[0:2] = [''.join(element[0:2])]
	Player ={}
	total = 0
	if (len(element) >8):
		Player['PlayerName'] = element[0]
		overs = element[1]
		maidens = element[2]
		runs = element[3]
		wickets = element[4]
		econ = element[5]
		dots = element[6]

		econ = float(econ)
		if (econ >= 0.00 and econ <= 5.00):
			total += 15
		elif (econ >= 5.01 and econ <= 8.00):
			total += 10
		elif (econ >= 8.01 and econ <= 10.00):
			total += 5
		elif (econ >= 10.01 and econ <=12.00):
			total -= 10
		elif(econ >12):
			total -= 15

		if(int(maidens) > 0 ):
			total += int(maidens)*20

		if(int(dots) > 0):
			total += int(dots)*1

		wic = int(wickets)
		if(wic >0):
			total += ((wic*20) + (wic-1)*10)

		Player['Points'] = total
		total_list.append(Player)

print "total_list is:",total_list
