l=[10,19,100,29,17,8,15,50,75,25]
l.sort()
k=int(input("Enter k for kth largest number:").strip())
print(l)
print(l[len(l)-(k)])
