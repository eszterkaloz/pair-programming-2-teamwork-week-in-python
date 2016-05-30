def palindrome(sentence):
    word_list = sentence.split(" ")
    one_piece = ""
    for i in range(len(word_list)):
        one_piece += word_list[i]
    lower_one_piece = one_piece.lower()
    same = 1
    for i in range(len(lower_one_piece)):
        same *= (lower_one_piece[0+i] == lower_one_piece[-1-i])
    return same


def main():
    sent = input("Enter a sentence to test if it is a palindrome: ")
    result = palindrome(sent)
    if result:
        print('Your sentence is a palindrome.')
    else:
        print("Your sentence is not palindrome.")
    return


if __name__ == '__main__':
    main()
