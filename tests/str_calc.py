def add(numbers):
    
    negative_num = False
    numStr = numbers
    
    numStrTemp = numStr.replace("\n",",").replace(";",",").replace("//",",").replace("\\","").replace("n","")
    
    var = numStrTemp.split(",")
    
    sum =0
    
    for i in var:
        if(i != ""):
            if(int(i) < 0):
                negative_num = True
            else:
                sum += int(i)
                
    if(negative_num == True):
        raise Exception('Negatives not allowed')
    else:
        print(sum)

    return sum