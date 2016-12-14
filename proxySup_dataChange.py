#!/usr/bin/env python
#-*- coding: utf-8 -*-



import socket

#for exit, argv
import sys

# import _thread //python3
import thread



HOST = '127.0.0.1'
PORT = 8080

maxConn = 5 # max amount of connections to my proxy server. maybe 1 is OK.
bufSize = 4096

proxyAddr = (HOST, PORT)






def proxyFunc(targetUrl, port, cs, data, addr, dataFrom, dataTo):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((targetUrl, port))

    data = data.replace('gzip,', '     ')
    print(data)
    s.send(data)
    a=1
    while(1):
        response = s.recv(bufSize)
        #dataChange

        if(type(dataFrom) == int and type(dataTo) == int):
            #default
            response = response.replace('hacking', 'ABCDEFG')
            response = response.replace('Michael', 'GILBERT')
            
        else:
            response = response.replace(dataFrom, dataTo)
            
        if(len(response)>0):
	    print(a)
	    a=a+1
            #print(response) for test
            cs.send(response)
        else:
            break

    s.close()
    cs.close()



def func(cs, data, addr, dataFrom, dataTo):
    try:  
        targetPort = 80
        #normal HTTP
        
        first_line = data.split('\n')[0]
        # get first line by parsing
        #print(first_line) for test

        #targetUrl = "http://" + first_line.split('/')[2]
        #socket.gaierror .. 

        targetUrl = first_line.split('/')[2]
        
        # get target Url by parsing    
        # print(targetUrl) for test
        
        proxyFunc(targetUrl, targetPort, cs, data, addr, dataFrom, dataTo)
    except Exception, e:
        pass




if __name__ == "__main__":
   # try:
	# ss means server socket

        dataChangeFrom, dataChangeTo = (1,1) # will be parameter

        if(len(sys.argv) == 1):
            pass
        elif(len(sys.argv) == 2 and sys.argv[1] == '-D'):
            dataChangeFrom = raw_input('input string, change from : ')
            dataChangeTo = raw_input('input string, change to : ')
            #because python2;;
        else :
            print("Not Implemented!")
            exit(-1)
	
	ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	ss.bind(proxyAddr)

	ss.listen(maxConn)

	#for k in range(1):
	while 1:
	    (cs, addr) = ss.accept() # cs means connection socket from client
	    data = cs.recv(bufSize) # receive client data
	    #type(data) == str
	    
	    thread.start_new_thread(func,(cs, data, addr, dataChangeFrom, dataChangeTo))
	    
	    #print(data)    
	    
	    
	ss.close()
   # except



    

    
    
