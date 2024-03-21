def is_leap(year):
    leap = False
    
    if year % 4 == 0 :
       print ("True")
    elif year % 100 == 0 :
       print ("False")
    elif year % 400 == 0 :
       print ("True")
    else :
        print ("False")
    
    return leap

year = int(input())