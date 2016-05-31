# from random import randint
import random
import string


def passwordgen():
    size = random.randint(8, 15)
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for x in range(size))


def main():
    pwd = passwordgen()
    print(pwd)
    return


if __name__ == '__main__':
    main()
