import random


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = []
b = []

length_a = random.randint(5, 50)
length_b = random.randint(5, 50)

# for i in range(length_a):
#     a.append(random.randint(1, 15))
# for i in range(length_b):
#     b.append(random.randint(1, 15))

a = [random.randint(1, 15) for i in range(length_a)]
b = [random.randint(1, 15) for i in range(length_b)]

print(a)
print(b)


def listoverlap(list1, list2):
    set_1 = set(list1)
    set_2 = set(list2)
    union = set_1 & set_2
    return list(union)


def main():
    unio = listoverlap(a, b)
    print(unio)
    return


if __name__ == '__main__':
    main()
