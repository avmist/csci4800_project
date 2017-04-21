import Tkinter as tk
from Tkinter import *




'''
Code that gets the ip address
and port from the user
ip,port = getIpAndPort()
print "ip =",ip,"port =",port
'''
globalIp = -1
globalPort = -1
globalUname = -1
globalPword = -1
def getIpAndPort():
    getIpAndPortWindow()
    return globalIp,globalPort,globalUname,globalPword
def getIpAndPortWindow():
    root = tk.Tk()
    root.title("Nessus Ip Address and Port")
    root.resizable(width=False, height=False)
    root.geometry('300x300')
    Label(root, text="Enter the IP\nAnd Port of the Nessus Server").grid(row=0,column=1)
    Label(root, text="IP").grid(row=1)
    Label(root, text="Port").grid(row=2)
    Label(root, text="Username").grid(row=3)
    Label(root, text="Password").grid(row=4)
    ip = Entry(root)
    port = Entry(root)
    uname = Entry(root)
    pword = Entry(root,show='*')
    ip.grid(row=1, column=1)
    port.grid(row=2, column=1)
    uname.grid(row=3, column=1)
    pword.grid(row=4, column=1)
    def submit():
        global globalIp
        global globalPort
        global globalUname
        global globalPword
        globalIp = ip.get()
        globalPort = port.get()
        globalUname = uname.get()
        globalPword = pword.get()
        root.destroy()
    Button(root,text="OK",width=20,command=submit).grid(row=5,column=1)
    root.mainloop()












'''
Code to allow the user to select the scan from a list
scanVal = getChosenScan(["a","b","c"])
print scanVal
'''
globalScan = -1
def getChosenScan(scanList):
    getChosenScanWindow(scanList)
    return globalScan
def getChosenScanWindow(scanList):
    root = tk.Tk()
    root.title("Select Scan")
    root.resizable(width=False, height=False)
    root.geometry('200x200')
    Label(root, text="Select the Scan").grid(row=0,column=1)
    scan = StringVar(root)
    scan.set(scanList[0])
    dropDown = apply(OptionMenu,(root, scan) + tuple(scanList))
    dropDown.grid(row=1,column=1)
    def submit():
        global globalScan
        globalScan = scan.get()
        root.destroy()
    Button(root,text="OK",width=10,command=submit).grid(row=3,column=1)
    root.mainloop()    










class Option():
	def __init__(self,optionString,root,col,ro):
		self.var = IntVar()
		self.option = optionString
		self.chk = Checkbutton(root,text=optionString,variable=self.var)
		self.chk.grid(sticky="W",row=ro,column=col)




'''
'''
fileDest = -1
optionList = -1
fileName = -1
def getChosenOptions(options):
    getChosenOptionsWindow(options)
    return fileDest,optionList
def getChosenOptionsWindow(options):
    root = tk.Tk()
    root.title("Select Options")
    root.resizable(width=False, height=False)
    root.geometry('600x400')
    Label(root, text="Select Options").grid(sticky="W",row=0,column=0)
    optionCheckList = []
    column = 0
    row = 1
    for option in options:
        optionCheckList.append(Option(option,root,column,row))
        row += 1
    def browseDirectory():
        global fileDest
        from tkFileDialog import askdirectory
        fileDest = askdirectory()
    def getCheckedOptions(optionCheckList):
        localList = []
        for opt in optionCheckList:
            if opt.var.get() == 1:
                localList.append(opt.option)
        return localList
    def getFileDest():
        return fileDest+"/"+fileName.get()   
    def submit():
        global fileDest
        global optionList
        global documentType
        optionList = getCheckedOptions(optionCheckList)
        fileDest = getFileDest()
        root.destroy()
    Label(root, text="Set File Name:").grid(sticky="W",row=row,column=0)
    fileName = Entry(root)
    row+=1
    fileName.grid(sticky="W",row=row,column=0)
    row+=1
    Button(root, text='Set Output Directory', command=browseDirectory).grid(sticky="W",row=row,column=0)
    row+=1
    Button(root,text="Create File",width=10,command=submit).grid(sticky="W",row=row,column=0)
    root.mainloop()
    
