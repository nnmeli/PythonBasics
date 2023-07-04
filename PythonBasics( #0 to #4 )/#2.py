my_name = "Muhammet Melih Tumur"
my_id = "200102002036"
my_email = "m.tumur2020@gtu.edu.tr"


#Your function should have a parameter that will hold a string. This string will be the cards from a
#deck of cards. Return True if there is a King in the cards, False if not.

def problem1(a):
    x = False
    for i in a:
        if i == "K":
            x=True
        else:
            None
    return x

#Write a function that expects four parameters as numbers, and returns the minimum of these numbers.

def problem2(a, b, c, d):
    numbers = [a, b, c, d]
    numbers.sort()
    return numbers[0]

#Write a function that expects two parameters as numbers, rounds the first number according to the
#second number and returns the result.

def problem3(f, g):
     if type(f) == float :  
        if ( f < g ) :
            f += 1
        elif (g<f):
            None
     else :
         return f
     return int(f)

#Write a function that will calculate and return the volume of a cylinder.

def problem4(radius, height, pi=3.1415):
    return radius*radius*height*pi


#Volume of a cylinder with error check
def problem5(radius, height, pi=3.1415):

    if isinstance(radius, (int, float)) and isinstance(height, (int, float)) and isinstance(pi, (int, float)):
        return radius*radius*height*pi

    else:
        return -1


#Write a function that will find and return the only character that does not have a duplicate in a
#given string. The returned character needs to be a string.

def problem6(x):

    for i in x:
        if x.count(i) == 1:
            return i

#Write a program that will find and return if the characters are in ascending order. (abcde...z).

def problem7(x):
    if list(x) == sorted(x):
        return True
    else:
        return False

#Write a program that will find if the characters in a string are all unique. Meaning, there are no
#duplicate characters.
def problem8(x):

    if len(list(x)) == len(list(set(x))):
        return True
    else:
        return False

#Write a program that will find and return the number with the given row (i-th) and column (j-th)
#index using the following rules.

def problem9(row, column):

    if row == 1 and column == 1:
        return 1
    elif row > 1 and column == 1:
        return 3
    elif row > 1 and column == row:
        return 2
    else:
        return problem9(row-1, column-1) + problem9(row-1, column)

#Write a program that takes two parameters as strings and returns the number of characters that
#appear in the same index.

def problem10(x, y):
    if len(x)>len(y):
        a = y
    elif len(y)>len(x):
        a=x
    else :
        a=x
    
    
    s = 0
    for i in range(len(a)):
        if x[i] == y[i]:
            s += 1

    return s
