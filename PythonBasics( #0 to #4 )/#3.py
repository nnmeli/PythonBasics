my_name = "Muhammet Melih Tumur"
my_id = "200102002036"
my_email = "m.tumur2020@gtu.edu.tr"

#Write a function that takes two arguments; a list and an integer called n. Return the list of numbers that repeats n times. 

def problem1(x ,y):
  a=[]
  for i in x : 
    if x.count(i)==y:
        a.append(i) 
  return list(set(a))
      

#Write a function that takes one argument: a dictionary. It will have the name, grade pair for the INF211 class. Find and return the 
#median grade of the class. 

def problem2(x):
    a=x.values()
    a = sorted(list(a))
    if len(a)%2==1 :
        ortanca = a[int(((len(a)+1)/2)) -1]
        return ortanca
    
    if len(a)%2==0 :
        ortanca_1 = a[int(len(a)/2)-1]
        ortanca_2 = a[int(len(a)/2)]
        return (ortanca_1+ortanca_2)/2
    

#Write a function that takes a filename as parameter. File will have a list of courses with the credits 
#, given term and the scores. You need to read this file, create a dictionary for each course and add 
#it to a list. Finally return this list. Example file is given with the assignment.

def problem3():
    b= r"C:\Users\Melih\Desktop\inf\PyhtonLabs&Projects\transcript1.txt" 
    dosya = open(b,"r")
    
    sonuc =[]
    liste = dosya.read()
    a = liste.rsplit("\n")
    b=[]
    for i in range(len(a)-1) :
        b.append(a[i].rsplit(","))
    
    for i in b :
        notlar = {'name' : "", 'credit' : 0, 'term' : 0, 'grade' : ''}
        notlar["name"] = i[0]
        notlar["credit"] = i[1]
        notlar["term"] = i[2]
        notlar["grade"] = i[3]
        sonuc.append(notlar)
    
    return(sonuc)    
  
#Write a function that takes two parameters: a list that holds the transcript as dictionary items. You need to calculate the GPA.       

def problem4(a,b):
        grades = {"AA":4.0, "BA":3.5,  "BB":3.0,"CB":2.5,"CC":2.0,"DC":1.5,   "DD":1.0,"FF":00}     
        gpa=0
        bolu=0
        for i in a :
         	gpa += i["credit"]*grades[i["grade"]]
         	bolu += i["credit"]
        return gpa/bolu

  

#Write a function that takes two parameters: a function, and a number. This function's definition is given below, and the function 
#may or may not work as expected. Your function should figure out if the given function is working or not working as expected. 
#Return True if the function works correctly, False otherwise.
        
def problem5(x , y):       
    def f(x):
        a=[]
        b=""
        c=0
        for i in range(0,x+1):
            if str(1) in str(i) :
                a.append(i)
        for i in a :
            b +=str(i)
        for i in b :
            if i =="1":
                c+=1
        return c
    if x(y)==f(y):
        return True
    else :
        return False    

#Write a program that accepts a string and returns all possible combinations of the given strings.        
def problem6(s):
    results = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i, len(s)):
            results.add(s[i:j+1])
    return sorted(list(results))

          

 

#Write a function that will take two parameters, both are list of lists representing a matrix. The 
#function should find and return True if the second matrix is a sub-matrix of the first one. If it is not a 
#sub-matrix, return False.
    
def problem8(x,y):
    yan_sublar=[]
    dik_sublar=[]
    for i in x :
        a=[]
        for k in i :
            a.append(k)
            yan_sublar.append(a.copy())
    c=0
    b=[]
    while c<len(x[0]) : 
        b=[]
        for i in x:
            b.append(i[c])
            dik_sublar.append(b.copy())
        c+=1    
            
    tum_sublar=yan_sublar + dik_sublar   
    
    for i in range(len(y)):
        if y[i] not in tum_sublar :
            return False
    return True
                                                                                
                                                                                             
#Our engineers developed a novel compression algorithm that they claim will save a lot of space when saving text files. In this 
#algorithm, if a letter is consequently repeated more than 1 time, instead of writing the letter multiple times, a number is appended 
#to denote how many times the preceding letter is repeated. Write a program that compresses the given string, and returns the 
#compressed version as a string and the compression rate as a percentage rounded to an integer      

def problem9(x):
    a=""
    
    for i in x :
        if i not in a :
            a+=i
            y=x.count(i)
            if y != 1 :
                a+=str(y)
    b=round(len(a)*100/len(x))
    
    return a , 100-b    


#Write a function that will find the missing number in a given list of numbers. The numbers in the list are consecutive but might not 
#be sorted. If no number is missing, return the next number. 
def problem10(x):
    x=list(sorted(x))
    a=[]
    for i in range(x[0],x[len(x)-1]+1):
        a.append(i)
    
    for i in range(0,len(x)):
        if x[i]!=a[i]:
            return a[i]
    return x[len(x)-1]+1




    



  
    