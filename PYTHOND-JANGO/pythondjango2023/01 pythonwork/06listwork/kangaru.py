text1 = "chicken"
text2 = "henz"
srt1 = sorted(text1)
srt2 = sorted(text2)
flag=1
if len(srt1)<len (srt2) :
    sml_wrd =srt1 
    big_wrd= srt2

else:
    sm1_wrd = srt2
big_wrd= srt1
for i in range (0,len(sml_wrd)) : 
    if sml_wrd[i] in big_wrd:
        flag*=1 
    else:
        flag*=0
if flag==1:
    print ("Kangaroo word.")
else:
    print("Not Kangaroo word.")