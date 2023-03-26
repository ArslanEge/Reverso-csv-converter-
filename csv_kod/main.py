import csv 
count=0
mylist=[]
with open ('file.csv') as german:
    file=csv.reader(german,delimiter=',')
    next(file)
    for row in file:
        mylist.append(row)
        
    
    i=0
    for big in mylist:

        for row in big:
            if "<em>" in row:
                break
            else:
                count+=1

        big[count]=big[count].replace("<em>",'')
        big[count]=big[count].replace("</em>",'')
        count=0

    for big in mylist:
        big=big.pop(4)

        

    for big in mylist:

        for row in big:
            if "<em>" in row:
                break
            else:
                count+=1

        big[count]=big[count].replace("<em>",'')
        big[count]=big[count].replace("</em>",'')
        count=0
    
   


with open("final.csv","w") as f:

    thewriter=csv.writer(f)
    
    for big in mylist:
         thewriter.writerow(big)



        
        
                  
    
    
    
    

           
        
           
        

   

