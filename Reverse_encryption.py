while True:
    message = input('Enter text to encrypt: ')
    i = len(message) - 1
    translate = ''
    while i > 0:
        translate = translate + message[i]
        i = i - 1
    print('The encrypted text is: ', translate)
