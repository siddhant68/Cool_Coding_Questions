step = 0
infected, normal = input().split('#')
l = [int(x) for x in normal.split()]
l.append(int(infected))
l.sort()

index = l.index(int(infected))

for i in range(index):
    l[index] += l[i]

temp = l[index]
l.sort()
index = l.index(temp)
print(l)

while index != (len(l)-1) :
    if l[index+1] < (2 * l[index] - 1):
        step += 1
        l[index] = 2 * l[index] - 1
        
        temp = l[index]
        j = index
        
        while j+1 < len(l) and l[j+1] < temp:
            temp += l[j+1]
            l[j] = l[j+1]
            j += 1
            
        l[j] = temp
        index = l.index(temp)
        print(l)
        
        
    elif l[index+1] >= (2 * l[index] - 1):
        step += len(l) - 1 - index 
        print('here', l, step)
        break

print(step)        