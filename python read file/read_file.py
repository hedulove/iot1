def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches


from datetime import datetime, timedelta

#d = datetime.today() - timedelta(days=days_to_subtract)
#now = datetime.datetime.now()
yesterday = datetime.today() - timedelta(days=1)
print(yesterday)
strYesterday = yesterday.strftime("%Y-%m-%d")
print(strYesterday+'beacon.txt') #

with open(strYesterday+'beacon.txt', 'r') as myfile:
  data = myfile.read()


beaconsList = [
"c17bf9d6b5c1b713",
"d7dae549a2c29874",
"e875c10477754cb5",
"63e420c70fa653d3",
"0a20e1976661772a",
"94626b9331b47a21",
"f22afb64888f5040",
"ff6117525a5a95c6",
"eccd46812fe3ca78",
"9c0a06ce633a7482",
"01056505f733cd1f"
]
  
  
#print (data)
#print (type(data))
for beaconId in beaconsList: 
    listPositionsBeacons = list(find_all(data, beaconId)) # [0, 5, 10, 15]
    print (beaconId, end='')
    print ("  ", end='')
    print (len(listPositionsBeacons))