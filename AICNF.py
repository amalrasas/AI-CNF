from collections import Counter
def resolution(clause):
    #chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    canBeEntailed=False;
    isEmpty=False
    frequency = Counter(clause)
    #print("Count Occurrences of Each Character :")
    for (key, value) in frequency.items():
        x=value
        if x>1:
            y=y="not("+key+")"
            contains=False
            if y in clause and key in clause:
                str1=clause.replace(y,"")
                newclause=str1.replace(key,"")
                clause=newclause
                isEmpty=checkIfEmpty(newclause)
                

    if(isEmpty==True):
        canBeEntailed=True;
    return canBeEntailed     
                 
def checkIfEmpty(clause):
    isEmpty=False
    for i in clause:
        str1=i.replace("(","")
        str2=str1.replace(")","")
        str3=str2.replace("and","")
        str4=str3.replace("or","")
        str5=str4.replace("not","")
        str6=str5.replace(" ","") 
        clause=str6
        
    if not clause:#if string is empty 
        isEmpty=True 
    return isEmpty    

kb=[]
query=[]
toggledquery=[]
kbandtoggledquery=[]
fixedbool=[]
file=input("Please enter file name")
count = len(open(file).readlines(  ))
counter=0
f=open(file,"r")
for i in f:
    #print(i)
    
    if counter<count and counter%2==0:
        kb.append(i)
        print("KB: ",i)
        counter=counter+1
    elif counter<count and counter%2!=0:
        query.append(i)    
        print("query: ",i)
        counter=counter+1
f.close()  
for i in query:
    l =i
    if i[0]=="~":
        i=l[1:]
        toggle=" ("
        x=toggle+i+")"
        toggledquery.append(x)
  
    else:
        toggle=" ~("
        x=toggle+i+")"
        toggledquery.append(x)
#print(toggledquery)
newtoggledquery=[]        
for i in toggledquery:
    #newtoggledquery.append(i)
    i=i.replace(" ","")
    i=i.replace("\n","")
    size=len(i)  
    if size==4:
        newtoggledquery.append(i)     
    elif i[0]=="~" and size>4:
        i=i.replace("^","v")
        i=i.replace("v~(","^~(")
        x="v"
        y=i.find(x) #index of v
        newstr=" ^ "+i[ : y]+")"+i[y]+" ~("+i[y+1: ]
        #print(newstr)
        newtoggledquery.append(newstr)
        #newstr=newstr.replace(""," ")
        #newtoggledquery.append(newstr)
        #print(newstr)
#print(newtoggledquery)        

for i in range(len(kb)):
    str1=kb[i]
    str2=newtoggledquery[i]
    str3=str1+str2 
    kbandtoggledquery.append(str3)
#print(kbandtoggledquery) 
for i in kbandtoggledquery:
    text0=i.replace("v","or")
    text1=text0.replace("^","and")
    text2=text1.replace("~","not ")
    text3=text2.replace("\n","")
    #text4=text3.replace("(","")
    #text5=text4.replace(")","")
    fixedbool.append(text3)  
#print(fixedbool)
cenBeEntailed=False  
for i in range (len(fixedbool)):
    z=fixedbool[i].replace(" ","")
    canBeEntailed=resolution(z)
    if canBeEntailed==True:
        print("Yes,",query[i]," can be entailed")
    else:
        print("No,",query[i]," can't be entailed")
        
