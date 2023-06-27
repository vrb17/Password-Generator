# Password generator
from random import randint

alpha_lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alpha_upper = [x.upper() for x in alpha_lower]
spec_chars = ['!','@','#','$','%','^','&','*']

len_pass = input('Enter the length of your desired password: ')
len_pass.strip()

length = int(len_pass)

i = 0
pass_list = []
while i < length:
    four = num = randint(1, 4)

    if four == 1:
        num = randint(0, 25)
        pass_list.append(alpha_lower[num])

    if four == 2:
        num = randint(0, 25)
        pass_list.append(alpha_upper[num])

    if four == 3:
        num = randint(0, 9)
        pass_list.append(num)

    if four == 4:
        num = randint(0, 7)
        pass_list.append(spec_chars[num])

    i += 1
else:
    print("Your generated password is: ", end='')
    for i in pass_list:
        print(i, end='')






