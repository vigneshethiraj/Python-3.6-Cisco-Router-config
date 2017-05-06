'''
This program is used to telnet to the router and configure 
a loopback interface 0 automatically and assign an ip address to it
'''

import getpass
import sys
import telnetlib

#Enter your host IP to which you wish to telnet to instead of x.x.x.x
HOST = "x.x.x.x"

#The below command takes your username as input 
user = input("Enter your telnet username : ")

#This command is used to get your password
password = getpass.getpass()

#Executing the below command is similar to executing "telnet x.x.x.x" in command prompt, this command establishes the telnet session
tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
    
#the below commands will configure the loop back interface
tn.write(b"enable\n")
tn.write(password.encode('ascii') + b"\n")
tn.write(b"conf t\n")
tn.write(b"int loop 0\n")
tn.write(b"ip address 1.1.1.1 255.255.255.255\n")
tn.write(b"end\n")
tn.write(b"exit\n")
print (tn.read_all())
