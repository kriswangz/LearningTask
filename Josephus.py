# The program is used for solving josephus promblem.
# character:
#           n: total numbers
#           k: step value
# description:
#           Counting from the first person, when count to the step value, he must commit suicide, 
#           and then report again from the next, until everyone suicide.

def josephus(n, k):
    if k == 1:
        print('survive:%d' % (n))
        return
# generate person list. [1,2...n]
    total = []
    for i in range(1, n+1):
        total.append(i)

    p = 0       # index point
    while True:
        if len(total) == 1:
            break
        p = (p + (k - 1)) % len(total)

        # step 1: p=1 kill total[1] = 2, total[] = [1,3,4,5,6]
        # step 2: p=2 kill total[2] = 3, total[] = [1,3,5,6]
        # step 3: p=3 kill total[3] = 4, total[] = [1,3,5]
        # step 4: p=4%3=1 kill total[1] = 3, total[] = [1,5]
        # step 5: p=2%2=0 kill total[0] = 1, total[] = [5]

        print ('kill:%d' % (total[p]))
        # list.pop can also be used for deleting items in list and return items
        del total[p]
    print ('survive:%d' % (total[0]))

josephus(6, 3)
############################
