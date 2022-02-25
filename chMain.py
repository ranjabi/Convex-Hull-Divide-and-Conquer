from cgi import print_environ
from hashlib import sha224
from traceback import print_exception
import numpy as np
import pandas as pd
from numpy import linalg as LA
import matplotlib.pyplot as plt
from sklearn import datasets
from sqlalchemy import true
data = datasets.load_iris()
#create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)
print(df.shape)
df.head()

bucketInput = []
verticesOutput = []

#visualisasi hasil ConvexHull
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
plt.figure(figsize = (10, 6))
colors = ['b','r','g']
plt.title('Petal Width vs Petal Length')
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])
# for i in range(len(data.target_names)):
for i in range(0,3):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[0,1]].values
    bucketInput.append(bucket)
    hull = ConvexHull(bucket) #bagian ini diganti dengan hasil implementasi

    for pt in hull.vertices:
        # print("xv: ", bucket[pt, 0], ", yv: ", bucket[pt, 1])
        verticesOutput.append(bucket[pt])

# ConvexHull Divide & Conquer
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    for simplex in hull.simplices:
        plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i])
plt.legend()
# print(len(bucketInput[0]))
bucketInput = bucketInput[0]
for elmt in bucketInput:
    print(elmt)
print("hull point:")
for elmt in verticesOutput:
  print(elmt)
  
def find_p1(array):
  # cari x paling kiri, return y nya juga
  min = array[0]
  for i in range(len(array)):
    if (array[i][0]<=min[0]):
      min = array[i]
  return min

def find_pn(array):
  # cari x paling kanan, return y nya juga
  max = array[0]
  for i in range(len(array)):
    if (array[i][0] >= max[0]):
      max = array[i]
  return max

def find_det(p1, pn, arrayDet):
  x1 = p1[0]
  y1 = p1[1]
  x2 = pn[0]
  y2 = pn[1]
  x3 = arrayDet[0]
  y3 = arrayDet[1]
  a = np.array([[x1,y1,1], [x2,y2,1], [x3,y3,1]]) 
  return (np.linalg.det(a))

s1 = [] # atas
s2 = [] # bawah

def printPosNeg(bucketone, s1, s2, p1, pn):
  posDet=0
  negDet=0
  zeroDet=0
  for i in range(len(bucketone)):
    det = find_det(p1, pn, bucketone[i])
    status=""
    if (det>(0)):
      posDet+=1
      status="pos"
      s1.append(bucketone[i])
    elif (det<0):
      negDet+=1
      status="neg"
      s2.append(bucketone[i])
    else:
      zeroDet+=1
      status="zero"
    #   bucketone = np.delete(bucketone,i)
    print(bucketone[i], det, status)
    
  # print("posDet:", posDet, "negDet:", negDet, "zeroDet:", zeroDet)
  
p1 = find_p1(bucketInput)
pn = find_pn(bucketInput)
print("min ", p1)
print("max ", pn)
printPosNeg(bucketInput,s1,s2,p1,pn)

def printList(list):
    for x in list:
        print(x)
print("s1:")
printList(s1)
print("s2:")
printList(s2)

def findNorm(p1,p2,p3):
    return (LA.norm(np.cross(p2-p1, p1-p3))/LA.norm(p2-p1))

    
s1p1 = p1 #
s1pn = pn #
print("s1p1, s1pn:", s1p1, s1pn)

# A utility function to calculate area
# of triangle formed by (x1, y1),
# (x2, y2) and (x3, y3)
 
def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0)
 
 
# A function to check whether point P(x, y)
# lies inside the triangle formed by
# A(x1, y1), B(x2, y2) and C(x3, y3)
def isInside(x1, y1, x2, y2, x3, y3, x, y):
 
    # Calculate area of triangle ABC
    A = area (x1, y1, x2, y2, x3, y3)
 
    # Calculate area of triangle PBC
    A1 = area (x, y, x2, y2, x3, y3)
     
    # Calculate area of triangle PAC
    A2 = area (x1, y1, x, y, x3, y3)
     
    # Calculate area of triangle PAB
    A3 = area (x1, y1, x2, y2, x, y)
     
    # Check if sum of A1, A2 and A3
    # is same as A
    if(A == A1 + A2 + A3):
        return True
    else:
        return False

def findPmax(s1p1,s1p2,s1):
    max = findNorm(s1p1,s1p2,s1[0])
    maxIndex = 0
    for x in range(len(s1)):
        temp = findNorm(s1p1,s1p2,s1[x])
        if (temp>max):
            max = temp
            maxIndex = x
    # print("temp: ", temp, maxIndex, max)
    return s1[maxIndex]
  
def findPmax2(s1p1,s1p2,s2):
    max = findNorm(s1p1,s1p2,s2[0])
    maxIndex = 0
    for x in range(len(s2)):
        temp = findNorm(s1p1,s1p2,s2[x])
        print("temp:",temp,s2[x])
        if (temp>max):
            max = temp
            maxIndex = x
    # print("temp: ", temp, maxIndex, max)
    return s2[maxIndex]
        
for x in range(len(s1)):
    print(findNorm(s1p1,s1pn,s1[x]), s1[x])
print("-----------")
for x in range(len(s2)):
    print(findNorm(s1p1,s1pn,s2[x]), s2[x])
    
print("max s1p1 s1pn:", findPmax(s1p1,s1pn,s1))
print("max s2p2 s2pn:", findPmax(s1p1,s1pn,s2))

# determinan positif ada di sebelah kiri
s11 = []
s12 = []
temp = []
s21 = []
s22 = []

def findLeftRightTri(p1,pn,pmax,s11,s12,s1):
  printPosNeg(s1,s11,temp,p1,pmax)
  # s11 terisi elemen bagian kiri dari segitiga
  
  printPosNeg(s1,temp,s12,pn,pmax)
  # s12 terisi elemen bagian kanan dari segitiga
  
  # print("s11:",s11,"\ns12",s12)
  
def findLeftRightTri2(p1,pn,pmax,s21,s22,s2):
  printPosNeg(s2,s21,temp,pmax,p1)
  # s11 terisi elemen bagian kiri dari segitiga
  
  printPosNeg(s2,temp,s22,pmax,pn)
  # s12 terisi elemen bagian kanan dari segitiga
  
  # print("s11:",s11,"\ns12",s12)
# findLeftRightTri(p1,pn,findPmax(s1p1,s1pn,s1),s11,s12,s1)
curPmax2 = findPmax(s1p1,s1pn,s2) # [4.5 2.3]

# findLeftRightTri2(p1,pn,findPmax(s1p1,s1pn,s2),s21,s22,s2)
print("s21:")
printList(s21)
print("s22:")
printList(s22)

curPmax = findPmax(s1p1,s1pn,s1)


s111 = []

# nextPmax = findPmax(s1p1,curPmax,s11)
# nextPmax2 = findPmax(curPmax2,s1pn,s2)
# nextPmax3 = findPmax(s1pn,curPmax2,s12)
# print("nextPmax1:",nextPmax)
# print("nextPmax2:",nextPmax2)
# print("nextPmax3:",nextPmax3)

def ifAlready(elmt, list):
  found = False
  for i in range(len(list)):
    v = np.array(elmt) == np.array(list[i])
    if (v.all()):
      found = True
  return found

def remove_duplicate(list):
  new = []
  for elmt in list:
    if not(ifAlready(elmt,new)):
      new.append(elmt)
      # print("append")
  return new

def addConvexLeft(sn,chlist,p1,pn):
  s11 = [] # diisi elemen kiri
  s12 = [] # diisi elemen kanan
  if (len(sn)==0):
    # if ifAlready(p1,chlist):
      chlist.append(p1)
    # if ifAlready(p1,chlist):
      chlist.append(pn)
  else:
    pmax = findPmax(p1,pn,sn)
    print("pmax1:",pmax)
        
    findLeftRightTri(p1,pn,pmax,s11,s12,sn)
    s11delpos = []
    s12delpos = []
    print("s11:")
    print(s11)
    print("s12:")
    print(s12)
    s21delpos = []
    s22delpos = []
    
    if len(s11) != 0:
      for i in range(len(s11)):
        if isInside(p1[0],p1[1],pn[0],pn[1],pmax[0],pmax[1],s11[i][0],s11[i][1]):
          print(p1[0],p1[1],pn[0],pn[1],pmax[0],pmax[1],s11[i][0],s11[i][1])
          s11delpos.append(i)
    # print("delete pos",i)
    if (len(s11delpos)!=0):
      print("s11delpos:")
      printList(s11delpos)
      print("s11")
      printList(s11)
      
      for i in range(len(s11delpos)):
        s11.pop(s11delpos[len(s11delpos)-i-1])
        print("deleted")
      printList(s11)
    
    if len(s12) != 0:
      for i in range(len(s12)):
        if isInside(p1[0],p1[1],pn[0],pn[1],pmax[0],pmax[1],s12[i][0],s12[i][1]):
          print(p1[0],p1[1],pn[0],pn[1],pmax[0],pmax[1],s12[i][0],s12[i][1])
          s12delpos.append(i)
          # s12 = np.delete(s12,i)
          # print("delete")
    if (len(s12delpos)!=0):
      print("s12delpos:")
      printList(s12delpos)
      print("s12")
      print(len(s12))
      for i in range(len(s12delpos)):
        s12.pop(s12delpos[len(s12delpos)-i-1])
        print("deleted")
      print(len(s12))
    
    
    addConvexLeft(s11,chlist,p1,pmax)
    addConvexLeft(s12,chlist,pmax,pn)
  print("chlist kiri")
  printList(remove_duplicate(chlist))
    
    # if len(s11) != 0:
    #   print("pmax:",s11)
    #   print("pmax:",s11[0])
    #   print("pmax:",s11[0][0],s11[0][1])
    
  # xl = []
  # yl = []
  # for i in range(len(chlist)):
  #   xl.append(chlist[i][0])
  #   yl.append(chlist[i][1])
  # plt.scatter(xl,yl)
  # plt.show()
  
def addConvexRight(sn,chlist,p1,pn):
  s21 = [] # diisi elemen kiri
  s22 = [] # diisi elemen kanan
  if (len(sn)==0):
    # if ifAlready(p1,chlist):
      chlist.append(p1)
    # if ifAlready(p1,chlist):
      chlist.append(pn)
  else:
    pmax = findPmax2(p1,pn,sn)
    print("pmax2:",pmax)
        
    findLeftRightTri2(p1,pn,pmax,s21,s22,sn)
    print("s21:")
    print(s21)
    print("s22:")
    print(s22)
    s21delpos = []
    s22delpos = []
    
    if len(s21) != 0:
      for i in range(len(s21)):
        if isInside(p1[0],p1[1],pn[0],pn[1],pmax[0],pmax[1],s21[i][0],s21[i][1]):
          print(p1[0],p1[1],pn[0],pn[1],pmax[0],pmax[1],s21[i][0],s21[i][1])
          s21delpos.append(i)
    # print("delete pos",i)
    if (len(s21delpos)!=0):
      # print("s211delpos:")
      # printList(s21delpos)
      # print("s21")
      # printList(s21)
      
      for i in range(len(s21delpos)):
        s21.pop(s21delpos[len(s21delpos)-i-1])
        print("deleted")
      printList(s21)
    
    if len(s22) != 0:
      for i in range(len(s22)):
        if isInside(p1[0],p1[1],pn[0],pn[1],pmax[0],pmax[1],s22[i][0],s22[i][1]):
          print(p1[0],p1[1],pn[0],pn[1],pmax[0],pmax[1],s22[i][0],s22[i][1])
          s22delpos.append(i)
          # s12 = np.delete(s12,i)
          # print("delete")
    if (len(s22delpos)!=0):
      # print("s12delpos:")
      # printList(s22delpos)
      # print("s22")
      # print(len(s22))
      for i in range(len(s22delpos)):
        s22.pop(s22delpos[len(s22delpos)-i-1])
        print("deleted",)
      print(len(s22))
    
    
    addConvexRight(s21,chlist,p1,pmax)
    addConvexRight(s22,chlist,pmax,pn)
  print("chlist kanan")
  printList(remove_duplicate(chlist))
  
  

def findConvex(bucketInput):
  # convexHull = np.array([1,2,3])
  # print("empty:",convexHull.size)
  
  s = bucketInput
  # bagi s menjadi dua bagian
  s1 = []
  s2 = []
  p1 = find_p1(s)
  pn = find_pn(s)
  printPosNeg(s,s1,s2,p1,pn)
  # s1 dan s2 terbagi setelah printPosNeg
  # print(s1, s2)
  
  convexList = []
  addConvexLeft(s1,convexList,p1,pn)
  addConvexRight(s2,convexList,p1,pn)
  # printList(convexList)
  return convexList
  # print(remove_duplicate(convexList))
  

print("--------------------")

convexList = findConvex(bucketInput) 

# printList(convexList)
# if((convexList[1]==convexList[2]).all()):
#   print("true")
# print(convexList[0]==convexList[2])
# print(convexList[3]==convexList[4])
outputList = remove_duplicate(convexList) 
# printList()
print("end")

# to do
# yang di dalam segitiga gaperlu dikonsider
# x1 = 4.3
# y1 = 3.0
# x2 = 5.8
# y2 = 4.0
# x3 = 4.5
# y3 = 2.3
# x = 4.4
# y = 2.9
# print(isInside(x1,y1,x2,y2,x3,y3,x,y))
############################################
# printList(verticesOutput)
print("====")
printList(outputList)
xl = []
yl = []
for i in range(len(outputList)):
  xl.append(outputList[i][0])
  yl.append(outputList[i][1])
plt.scatter(xl,yl)
plt.show()