from stringprep import in_table_c11_c12


data = list(input())

print(data)
data.sort()

print(data)
for i in range(len(data)-1):
    tmp = 0
    res = 0
    if data[i] == data[i+1]:
        tmp += 1
        for j in range(i+1,len(data)):
            if data[i] == data[j]:
                tmp +=1
        if tmp == res:
            print("?")
            break 
        if tmp>res:
            res = tmp
            i_res = i    


print(data[i_res])