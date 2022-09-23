first = [1, 4, 8, 100, 101, 120]
second = [2, 3, 7, 10, 12]
merge = []

l_first = len(first)
l_second = len(second)

i = j = 0

while i < (l_first-1) and j < (l_second-1):
    if first[i] < second[j]:
        merge.append(first[i])
        i += 1
    else:
        merge.append(second[j])
        j += 1
    
while i < l_first-1:
    merge.append(first[i])
    i += 1
    
while j < l_second-1:
    merge.append(second[i])
    j += 1

print(merge)
