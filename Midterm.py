import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    return round(math.pi * ((radius) ** 2), 2)

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
        result = ''
    
        if (n < 4):
            result = 'The triangle height should be at least 4.'
            
        elif (n >= 4):
            for i in range(n - 1):

                result += '*'

                if (i > 0):
                    for j in range(i - 1):
                        result += ' '
                     
                    result += '*'
                                
                result += '\n'
                
            result += ((n)  * '*')
        return result.rstrip()


# Q3: Inverted Pyramid
def inverted_pyramid(n):  
    result = ''


    if (n <= 2):
        result = 'The pyramid height should be at least 3.'


    if (n >= 3):
        for i in range(n):

            for j in range(i):
                result += ' '

            for k in range((n * 2) - (i * 2) + 1):
                result += '*'
                        
            result += '\n'
        
        result += ((n)  * ' ' + '*')
            
    return result.rstrip()


# ----------------------------------------------------------------
print(area_of_circle(5))
print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(3))
print()

print(inverted_pyramid(4))
print()

print(inverted_pyramid(5))
print()
