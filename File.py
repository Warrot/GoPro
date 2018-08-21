#All changed must be made in the pi version


import glob
import os
import time

#Loop over the amount of pictures we want to move
for i in range(3,0,-1):
	#Fetch newest file
	list_of_files = glob.iglob('/Users/Nicolai/Documents/Python/GoPro/*.JPG') # * means all if need specific format then *.csv
	latest_file = max(list_of_files, key=os.path.getctime)

	#Create new name for the file
	newName = time.strftime("%Y_%m_%d_%H_%M_"+str(i))+".JPG"
	
	#Check whether morning or evening
	if int(time.strftime('%H')) > 12:
		#Change name and path of the file
		os.rename(latest_file, '/Users/Nicolai/Documents/Python/GoPro/Evening/'+str(i)+'/'+newName)
	else:
		os.rename(latest_file, '/Users/Nicolai/Documents/Python/GoPro/Morning/'+str(i)+'/'+newName)

