import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import csv
import play
from play import test_grades,test_restaurant_grades,test_nyc_restaurant_grades

class assessTools():
	"""This is a tool to assess the quality of restaurant of New York city"""

	def __init__(self,Borough):
		"""this is the initialization of the class"""
		self.Borough = Borough

	def test_Borough_restaurant_grade(self):
		"""this is the method to calculate each borough's restaurants GRADE"""
		Borough = self.Borough ####inherit from init 
		boromask = cleandata['BORO'] == Borough ##create a mask for each bogrough
		data = cleandata[boromask] ##use the mask to get each borough's data
		boro_camisarray = data.CAMIS.unique() ###get the unique CAMIS_ID
		boro_tempList = []
		for i in range(len(boro_camisarray)):
			this_id = boro_camisarray[i]
			n = test_restaurant_grades(this_id)
			boro_tempList.append(n)
		return sum(boro_tempList)

if __name__ == '__main__':
	rawdata = pd.read_csv("DOHMH_New_York_City_Restaurant_Inspection_Results_raw.csv", low_memory = False)
	cleaningdata1 = rawdata.dropna(subset = ['GRADE']) # get the NAN eliminated
	cleaningdata2 = cleaningdata1.query('GRADE != "Not Yet Graded"') #get the "Not Yet Graded" eliminated
	cleaningdata2['GRADE DATE'] = pd.to_datetime(cleaningdata2['GRADE DATE'],format = '%m/%d/%Y')
	

	# cleandata.sort('GRADE DATE')
	cleandata = cleaningdata2.sort(['GRADE DATE'])
	Borolist = ['MANHATTAN','BROOKLYN','QUEENS','BRONX','STATEN ISLAND']
	for ele in Borolist:
		print ele + "'s restaurants grade is " + str(assessTools(ele).test_Borough_restaurant_grade())+'.'
	print 'NYC restaurants grade is '+ str(test_nyc_restaurant_grades())+'.'


