def main():
    a = True
    while a:
        print('Menu\n-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print()
        x = input('Please enter an option: ')
        if int(x) == 1:
            password = input('Please enter your password to encode: ')
            print('Your password has been encoded and stored!')
            encoded = encode(password)
            print()
        elif int(x) == 2:
            pass
        elif int(x) == 3:
            a = False


def encode(password):
    word = ""
    for char in str(password):
        word += str((int(char)+3)%10)
    return int(word)

if __name__ == '__main__':
    main()