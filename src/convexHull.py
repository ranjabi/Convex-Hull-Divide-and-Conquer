import math
from helper import *

def findP1(array):
# Mengembalikan point dengan x terletak di koordinat paling kiri
  min = array[0]
  for i in range(len(array)):
    if (array[i][0]<=min[0]):
      min = array[i]
  return min

def findPn(array):
# Mengembalikan point dengan x terletak di koordinat paling kanan
  max = array[0]
  for i in range(len(array)):
    if (array[i][0] >= max[0]):
      max = array[i]
  return max

def cekPosNeg(bucketone, s1, s2, p1, pn):
# Menambahkan point list ke s1 jika determinan > 0, menambahkan ke s2 jika determinan < 0
  for i in range(len(bucketone)):
    det = findDet(p1, pn, bucketone[i])
    if (det>(0)):
      s1.append(bucketone[i])
    elif (det<0):
      s2.append(bucketone[i])

def findPmax(s1p1,s1p2,s1):
# Mengembalikan nilai Pmax dari p1 dan p2 pada s1
# Berlaku juga untuk s2
  max = findNorm(s1p1,s1p2,s1[0])
  maxIndex = 0
  for x in range(len(s1)):
      temp = findNorm(s1p1,s1p2,s1[x])
      if (temp>max):
          max = temp
          maxIndex = x
  # print("temp: ", temp, maxIndex, max)
  return s1[maxIndex]

def findLeftRightTriS1(p1,pn,pmax,s11,s12,s1):
# Menyimpan elemen s1 bagian kiri dan kanan dari segitiga (p1,pn,pmax) ke dalam s11 dan s12
  temp=[]
  cekPosNeg(s1,s11,temp,p1,pmax)
  cekPosNeg(s1,temp,s12,pn,pmax)
  
def findLeftRightTriS2(p1,pn,pmax,s21,s22,s2):
# Menyimpan elemen s2 bagian kiri dan kanan dari segitiga (p1,pn,pmax) ke dalam s21 dan s22
  temp=[]
  cekPosNeg(s2,s21,temp,pmax,p1)
  cekPosNeg(s2,temp,s22,pmax,pn)
  
def deletePointTriangle(s11,s12,p1,pn,pmax):
# Menghapus titik pada s11 yang terdapat di dalam segitiga (p1,pn,pmax)
# Berlaku juga untuk s21 dan s22 pada s2
  s11delpos = []
  s12delpos = []
  
  if len(s11) != 0:
    for i in range(len(s11)):
      if isInside(p1[0],p1[1],pn[0],pn[1],pmax[0],pmax[1],s11[i][0],s11[i][1]):
        s11delpos.append(i)
  if (len(s11delpos)!=0):
    for i in range(len(s11delpos)):
      s11.pop(s11delpos[len(s11delpos)-i-1])
  
  if len(s12) != 0:
    for i in range(len(s12)):
      if isInside(p1[0],p1[1],pn[0],pn[1],pmax[0],pmax[1],s12[i][0],s12[i][1]):
        s12delpos.append(i)
  if (len(s12delpos)!=0):
    for i in range(len(s12delpos)):
      s12.pop(s12delpos[len(s12delpos)-i-1])

def addConvexLeft(sn,chlist,p1,pn):
# Menambahkan convex list bagian kiri ke s11 dan bagian kanan ke s12
  s11 = []
  s12 = []
  if (len(sn)==0):
      chlist.append(p1)
      chlist.append(pn)
  else:
    pmax = findPmax(p1,pn,sn)
    
    findLeftRightTriS1(p1,pn,pmax,s11,s12,sn)
    deletePointTriangle(s11,s12,p1,pn,pmax)
    
    addConvexLeft(s11,chlist,p1,pmax)
    addConvexLeft(s12,chlist,pmax,pn)
  
def addConvexRight(sn,chlist,p1,pn):
# Menambahkan convex list bagian kiri ke s21 dan bagian kanan ke s22
  s21 = []
  s22 = []
  if (len(sn)==0):
      chlist.append(p1)
      chlist.append(pn)
  else:
    pmax = findPmax(p1,pn,sn)
        
    findLeftRightTriS2(p1,pn,pmax,s21,s22,sn)
    deletePointTriangle(s21,s22,p1,pn,pmax)
    
    addConvexRight(s21,chlist,p1,pmax)
    addConvexRight(s22,chlist,pmax,pn)
  
  
def findConvex(listInput):
# Mengembalikan convex hull dari listInput
  s = listInput
  
  # bagi s menjadi dua bagian
  s1 = []
  s2 = []
  
  # cari p1 dan pn
  p1 = findP1(s)
  pn = findPn(s)
  
  # isi elemen s1 dan s2
  cekPosNeg(s,s1,s2,p1,pn)
  
  convexList = []
  
  # cari convex hull pada s1 dan s2
  addConvexLeft(s1,convexList,p1,pn)
  addConvexRight(s2,convexList,p1,pn)
  # printList(convexList)
  
  # hapus elemen duplikat dan sort berlawanan arah jarum jam
  remove_duplicate(convexList)
  convexList = sort_counterclockwise(convexList)
  convexList.append(convexList[0])
  
  return convexList
  
def sort_counterclockwise(points):
# Mengurutkan elemen ada points berlawanan arah jarum jam dengan menghitung theta dari koordinat polar

  # Mencari titik tengah dari points dengan menghitung mean
  center_x, center_y = sum([x for x,_ in points])/len(points), sum([y for _,y in points])/len(points)
  
  # Menghitung theta
  angles = [math.atan2(y - center_y, x - center_x) for x,y in points]
  
  # Urutkan berdasarkan theta
  counterclockwise_temp = sorted(range(len(points)), key=lambda i: angles[i])
  counterclockwise_points = [points[i] for i in counterclockwise_temp]
  
  return counterclockwise_points