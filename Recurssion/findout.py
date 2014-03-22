def recursive(string, num):
# function calling itself  
     print (string, num)
     global i
     i += 1
     try:
        recursive(string, num+1)
     except:
        print "count stops at:",i
i = 0
recursive("counting:",0)
