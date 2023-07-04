
my_name = "Muhammet Melih Tumur"
my_id = "200102002036"
my_email = "m.tumur2020@gtu.edu.tr"

#Ask for a Fahrenheit degree from the user, then convert to Celsius
#and return the result as a float.

def problem1():
    fah=float(input("Enter a Fahrenheit degree:"))
    cel=float((fah-32)*(5/9))
    return cel


#Ask for a Celsius degree from the user, then convert to Fahrenheit and return the result as a float.   
def problem2():
    cel=float(input("Enter a Celcius degree:"))
    fah=float(cel*(9/5)+32)
    return fah

#Ask for a number from the user. Calculate and return the hexagonal number that corresponds to
#that number. As an example, first 7 hexagonal numbers are: 1, 6, 15, 28, 45, 66, 91
def problem3():
    number=int(input("Enter a number:"))
    hexa=((2*number*number)-number)
    return hexa

#Ask for a number from the user. Calculate and return the lucas number that corresponds to that
#number starting with index 0. As an example, first 7 Lucas numbers are: 2, 1, 3, 4, 7, 11, 18

def problem4():
    def lucas(n):       
        if n==0: return 2
        elif n==1: return 1
        else : return lucas(n-1)+lucas(n-2)
    n=int(input("Enter a number :"))
    return lucas(n)

#Ask for an input string from the user and return the reverse of it.
        
def problem5():
    giris=input("Enter a string :")
    return giris[::-1]           

#Ask for an input string from the user and return the string with only letters and numbers in the entered order
def problem6():
    giris=input("Enter a string :")
    unwanted=("!",'"',"#","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","\\","]","^","_","`","{","|","}","~") 
    
    for i in giris :
        if i in unwanted :
            giris=giris.replace(i,"")
            
    
    return giris


#Ask for an integer from the user, then return the base 4 representation of that number as a string.
def problem7():
    giris=int(input("Enter input :"))
    cikis=""
    
    if giris < 0:
        #cikis = "-" + cikis 
        while giris !=0:              
              giris=abs(giris)
              cikis += str(giris%4)
              giris = giris//4
        return "-" + cikis[::-1]      
    else:
         while giris !=0:
              cikis += str(giris%4)
              giris = giris//4
         return cikis[::-1]
    

#Ask for an input from the user containing only parentheses. Then return if the parentheses are
#actually in correct order (or it is valid).

def problem8():
    
    controlDict = {"[":"]" ,"(":")" ,"{":"}"  } 
    giris=input("Enter input :")
    forControl = []

    def keyCheck(val):
        for key, value in controlDict.items():
            if val == value:
                return key
        

    def control(giris):
        for i in giris :
            if i in list(controlDict.keys()):
                forControl.append(i)
            elif i in list(controlDict.values()):
                if (len(forControl)>0) and ( keyCheck(i) == (forControl[len(forControl)-1])) :
                    forControl.pop()
            else :
                return "Unbalanced1"
    control(giris)
    if len(forControl)==0 :
        return "Balanced"
    else :
        return "Unbalanced2" 
    
# function to return key for any value
 
    
        

print(problem8())

#Ask for a string input from the user, then find the length of the last word in the string. Return the length.

def problem9():
    giris=input("Enter a string :")
    giris_ters= giris[::-1] 
    sayi=0
    for i in giris_ters :
        sayi += 1
        if i == " " :
            sayi=sayi-1
            break 
    return sayi

#Assume that you are in a maze, and you are given a set of commands describing how to exit from
#the maze using east, west, north, and south commands each denoted with first letters (e, w, n, s).
#Assuming you start at the origin of the x-y coordinate system (0, 0), calculate the length of the
#straight line connecting your starting point and where you arrived in the coordinate plane.[3]

def problem10():
    giris=input("Enter the exit route :")
    
    e=0
    w=0
    n=0
    s=0
    
    for i in giris : 
        if i=="s":
            s -=1
        if i =="w":
            w -=1
        if i =="n":
            n +=1
        if i =="e":
            e+=1

    y=abs(s+n)
    x=abs(e+w)
    
    hipo_kare=(x**2 + y**2)
    
    low = 0
    high = hipo_kare
    eps = 1E-4
    
    counter = 0
    while True:
        counter += 1
        guess = (high + low) / 2
        if abs(guess*guess -hipo_kare) < eps:
      
            break
        if guess*guess >hipo_kare :
            high = guess
        else:
            low = guess
    return guess


























