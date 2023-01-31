# Countdown 
newlist=[]
def countdown(a):
    for i in range(a+1):
        newlist.append(i)
    print (newlist)

countdown(3)

# Print and Return 
list=[]
def print_and_return(list):
    for i in range(len(list)):
        print(list[i])
        return(list[i+1])
list1=[1,2,3]
print_and_return(list1)

# First Plus Length 
list=[]
def First_Plus_Length(list):
        print(list[0]+len(list))
list1=[1,2,3]
First_Plus_Length(list1)
# Values Greater than Second
list=[]
listgreater=[]
def values_greater_than_second(list):
    for i in range(len(list)):
        if list[i]>list[1]:
            listgreater.append(list[i])
    print(listgreater)
values_greater_than_second([5,2,3,2,1,4])


# This Length, That Value 
newlist=[]
def length_and_value(size,value):
    for i in range(size):
        newlist.append(value)
    print(newlist)
length_and_value(2,3)

