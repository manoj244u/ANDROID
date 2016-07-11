import re
str = "welcome to P3 solutions";
matchobj = re.match(r'welcome', str, re.M|re.I)
if matchobj:
  print ("match ----> matchobj.group(): ", matchobj.group())
else:
  print ( "No matching")
searchobj = re.search(r'welcome', str, re.M|re.I)
if searchobj:
  print ("search----->searchobj.group()", searchobj.group())
else:
  print ("No elemenrt fond in string")