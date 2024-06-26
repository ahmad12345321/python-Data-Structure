# #dictionary in python
student={'Name':'Muhammad Ahmad Raza',"rollno":47,"age":22,"fathername":"arifali"}


# print simple dictonary  data
print(student)



# # print simple dictonary  name
print(student["Name"])

# # print simple dictonary  age
print(student["age"])

# # print simple dictonary  father name
print(student["fathername"])

# # get values from dictonary into dictonary
print(student.values())

# # get keys from dictonary into dictonary
print(student.keys())

# # get items from dictonary into dictonary
print(student.items())

# # check item is available in list
print(student.get("email","not found try again"))
print(student.get("Name","not found"))

# # add element in dictionary python
student["email"]="abc@gmail.com"
print(student)

# # update element in python
student["Name"]="Muhammad Anas Raza"
print(student)
#
# # Delete element in python dictonary
print(student.pop("fathername"))
print(student)

print(student.pop("email"))
print(student)

# # print using for loop
for i in student:
    print(i)

# # print keys in dictionary using loops
for i in student.keys():
    print(i)
# #  using item function to get items from list
for i in student.items():
    print(i)
# # nessted dictonary
#
Schoolclass={
    1:{"Class":"1st","totalstudent":45,"total chair":55},
    2:{"Class":"2nd","totalstudent":43,"total chair":67},
    3:{"Class":"3ed","totalstudent":47,"total chair":66},
    4:{"Class":"4th","totalstudent":40,"total chair":69}

}
# print(Schoolclass)
# ## using loops to print the number
for i in Schoolclass.values():
    print(i)
print("thank you")
# #example no 1
#
student={"name":"Muhammad Ahmad Raza","Age":21,"designation":"student"}
user_key=input("enter the key")
if user_key in student.keys():
    print("key is available")
else:
    print("does not hava a key ")
#
#
# #example 2
#
salary1={"name":"Muhammad Ahmad Raza", "salary":55000}
salary2 = {"name": "Zahid Maqbool", "salary": 55000}

salary1.update(salary2)
print(salary1)

# #example 3
#
# # Multiply all the values in a dictionary
number={'a':1,'b':2,'c':3,'4':5}
num=int(input("enter your number"))
for i in number:
    num=num*number[i]
    print(num)



# #example 4
sums={'ahmad':55,'saad':55,'zahid':77,'anas':20,}
total=sum(sums.values())
print(total)



# #example 5 Convert two lists into a dictionary
list1=['a','b','c','d','e','f']
list2=['A','B','C','D','E','F']
merge=dict(zip(list1,list2))
print(merge)

