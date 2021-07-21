import time
LEN = 1000001
prime = [True for i in range(LEN)]
start = time.time()

for i in range(2,LEN):
    if prime[i] == False:
        continue
    for j in range(i+i,LEN,i):
        prime[j] = False



for i in range(2, LEN):
    if prime[i]:
        print(i, end= ' ')
print()
print("time :", time.time() - start)
