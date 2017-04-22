from gui_windows import getIpAndPort,getChosenScan,getChosenOptions
from nessus import login,get_scans,get_scan_data,createDocument

login = {} # JSON object for holding login info
base_url = ''
ip = -1
port = -1
ip,port,username,password = getIpAndPort()                                                #get the ip and port of the nessus server from the user
login = {'username':username,'password':password}
base_url = 'https://' + ip + ':' + port

scanList = get_scans(login,base_url)                                             #get the test list from the nessus server

for scan in scanList:
	print scan
chosenScan = getChosenScan(scanList)                                        #get the selected test from the user

optionsList = get_scan_data(login,base_url,chosenScan)                                #get the options available for chosenTest from the nessus server

fileLocation,chosenOptionsList = getChosenOptions(optionsList) 			#get chosen options from user

createDocument(login,base_url,chosenScan,chosenOptionsList,fileLocation)

