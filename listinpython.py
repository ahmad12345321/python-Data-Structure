data=["Muhammad Ahmad Raza",20,45,67,8,8,"Muhammad Anas Raza"]
print(data)
#***********    add data in list     ***********
data.append("ali")
data.append("saeed")
print(data)
#***********    delete data in list     ***********
data.pop(6)
print(data)
#***********     update data in list     ***********
data[4]="Habib"
print(data)
#***********     print data in list     ***********
# simple print  list
print(data)
# we print any element of list for example
print(data[4])
print(data[6])
print(data[2])
# indexing in list
# data.index(8)
# print(data)

for i in data:
     print(i)
# show list length using len() function
length=len(data)
print(length)
# maximum function in list
maximum=[1,2,3,4,5,6,7,8,9]
maximum=max(maximum)
print(maximum)
maximumstring=['rana',"ahmad",'raza',"anas"]
maximumstring=max(maximumstring)
print(maximumstring)
# minimum function in list
minimum=[1,2,3,4,5,6,7,8,9]
minimum=min(minimum)
print(minimum)
minumummumstring=['rana',"ahmad",'raza',"anas"]
minumummumstring=min(minumummumstring)
print(minumummumstring)
# insert in list
data.insert(1,"hussnain")
print(data)
data.remove(5)
print(data)
