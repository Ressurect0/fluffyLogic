#!/usr/bin/python3

import sys
import json
import os
import subprocess

#Fetch the current working directory
curDir = os.getcwd()

# Fetching the arguments
service=str(sys.argv[1])
check=str(sys.argv[2])

# Fetching the iplist
tmp = open(curDir+"/"+str(sys.argv[3]))
tmp2=tmp.read().strip("\n").split(", ")
tmp.close()
# Removing blank fields
while ('' in tmp2):
        tmp2.remove('')

iplist=tmp2
print("iplist: ",iplist)

finalip = []

if (len(sys.argv) == 1):
        print("Syntax: ./diagnostic.py <service> <check> <iplist>\r\nFor eg. ./diagnostic.py DNS CVE-2005-1794 iplist.txt")
else:


        # Importing the config.json
        tmp = open(curDir+"/config.json")
        configJson =json.loads(tmp.read())
        tmp.close()

        print("Service: "+service+"\r\nCheck: "+check)

        # Execute the command
        tmp=configJson[service][check]['command']
        tmp=tmp.replace("<path>",curDir+"/bin/")

        for ip in iplist:
                # Substitute IP and port
                tmp4=tmp.replace("<IP>",ip.split(":")[0])
                tmp4=tmp4.replace("<port>",ip.split(":")[1])
                	
                cmd=tmp4.split(" ")
                tmp3 = subprocess.run(cmd, stdout=subprocess.PIPE)
                result = tmp3.stdout.decode('utf-8')
                print(result)

                # Check if True Positive
                if configJson[service][check]['confirm_string'].lower() in result.lower():
                        finalip.append(ip)

        # Print final IP list
        for i in finalip:
                print(i)

