def timeConversion(s):
    #
    # Write your code here.
    #
    ss=s[8]
    print(ss)
    if ss=="A" and not((s[0]+s[1])=="12"):
        return(s[0:8])
    elif ss=="A" and ((s[0:2])=="12"):
        return("00"+s[2:8])    
    elif ss=="P" and not((s[0]+s[1])=="12"):
        return(str((int(s[0:2]))+12)+s[2:8])
    elif ss=="P" and ((s[0]+s[1])=="12"):
        return("12"+s[2:8])        

print(timeConversion("12:05:39AM"))