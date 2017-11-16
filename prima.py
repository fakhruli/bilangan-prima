import time
start_time = time.time()
a = int(input("Masukkan banyak bilangan prima: "))

b = 1
c = 1
ca = a
start = 2
while c <= ca:
    while(b<=a):
        d = 0
        for i in range(1,start+1):
            if (b%i) == 0 :
                d += 1
        start += 1
        if d == 2:
            print(c,")",b)
            c += 1
        else:
            a+=1
        b+=1

print("--- %s seconds ---" % (time.time() - start_time))
