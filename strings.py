# make a string in python
name="Ahmad Raza"
print(name)
# find a legnth of name
length=len(name)
print(length)
# itreating in string using loops
# we print simple character for strings
for i in name:
    print(i)
# print name for 1,19 using range
for i in range(1,19):
    print(name)
# foward indexing in string
for i in range(0,4):
    print(name[i])
# backword indexing in string
for j in range(-4,-1):
    print(name[j])
# silicing in string
# print(name[-3,-1])
# print(name[0:3])
print(name[-5:-2])
print(name[0:-3])
print(name[-2:0])
# methods in string
# for upper case
upper=name.upper()
print(upper)
# for lower case
lower=name.lower()
print(lower)
# for length
length=len(name)
print(length)

lstrip=name.lstrip()
print(lstrip)

# for replace string we use replace in python

replace=name.replace("Raza","Ahmad     ")
print(replace)

split=name.split()
print(split)

captlize=name.capitalize()
print(captlize)
# count word in string
count=name.count("Ahmad")
print(count)
# we check lines end with character using endswith

endswith=name.endswith("!!!")
print(endswith)

# find is use to find any word in string

find=name.find("Ahmad")
print(find)



