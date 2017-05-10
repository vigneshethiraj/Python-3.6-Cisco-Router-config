'''
This program is used to telnet to 2 routers and assign ip address to its interfaces

Topology:
    
 Host------------fa4/0(R1)fa0/1-------------------------fa1/0(R2)fa5/0--------------Host
             10.0.0.55   20.0.0.1                   20.0.0.2    11.0.0.55
'''

import getpass
import sys
import telnetlib

number = int(input("enter number of routers that you wish to configure: "))
#Enter your host IP to which you wish to telnet to instead of x.x.x.x


#The below command takes your username as input 
user = input("Enter your telnet username : ")

#This command is used to get your password
password = getpass.getpass()
for i in range (0,number,1):
    HOST = ["9.0.0.1" , "9.0.0.2"]  #Enter your host IPs seperated by a comma 
#Executing the below command is similar to executing "telnet x.x.x.x" in command prompt, this command establishes the telnet session
    tn = telnetlib.Telnet(HOST[i])

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    

#change the below code as per your requirement, if more than 2 routers are required to be configured
#then add 1 more if statement by copy pasting the below code.
    
    if i == 0:
        #the below commands will configure the interface and assigns IP to it
        tn.write(b"enable\n")
        tn.write(password.encode('ascii') + b"\n")
        tn.write(b"conf t\n")
        tn.write(b"int fa4/0\n")
        tn.write(b"ip address 10.0.0.55 255.255.255.0\n")
        tn.write(b"exit\n")
        tn.write(b"int fa0/1\n")
        tn.write(b"ip address 20.0.0.1 255.255.255.0\n")
        tn.write(b"end\n")
        tn.write(b"exit\n")
        print (tn.read_all())

    if i == 1:
        #the below commands will configure the interface and assigns IP to it
        tn.write(b"enable\n")
        tn.write(password.encode('ascii') + b"\n")
        tn.write(b"conf t\n")
        tn.write(b"int fa5/0\n")
        tn.write(b"ip address 11.0.0.55 255.255.255.0\n")
        tn.write(b"exit\n")
        tn.write(b"int fa1/0\n")
        tn.write(b"ip address 20.0.0.2 255.255.255.0\n")
        tn.write(b"end\n")
        tn.write(b"exit\n")
        print (tn.read_all())
        
'''
Output sample:
    b'\r\nRouter1>enable\r\nPassword: \r\nRouter1#conf t\r\nEnter configuration commands, one per line.  End with CNTL/Z.\r\nRouter1(config)#int fa4/0\r\nRouter1(config-if)#ip address 10.0.0.55 255.255.255.0\r\nRouter1(config-if)#exit\r\nRouter1(config)#int fa0/1\r\nRouter1(config-if)#ip address 20.0.0.1 255.255.255.0\r\nRouter1(config-if)#end\r\nRouter1#exit\r\n'
b'\r\nRouter2>enable\r\nPassword: \r\nRouter2#conf t\r\nEnter configuration commands, one per line.  End with CNTL/Z.\r\nRouter2(config)#int fa5/0\r\nRouter2(config-if)#ip address 11.0.0.55 255.255.255.0\r\nRouter2(config-if)#exit\r\nRouter2(config)#int fa1/0\r\nRouter2(config-if)#ip address 20.0.0.2 255.255.255.0\r\nRouter2(config-if)#end\r\nRouter2#exit\r\n'
'''