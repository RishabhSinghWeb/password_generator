import random
#import string
#characters = string.ascii_letters + string.punctuation  + string.digits
#for i in range(32,127):
#	print('\'',chr(i),'\',',end='',sep='')

list = [' ','!','"','#','$','%','&','\'','(',')','*','+',',','-','.','/','0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','[','\\',']','^','_','`','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','{','|','}','~']
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~0123456789'

for _ in range(40000):
    print(random.choice(list),
    	list[random.randint(0,len(list)-1)],
    	random.SystemRandom().choice(characters),
    	random.choice(characters),
    	sep='', end='')
