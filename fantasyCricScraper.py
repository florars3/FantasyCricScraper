from selenium import webdriver
import time, math, random, lxml.html
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

print "Bowler list:",total_list

listOfElem1 =[]
#batsman = driver.find_elements_by_xpath("//*[@id=\"full-scorecard\"]/div[2]/div//table/tbody//tr//td/a[contains(@class, 'playerName')]")

batsmanTotal = 0 
#import lxml.html
tree = lxml.html.parse('http://www.espncricinfo.com/indian-premier-league-2016/engine/match/980919.html')
batting = tree.xpath("//table[@class='batting-table innings']/tr[not(@*)]")
for player in batting:
	Batsman={}
	Batsman['PlayerName'] = player.xpath("./td[@class='batsman-name']/a/text()")[0]
	runs = player.xpath("./td[4]/text()")[0]
	balls = player.xpath("./td[6]/text()")[0]
	fours = player.xpath("./td[7]/text()")[0]
	sixes = player.xpath("./td[8]/text()")[0]
	strikeRate = player.xpath("./td[9]/text()")[0]

	
	batsmanTotal = 0
	runs = int(runs)

	bonus = math.floor(runs/25)*10
	if (int(balls) > 0 and runs > 0 ):
		strikeRate = (float(strikeRate))
		sixes = (float(sixes))
		if (runs >=10):
			if (strikeRate == 0.00 and strikeRate <= 74.99):
				batsmanTotal -= 15
			elif (strikeRate > 74.99 and strikeRate <= 99.99):
				batsmanTotal -= 10
			elif (strikeRate > 99.9 and strikeRate <=149.99):
				batsmanTotal += 5
			elif (strikeRate > 150.00 and strikeRate <=199.99):
				batsmanTotal += 10
			else:
				batsmanTotal += 15

		if (sixes > 0 ):
			batsmanTotal  += 2*sixes 
	elif int(runs) == 0:
		batsmanTotal -= 5
	batsmanTotal +=runs
	batsmanTotal +=bonus
	Batsman['Points'] = batsmanTotal

	#print "total val is: ", total
	listOfElem1.append(Batsman)

print "Batsman Points:",listOfElem1
