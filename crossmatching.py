import numpy as np
def hms2dec(a,b,c):
  return ( 15*(a+ (b/60) +(c/3600)))
def dms2dec(d,e,f):
  if d>=0:
    return ( d+ (e/60) + (f/3600))
  else:
    return  -1*((abs(d)+ (e/60) + (f/3600)))
def import_bss():
  bss= np.loadtxt('bss.dat', usecols=range(1,7))
  final=[]
  count=0
  for i in bss:
    row=[]
    count+=1
    row.append(count)
    ra=hms2dec(i[0],i[1],i[2])
    de=dms2dec(i[3],i[4],i[5])
    row.append(ra)
    row.append(de)
    final.append(tuple(row))  
  return final
def import_super():
  super1=np.loadtxt('super.csv',delimiter=',',skiprows=1,usecols=[0,1])
  final1=[]
  count=0
  for i in super1:
    row=[]
    count+=1
    row.append(count)
    for j in i:
      row.append(j)
    final1.append(tuple(row))
  return final1
def crossmatch(cat,supercat,maximum):
  count1=0
  temp=0
  match=[]
  unmatch=[]
  for j in cat:
    closest_dist = np.inf
    count=0
    count1+=1
    ra1=np.radians(j[1])
    dec1=np.radians(j[2])
    for i in supercat:
      count+=1
      ra2=np.radians(i[1])
      dec2=np.radians(i[2])
      a=np.sin((dec1-dec2)/2)**2
      b=np.cos(dec1)* np.cos(dec2)*(np.sin((abs(ra1-ra2))/2)**2)
      d=2*np.arcsin(np.sqrt(a+b))
      if d< closest_dist:
        closest_dist = d
        temp=np.degrees(closest_dist)
    if temp>maximum:
      unmatch.append(count1)
    else:
      match.append((count1,count,temp))
        
  return match,unmatch
bss_cat = import_bss()
super_cat = import_super()
max_dist = 40/3600
matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
print(matches)
