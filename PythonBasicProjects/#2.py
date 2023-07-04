"""

Project 2 - Image Transformation

In this project, you are asked to
implement functions that will enable
you to apply image transformation
techniques on a given image.
The objective of this project is to
learn about representation of colors, data structures, practice
basic mathematical operations on custom data structures, and
create fundamental knowledge about basics of the image
processing techniques.


Some RGB color examples:
1. Blue = [ 0, 0, 255]
2. Green = [ 0, 255, 0]
3. Red = [ 255, 0, 0]
4. White = [ 255, 255, 255]
5. Black = [ 0, 0, 0]
6. Gray = [ 95, 95, 95]

"""

my_name = "Muhammet Melih Tumur"
my_id = "200102002036"
my_email = "m.tumur2020@gtu.edu.tr"

import random


def generate_random(row,column):
    
    gecici_dict={"red": 0 , "green":0 , "blue": 0}  
    cikti=[]
    
    for i in range(row):
       gonderici=[]
       cikti.append(gonderici)
       for i in range(column):
           gecici_dict["red"]=random.randint(0, 255)
           gecici_dict["green"]=random.randint(0, 255)
           gecici_dict["blue"]=random.randint(0, 255)
           gonderici.append(gecici_dict.copy())
          
       
    return cikti


def is_valid(img):
  for i in img:
    for k in i :
      if k["red"] < 0 or k["red"]>255 or type(k["red"])!= int:
        return False
      if k["green"] < 0 or k["green"]>255 or type(k["green"])!= int:
        return False
      if k["blue"] < 0 or k["blue"]>255 or type(k["blue"])!= int:
        return False
    return True 

def clear(img):
  for i in img:
    for k in i :
       k["red"]=0       
       k["green"]=0        
       k["blue"]=0
  



def set_value(img,value,channel="rgb"):
  
  def changer(a):
    if a=="r" :
      for i in img:
        for k in i :
           k["red"]=value
    if a=="g" :
      for i in img:
        for k in i :
           k["green"]=value
    if a=="b" :
      for i in img:
        for k in i :
           k["blue"]=value
  for i in channel :
    changer(i)
         

def fix(img):
  for i in img:
    for k in i :
      if k["red"] < 0 : k["red"] = 0
      if k["red"]>255 : k["red"]=255
      if type(k["red"])!= int: k["red"]= round(k["red"])

      if k["green"] < 0 : k["green"] = 0
      if k["green"]>255 : k["green"]=255
      if type(k["green"])!= int: k["green"]= round(k["green"])

      if k["blue"] < 0 : k["blue"] = 0
      if k["blue"]>255 : k["blue"]=255
      if type(k["blue"])!= int: k["blue"]= round(k["blue"])


def rotate90(img):
  img2=img.copy()
  img2[:]=(list(zip(*img2[:])))
    
  for i in range(len(img2)) :        
      img2[i]=list(img2[i][::-1])
  return img2
        
def rotate180(img):
  img2=img.copy()
  for i in range(2): 
    
    img2[:]=(list(zip(*img2[:])))
      
    for i in range(len(img2)) :        
        img2[i]=list(img2[i][::-1])
  
  return img2

def rotate270(img):
  img2=img.copy()
  for i in range(3): 
    
    img2[:]=(list(zip(*img2[:])))
      
    for i in range(len(img2)) :        
        img2[i]=list(img2[i][::-1])
  return img2

def mirror_x(img):
  for i in img:
    i[:] = reversed(i[:])
  
def mirror_y(img):
  img[:]=reversed(img[:])
             
  

def enhance(img , value , channel="rgb"):
  def changer(a):
    if a=="r" :
      for i in img:
        for k in i :
           k["red"]=k["red"]*value
    if a=="g" :
      for i in img:
        for k in i :
           k["green"]=k["green"]*value
    if a=="b" :
      for i in img:
        for k in i :
           k["blue"]=k["blue"]*value
  for i in channel :
    changer(i)
  fix (img)

"""
def grayscale(img, mode=1):
  if mode == 1 :
    for k in img :
      for i in k:
        
        a=(i["red"]+i["blue"]+i["green"])/3
        i["red"]=a        
        i["green"]=a
        i["blue"]=a
  
  if mode == 2 :
    for i in img :
      a=(i["red"]*0.299 +i["blue"]*0.114 +i["green"]*0.587)
  
      i["red"]=a
      i["blue"]=a
      i["green"]=a
  if mode == 3 :
    for i in img :
      a=(i["red"]*0.2126 +i["blue"]*0.0722 +i["green"]*0.7152)
  
      i["red"]=a
      i["blue"]=a
      i["green"]=a
  if mode == 4 :
    for i in img :
      a=(i["red"]*0.2627 +i["blue"]*0.0593 +i["green"]*0.6780)
  
      i["red"]=a
      i["blue"]=a
      i["green"]=a
  fix(img)

"""

         
