def check_prime(num):
    if num == 1 or num == 2:
        print("Number %d is prime" % num)
        return

    if num % 2 == 0:
        # print("Number %s is not prime." % num)
        return

    for i in range(3, num//2 + 1):
        if num % i == 0:
            # print("Number %d is not prime" % num)
            return
    print("%d " % num, end=" ")


for j in range(1, 100):
    check_prime(j)
