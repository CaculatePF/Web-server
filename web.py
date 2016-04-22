import socket
import signal
import errno
#from time import sleep
  
#p = open('C:/Users/cpf/Desktop/myhtml.html')
#for line in p:
#    print(line)
def HttpResponse(header,whtml):  
    f = open(whtml)  
    contxtlist = f.readlines()
    context = ''.join(contxtlist)  
    response = "%s %d\n\n%s\n\n" % (header,len(context),context)  
    response=response.encode('UTF-8')
    return response  
  
def sigIntHander(signo,frame):  
    print ('get signo# ',signo  )
    global runflag  
    runflag = False  
    global lisfd  
    lisfd.shutdown(socket.SHUT_RD)  
  
strHost = ""  
HOST = strHost #socket.inet_pton(socket.AF_INET,strHost)  
PORT = 20014  
  
httpheader = '' 
'''\ 
HTTP/1.1 200 OK 
Context-Type: text/html 
Server: Python-slp version 1.0 
Context-Length: '''  
  
lisfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
lisfd.bind((HOST, PORT))  
lisfd.listen(2)  
  
signal.signal(signal.SIGINT,sigIntHander)  
  
runflag = True  
while runflag:  
    try:  
        confd,addr = lisfd.accept()  
    except socket.error as e:  
        if e.errno == errno.EINTR:  
            print ('get a except EINTR')  
        else:  
            raise  
        continue  
    print ("connect by ",addr) 
    data = confd.recv(1024)  
    if not data:  
        break  
    print (data)  
    confd.send(HttpResponse(httpheader,'C:/Users/cpf/Desktop/myhtml.html'))  
    confd.close()  
else:  
    print ('runflag#',runflag) 
print ('Done')  
