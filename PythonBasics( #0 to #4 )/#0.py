
my_name = "Muhammet Melih Tumur"
my_id = "200102002036"
my_email = "m.tumur2020@gtu.edu.tr"

# Return the first letter on your name as a string.

def problem1():
    return my_name[0]


# Ask for a number from the user to define an index, then return the letter in your name that
#corresponds to that index starting from 0 (for input n → return nth index).

def problem2():
    sayi=int(input("Enter a number:"))
    if sayi >(len(my_name)-1) :
        return my_name[sayi%(len(my_name)-1) -1]
    elif sayi<0:
        return my_name[sayi%(len(my_name)-1) ]        
    else:
        return my_name[sayi]
    
#Ask two numbers from the user to define indexes, then find the substring of your my_name
#variable taking these two index values as beginning and end. Return this substring.

def problem3():
    sayi1=int(input("Enter first number:"))
    if sayi1<0:
       sayi1=sayi1%(len(my_name)-1)
    if sayi1>(len(my_name)-1) :
       sayi1=sayi1-len(my_name)
         
    sayi2=int(input("Enter second number:"))
    if sayi2<0:
       sayi2=sayi2%(len(my_name)-1)
    if sayi2>(len(my_name)-1) :
      sayi2=sayi2-len(my_name)

    if sayi1<sayi2:   
        return my_name[sayi1:sayi2]
    if sayi2<sayi1:
        return my_name[sayi2:sayi1]

#Ask for a string from the user, then count the number of vowels in the input and return the result.

def problem4():
    vowels=('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    giris=input("Enter input:")
    sesli=0
    for i in giris:
        if i in vowels :
            sesli += 1
    return(sesli)

    
#Sum up all the digits on your id number and return the result.

def problem5():
    x=0
    print
    for i in my_id:
        i=int(i)
        x += i
    return x

#Ask for a number from the user, then calculate and return the factorial of that number.

def problem6():
    sayi=int(input("Enter input :"))
    factoriel=1
    if sayi==0 :
        return 1
    else :
        for i in range(2,sayi+1):
            factoriel *= i
        return factoriel
    

#Ask for a number from the user. If that number is divisible to both 3 and 7 return True, else return False.

def problem7():
    sayi1=int(input("Enter a number:"))
    if sayi1%3 ==0 and sayi1%7 == 0 :
        a=True
    else : 
        a=False
    return a


#Ask for a number from the user.
#1. If that number is only divisible to 3, return 1,
#2. if that number is only divisible to 7, return 2,
#3. if that number is divisible to both 3 and 7, return 3        

def problem8():
    sayi1=int(input("Enter a number:"))
    if sayi1%3 ==0 and sayi1%7 !=0:
        return 1
    elif sayi1%7 ==0 and sayi1%3 !=0:
        return 2
    elif sayi1%3 ==0 and sayi1%7 ==0:  
        return 3
    
#Ask for a number from the user, then find if that number is a prime number.If the number is a prime number, return True, else return False
def problem9():
    sayi=int(input("Enter a number :"))
    a=True
    for i in range(2,sayi):
        if (sayi%i)==0 :
            a=False
            return a
                
    return a

    
    
    
    
    
    
    