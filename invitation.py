from __future__ import print_function
import csv

guestList = "guestList.csv"

with open(guestList, "r") as csvfile:
	guests = csv.reader(csvfile, delimiter=",")
	#guests = [["Manfred","Ute"," "," "," "," "," "," "]]
	for family in guests:
		capital = True
		count = 0
		greeting = ""
		fileName = ""
		for x in xrange(8):
			
			if family[x] != "" and family[x] != "x":
				if x == 0:
					greeting += "Liebe %s, " % family[x]
					capital = False
					count += 1
					fileName = family[x]
				elif x == 1:
					if capital == True:
						greeting += "Lieber %s, " % family[x]
						fileName = family[x]
					else:
						greeting += "lieber %s, " % family[x]
						fileName += family[x]
					count += 1
				elif x == 2 or x == 3 or x == 4:
					greeting += "lieber %s, " % family[x]
					count += 1
				elif x == 5 or x == 6 or x == 7:
					greeting += "liebe %s, " % family[x]
					count += 1
		if count > 1:
			with open("Inlay1.svg") as oldFile, open("../invitations/"+fileName+".svg","wb") as newFile:
				#content = ol.readLines()
				for line in oldFile:
					if '       sodipodi:linespacing="140%"><tspan\n' in line:
						tag = line
						tagList = tag.split(">")
						tagList[0] += ">"
						tagList.insert(1, greeting)
						newLine = " ".join(tagList)
						newFile.write(newLine)
					else:
						newFile.write(line)
		else:
			with open("Inlay1_single.svg") as oldFile, open("../invitations/"+fileName+".svg","wb") as newFile:
				#content = ol.readLines()
				for line in oldFile:
					if '       sodipodi:linespacing="140%"><tspan\n' in line:
						tag = line
						tagList = tag.split(">")
						tagList[0] += ">"
						tagList.insert(1, greeting)
						newLine = " ".join(tagList)
						newFile.write(newLine)
					else:
						newFile.write(line)


# with open("WeddingPlanner - Ga%08steliste detail.csv") as f:
#     for line in f:
#         print(line)
