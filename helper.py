import numpy as np
from numpy import linalg as LA

def findDet(p1, pn, arrayDet):
# Mengembalikan determinan dari tiga titik (p1, pn, arrayDet)
  x1 = p1[0]
  y1 = p1[1]
  x2 = pn[0]
  y2 = pn[1]
  x3 = arrayDet[0]
  y3 = arrayDet[1]
  a = np.array([[x1,y1,1], [x2,y2,1], [x3,y3,1]]) 
  return (np.linalg.det(a))

 
def area(x1, y1, x2, y2, x3, y3):
# Mengembalikan area segitiga dari (x1,y1), (x2,y2), (x3,y3)
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0)
 
def isInside(x1, y1, x2, y2, x3, y3, x, y):
# Mengecek apakah p(x,y) terdapat di dalam segitiga A(x1,y1), B(x2,y2), dan C(x3,y3)

    # Menghitung area segitiga ABC
    A = area (x1, y1, x2, y2, x3, y3)
    # Menghitung area segitiga PBC
    A1 = area (x, y, x2, y2, x3, y3)
    # Menghitung area segitiga PAC
    A2 = area (x1, y1, x, y, x3, y3)
    # Menghitung area segitiga PAB
    A3 = area (x1, y1, x2, y2, x, y)
    
    # Mengecek apakah A = hasil penjumlahan A1 + A2 + A3
    if(A == A1 + A2 + A3):
        return True
    else:
        return False
    
def printList(list):
# Mencetak setiap elemen list ke layar
    for x in list:
        print(x)

def findNorm(p1,p2,p3):
# Mengembalikan nilai norma pada vektor
    return (LA.norm(np.cross(p2-p1, p1-p3))/LA.norm(p2-p1))

def ifAlready(elmt, list):
# Mengembalikan nilai True jika elmt sudah ada di list
  found = False
  for i in range(len(list)):
    v = np.array(elmt) == np.array(list[i])
    if (v.all()):
      found = True
  return found

def remove_duplicate(list):
# Menghapus elemen duplikat di list
  new = []
  for elmt in list:
    if not(ifAlready(elmt,new)):
      new.append(elmt)
      # print("append")
  list = new