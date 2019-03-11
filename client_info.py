from uuid import getnode
from flask import request
import uuid


def clientInfo():
    mylist=[]
    import uuid
    macNumber = getnode()
    # print("Unique id : ", macNumber)
    # unique_id="Unique id : ",macNumber
    mylist.append(macNumber)

    import re, uuid
    macAddress = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    #print("MAC Address : ",macAddress)
    #mac_address="MAC Address : ",macAddress
    mylist.append(macAddress)

    import socket
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    #print("IP Address : ",IPAddr)
    #ip_address="IP Address : ",IPAddr
    mylist.append(IPAddr)

    import geocoder
    g = geocoder.ip('me')
    #print("Location : ",g.latlng[0], g.latlng[1])
    #location_address="Location :  ",g.latlng[0], g.latlng[1]
    mylist.append(g.latlng)

    return mylist

#print(clientInfo())
