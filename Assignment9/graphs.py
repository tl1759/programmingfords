import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import datetime
import time
import matplotlib.dates
# def load_data():
# 	global cleandata
# 	rawdata = pd.read_csv("DOHMH_New_York_City_Restaurant_Inspection_Results_raw.csv", low_memory = False)
# 	cleaningdata1 = rawdata.dropna(subset = ['GRADE']) # get the NAN eliminated
# 	cleaningdata2 = cleaningdata1.query('GRADE != "Not Yet Graded"') #get the "Not Yet Graded" eliminated
# 	####convert  'GRADE DATE' to datetime
# 	cleaningdata2 = cleaningdata2.dropna(subset = ['GRADE DATE'])### remember to drop nan!!!!
# 	cleaningdata2['GRADE DATE'] = pd.to_datetime(cleaningdata2['GRADE DATE'],format = '%m/%d/%Y')
# 	###convert datetime to date use date() method
# 	cleaningdata2['GRADE DATE'] = [time.date() for time in cleaningdata2['GRADE DATE']]
# 	###sort the dataframe use time 
# 	cleandata = cleaningdata2.sort(['GRADE DATE'])
# load_data()

# def calculate_grade_eachday(grade):
# 	datearray = (cleandata['GRADE DATE']).unique()
# 	date_grade = {}
# 	for date in datearray:
# 		datemask = cleandata['GRADE DATE']== date#####use mask to get the date index 
# 		dateDF1 = cleandata[datemask] ##get the date dataFrame
# 		# dateDF2 = dateDF1.query('dateDF1[GRADE DATE] !="255/255/1"') #### i WANT TO USE QUERY TO DEL UNVALID DATE
# 		grademask = dateDF1['GRADE'] == grade####get the grade mask 
# 		gradeDF = dateDF1[grademask] ###get the dataframe just contain one date and a sum grade number
# 		date_grade[date] = len(gradeDF)

	
# 	data = pd.Series(date_grade)
# 	# # print data.index
# 	data.plot()
# 	plt.show()

# Borougharray = (cleandata['BORO']).unique()
# def calculate_grade_boro(Borough,grade):
	# """this method can show one grade for each Borough"""
# 	for Borough in Borougharray:
# 		boromask = cleandata['BORO'] ==Borough
# 		cleandata = cleandata[boromask]
# 		datearray = (cleandata['GRADE DATE']).unique()
# 		boro_date_grade = {}
# 		for date in datearray:
# 			datemask = cleandata['GRADE DATE']== date#####use mask to get the date index 
# 			dateDF1 = cleandata[datemask] ##get the date dataFrame
# 		# dateDF2 = dateDF1.query('dateDF1[GRADE DATE] !="255/255/1"') #### i WANT TO USE QUERY TO DEL UNVALID DATE
# 			grademask = dateDF1['GRADE'] == grade####get the grade mask 
# 			gradeDF = dateDF1[grademask] 
		
# 			boroDF = gradeDF[boro_grade_mask]
# 			boro_date_grade[date] = len(boroDF)
# 		data = pd.Series(boro_date_grade)
	
# 		data.plot()
# 	plt.show()


def calculate_boro_grade(Borough):
	rawdata = pd.read_csv("DOHMH_New_York_City_Restaurant_Inspection_Results_raw.csv", low_memory = False)
	cleaningdata1 = rawdata.dropna(subset = ['GRADE']) # get the NAN eliminated
	cleaningdata2 = cleaningdata1.query('GRADE != "Not Yet Graded"') #get the "Not Yet Graded" eliminated
	####convert  'GRADE DATE' to datetime
	cleaningdata2 = cleaningdata2.dropna(subset = ['GRADE DATE'])### remember to drop nan!!!!
	cleaningdata2['GRADE DATE'] = pd.to_datetime(cleaningdata2['GRADE DATE'],format = '%m/%d/%Y')
	###convert datetime to date use date() method
	cleaningdata2['GRADE DATE'] = [time.date() for time in cleaningdata2['GRADE DATE']]
	###sort the dataframe use time 
	cleandata = cleaningdata2.sort(['GRADE DATE'])
	"""this is the method to show one borough with different grades"""
	gradearray = (cleandata['GRADE']).unique()
	print gradearray
	datearray = (cleandata['GRADE DATE']).unique()
	
	
	for grade in gradearray:
		
		boro_date_grade = {}
		grademask = cleandata['GRADE'] == grade
		cleandata = cleandata[grademask]

		for date in datearray:
			datemask = cleandata['GRADE DATE']== date#####use mask to get the date index 
			dateDF1 = cleandata[datemask]
			boromask = dateDF1['BORO'] == Borough####get the grade mask 
			boroDF = dateDF1[boromask]
		print boroDF
			# boro_date_grade[date] = len(boroDF)

	# 	data = pd.DataFrame(boro_date_grade.items())
		
		# data = data.set_index(pd.DatetimeIndex(data[0]))
	# 	# data = data.drop(data['Date'])

		data = data.groupby([pd.TimeGrouper('M'),'number']).sum()
	# print data

		# data.plot()
		# plt.savefig(grade + 'brooklyn.pdf')

calculate_boro_grade('BROOKLYN')
# plt.savefig('brooklyn.pdf')
