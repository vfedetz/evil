import random
import string

names = [line.rstrip('\n') for line in open('first_names.txt')]
f = open('csc_creds.txt', 'w')


count = 0
while (count < 1000):
    email = random.choice(names) + '.' + random.choice(names) + '@cscglobal.com'
    password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(12))
    f.write(email + ' ' + password + '\n')
    count += 1
    