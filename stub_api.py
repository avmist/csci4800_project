def login(ip,username,password,port):
	print "logging in to",ip,":",port,"with username",username,"and password",password

def get_scans():
	print "making an api call to get the scan list"
	return ["scan1","scan2","scan3","scan4","scan5"]

def get_scan_data(scan):
	print "making an api call to get scan data options from", scan
	return ["option1","option2","option3","option4","option5","this is another option"]

def createDocument(chosenOptionsList,fileLocation):
    print "creating file at",fileLocation,"with options",chosenOptionsList
    resultFile = open(fileLocation,"w")
    resultFile.write("this goes in the file"+str(chosenOptionsList))
    resultFile.close()
	
