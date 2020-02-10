v1 = 'first string'
v2 = 'second string'

v1 = v2 ## v1 = second string
v2 = v1 ## v2 = second string
    
    ## In line 4 variable v2 ='second string' was reassigned 
     # to v1 so when variable v2 pulls from v1 in line 5 
     # it returns the new assigned variable.


str1 = 'first string'
str2 = 'second string'
temp = str1 ##Placeholder to keep the variable str1 as its first variable.
            #definition

str1 = print(str2) ## str1 = 'second string'
str2 = print(temp) ## str2 = str1 | str1 = 'first string'