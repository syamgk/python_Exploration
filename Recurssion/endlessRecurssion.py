def recursive(string, num):
     global s,n
     s,n = string,num
     print (string, num)
     global i
     i += 1
     try:
        recursive(string, num+1)
     except:
        rec2(string,num+1)
        print "count:",i
def rec2(s,n):
     recursive(s,n)
i = 0
s,n = (0,0)
recursive("string",0)
