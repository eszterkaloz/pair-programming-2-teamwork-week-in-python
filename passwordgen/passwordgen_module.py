# from random import randint
import random
import string


def passwordgen():
    # small_letter_size = random.randint(2, 5)
    # big_letter_size = random.randint(2, 5)
    # digit_letter_size = random.randint(2, 5)
    # char_letter_size = random.randint(2, 5)
    # size = small_letter + big_letter + char_letter + digit_letter
    #
    # digit_letter = random.choice(string.digits)
    # char_letter = random.choice(string.punctuation)

    # characters = random.choice(string.ascii_letters) + random.choice(string.digits) + random.choice(string.punctuation)
    # return ''.join(random.choice(characters) for x in range(size))

    size = random.randint(2, 5)
    pwd = ""
    for i in range(size):
        pwd = pwd + random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice("[!@#$%^&*()?]")
    return pwd


def main():
    pwd = passwordgen()
    print(pwd)
    return


if __name__ == '__main__':
    main()
