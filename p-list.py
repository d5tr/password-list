print('''
      __________      
  ____/ / ____/ /______
 / __  /___ \/ __/ ___/
/ /_/ /___/ / /_/ /    
\__,_/_____/\__/_/  
    # Thank you for use my tool #
       insta = d_5tr
''')
from itertools import product
import string

print('''
[1]all Codes
[2]Letter only 
[3]Letter and numbers
''')  #قائمه الاختيار 
wwe = int(input('enter number :'))  #اختيار الرقم 

if wwe == 1:   #اذا كان 1 هو رقم الاختيار 
    min_len = int(input('enter minimum of password : '))  #اقل عدد من طول اللسته 
    max_len = int(input('enter maximum length of password : '))  #اكثر عدد من اللسته 
    counter = 0  #حسابه عدد الطول اللسته (ف الاخير )
    char = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation  #نوع الرموز ف اللسته 

    file_open = open(input('enter file name to save :'), 'w')  #صناعه ملف 

    for i in range(min_len,max_len):   #اخذ الارقام الموجوده 
        for j in product(char,repeat=i):   #كتابه اللسته 
            word = "".join(j)  #وضع اللسته 
            file_open.write(word)  #طباعه اللسته 
            file_open.write('\n')  #كتابه اللسته 
            counter+=1  #حساب عدد اللسته 

    print("done --->{} passwords list".format(counter)) #طباعه النهايه 
    #d5tr -- 01
elif wwe == 2 :
      min_len = int(input('enter minimum of password : '))
    max_len = int(input('enter maximum length of password : '))
    counter = 0
    char = string.ascii_lowercase+string.ascii_uppercase  #+string.digits+string.punctuation

    file_open = open(input('enter file name to save :'), 'w')

    for i in range(min_len,max_len):
        for j in product(char,repeat=i):
            word = "".join(j)
            file_open.write(word)
            file_open.write('\n')
            counter+=1

    print("done --->{} passwords list".format(counter))

elif wwe == 3 :
      min_len = int(input('enter minimum of password : '))
    max_len = int(input('enter maximum length of password : '))
    counter = 0
    char = string.ascii_lowercase+string.ascii_uppercase+string.digits  #+string.punctuation

    file_open = open(input('enter file name to save :'), 'w')

    for i in range(min_len,max_len):
        for j in product(char,repeat=i):
            word = "".join(j)
            file_open.write(word)
            file_open.write('\n')
            counter+=1

    print("done --->{} passwords list".format(counter))

else :
    exit
    print('number not found !!')



