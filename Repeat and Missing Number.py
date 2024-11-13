#https://takeuforward.org/data-structure/find-the-repeating-and-missing-numbers/

n=[3 ,1 ,2, 5, 3]
s=n[0]
for i in n[1:len(n)]:
    s=s^i
for i in set(n):
    s^=i
print(s)


b= (sum([i for i in range(len(n)+1)])  - sum(n) +s)
print(b)
