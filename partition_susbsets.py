l = [3, 1, 4, 2, 2, 1]

def partition_rec(l, i, totalSum, calculatedSum):
    if i < 0:
        return abs((totalSum-calculatedSum) - calculatedSum)
    
    return min(partition_rec(l, i-1, totalSum, calculatedSum),
               partition_rec(l, i-1, totalSum, calculatedSum+l[i])
               )

def partition(l):
    print(partition_rec(l, len(l)-1, sum(l), 0))

partition(l)
	
	
for _ in range(int(input())):
	s = input()
	l = []
	for i in range(len(s)):
		for j in range(i, len(s)):
			l.append(s[i: j+1])
	l.sort()
	for i in l:
		print(''.join(i))
	