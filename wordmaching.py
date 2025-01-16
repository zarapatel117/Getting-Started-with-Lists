def matchingword(words):
    crt=0
    lst=[]
    for word in words:
        if len(word) >1 and word[0]==word[-1]:
            crt+=1
            lst.append (word)
    print("the list af the words which first and last letter are same",lst) 
    return crt
count=matchingword (['122','asa','1221','1321','555'])
print("the words which first and last letter are same",count)
 
    
