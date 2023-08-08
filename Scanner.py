import threading 
import socket 
 
target = '51.81.42.14' 
#ip = socket.gethostbyname(target) 
 
def portscan(port): 
 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.settimeout(0.5)# V 
 
    try: 
        con = s.connect((target,port)) 
 
        print('Port :',port,"is open.") 
 
        con.close() 
    except:  
        pass 
r = 1  
for x in range(1,65535): 
 
    t = threading.Thread(target=portscan,kwargs={'port':r}) 
 
    r += 1 
    t.start() 
