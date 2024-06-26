#dictionary in python
student={'Name':'Muhammad Ahmad Raza',"rollno":47,"age":22,"fathername":"arifali"}


# print simple dictonary  data
print(student)



# print simple dictonary  name
print(student["Name"])

# print simple dictonary  age
print(student["age"])

# print simple dictonary  father name
print(student["fathername"])

# get values from dictonary into dictonary
print(student.values())

# get keys from dictonary into dictonary
print(student.keys())

# get items from dictonary into dictonary
print(student.items())

# check item is available in list
print(student.get("email","not found try again"))
print(student.get("Name","not found"))

# add element in dictionary python
student["email"]="abc@gmail.com"
print(student)

# update element in python
student["Name"]="Muhammad Anas Raza"
print(student)

# Delete element in python dictonary
print(student.pop("fathername"))
print(student)

print(student.pop("email"))
print(student)

# print using for loop
for i in student:
    print(i)

# print keys in dictionary using loops
for i in student.keys():
    print(i)
#  using item function to get items from list
for i in student.items():
    print(i)
# nessted dictonary

Schoolclass={
    1:{"Class":"1st","totalstudent":45,"total chair":55},
    2:{"Class":"2nd","totalstudent":43,"total chair":67},
    3:{"Class":"3ed","totalstudent":47,"total chair":66},
    4:{"Class":"4th","totalstudent":40,"total chair":69}

}
# print(Schoolclass)
## using loops to print the number
for i in Schoolclass.values():
    print(i)
print("thank you")
