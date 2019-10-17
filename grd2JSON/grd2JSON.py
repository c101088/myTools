import json

def ugrd2JSON(srcFile,fileType):
    data = {}
    with open(srcFile) as file1:
        counter=0
        tempdata= []
        for line in file1:
            counter=counter+1
            if counter ==1 :
                tempStrArr=line.split()
                data.update({"datasrc":tempStrArr[0]})
            elif counter==2:
                tempStrArr=line.split()
                data.update({"numWidth":tempStrArr[0],"numHeight":tempStrArr[1]})
            elif counter==3:
                tempStrArr = line.split()
                data.update({"startLNG":tempStrArr[0],"endLNG":tempStrArr[1]})
            elif counter==4:
                tempStrArr = line.split()
                data.update({"startLAT":tempStrArr[0],"endLAT":tempStrArr[1]})
            elif counter==5:
                tempStrArr = line.split()
                data.update({"minValue":tempStrArr[0],"maxValue":tempStrArr[1]})
            else :    
                tempStrArr=line.split()
                tempdata.extend(tempStrArr)
            data.update({"data":tempdata})
    if fileType==0:
        with open("grd2JSON/data/v.json","w") as file2:
            json.dump(data,file2)
    else:
        with open("grd2JSON/data/u.json","w") as file2:
            json.dump(data,file2)

ugrd2JSON("grd2JSON/data/U.grd",1)
ugrd2JSON("grd2JSON/data/V.grd",0)
