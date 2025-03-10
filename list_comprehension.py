list1=[1,2,3,4,5,6,7,8,9,10]
new_list = []

for i in range (1,11):
    if i%2 == 0:
        new_list.append("even")
    
    else:
        new_list.append("odd")


print(new_list)

new_list = [i for i in range(1,11) if i%2==0]
print(new_list)

new_list = ["even" if i%2==0 else "odd" for i in range (1,11)  ]