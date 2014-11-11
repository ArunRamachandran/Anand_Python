''' Write a program myip.py to print the external IP address of the machine.
Use the response from http://httpbin.org/get and read the IP address from 
there. The program should print only the IP address and nothing else. '''

import requests
'''
r = requests.get(r'http://httpbin.org/get')
ip = r.json()['ip']
print 'Your IP is ', ip
'''

r = requests.get('http://httpbin.org/get')
ip= r.json()['origin']    #'origin' indicate the name of the corresponding field
print ip

# to get all the fields-- try " ip = r.text" instead of "ip = r.json()['origin']

