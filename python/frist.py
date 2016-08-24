import math
what_he_does = 'plays '
his_instrument = 'guitar '
his_name = 'Robert Johnson '
artist_intro = his_name + what_he_does +his_instrument
print (artist_intro)

num=1
string ='1'
num2 =int(string)
print(num+num2)

word='word '*3
print(word)

phone_number= '1386-660-006'
hiding_number= phone_number.replace(phone_number[:9],'*'*9)
print(hiding_number)

print('{} a word she can get what she {} for'.format('with','came'))

city = input('city??')
url="http://apistore.baidu.com/microservice/weather?citypinyin={}".format(city)

def C2F(c):
    F = c * 9/5 +32
    return str(F)+'F'# F是int 格式， 不能和string 相加故， str
print(C2F(36))

def g2kg(g):
    kg = g / 1000
    return kg
print(str(g2kg(25))+'kg')

def triangle(length,wideth):
    triangle = length**2 + wideth** 2
    return  math.sqrt(triangle)
result = triangle(3,4)
print('The right triangle third side\'s length is {}'.format(result))

file=open('H:/Desktop/text.txt','w')
file.write('Hello world!!!')

file_account = 0
while file_account<10:
    file_account= file_account+1
    file_account_s =str(file_account)
    file_path = 'H:/Desktop/1/'
    full_path = file_path + file_account_s +'.txt'
    file = open(full_path ,'w')
    file.write('HELLO,WORLD')
    file.close()
#=====================复利===========================================
def invest(amout,rate,time):
   print('principal amout:{}'.format(amout))
   for t in range(1,time+1):
       amout = amout * (1+rate)
       print('year'+str(time)+':'+'$'+str(amout))
invest(100,0.05,8)

#===================100以内整数============================
for i in range(1,101):
    if i%2 ==0:
        print (i)
#=====================猜大小=============================
import random
print('<<<<<<<<<< GAME STARTS! >>>>>>>>>>')
input_result= input('Big or Small:')
input_result= str(input_result)
print('<<<<<<<<<< ROLE THE DICE! >>>>>>>>>>')
point1 = random.randrange(1,7)
point2 = random.randrange(1,7)
point3 = random.randrange(1,7)
point= point1+point2+point3
def big_or_small():
    if 11<=point<=18:
        return ("Big")
    else:
        return ("Small")
result= big_or_small()
if result == input_result:
    result = 'Win!'
else:
    result = 'Lose!'
print('The points are ['+str(point1)+','+str(point2)+','+str(point3)+'] You {}'.format(result))

#=======================赌博=========================
def roll_dice(number=3,point=None):
    print('<<<<<<<<<< ROLE THE DICE! >>>>>>>>>>')
    if point is None:
        point = []
    while number>0:
        points= random.randrange(1,7)
        point.append(points)
        number=number-1
    return point
def roll_result(total):
    isBig= 11<=total <= 18
    isSmall = 3<= total <=10
    if isBig:
        return 'Big'
    elif isSmall:
        return 'Small'


def start_game():
    print('<<<<<<<<<< GAME STARTS! >>>>>>>>>>')
    choice=['big','small']
    input_result = input('big or small:')
    mymoney= 1000
    money = input('How much you wanna bet? -')
    money= int(money)
    mymoney=mymoney -money
    if mymoney<0:
        print('no money,try again')
    if input_result in choice:
        point =roll_dice()
        total = sum(point)
        YouWin = input_result ==roll_result(total)
        if YouWin:
            print('The points are ',point,'YOU WIN!!!')
            mymoney= mymoney +(2*money)
            print('You gained {},you have {} now'.format(money,mymoney))
        else:
            print('The points are ',point,'YOU Lose!!!')
            print('You lost {},you have {} now'.format(money,mymoney))
    else:
        print('Invalid Words')
        start_game()
start_game()

#===================手机号适配=================================================
def match_telephone():
    CN_mobile = [134,135,136,137,138,150,151,152,157,158,159,182,183,184,187,188,147,178,1705]
    CN_union =[130,131,132,155,156,185,186,145,176,1709]
    CN_telecom =[133,153,180,181,189,177,1700]
    telephoneNumber = input('Enter your number:')
    if len(telephoneNumber) != 11:
        print('Invaild length, your number should be in 11 digits')
    telephoneNumber = int(telephoneNumber[0:3])
    if telephoneNumber  in CN_mobile:
        print('Operator: CN_mobile ')
        print('We\'re sending verification code via text to your phone: {} '.format(telephoneNumber))
    elif telephoneNumber in CN_union:
        print('Operator: CN_union ')
        print('We\'re sending verification code via text to your phone: {} '.format(telephoneNumber))
    elif telephoneNumber in CN_telecom:
        print('Operator: CN_telecom ')
        print('We\'re sending verification code via text to your phone: {} '.format(telephoneNumber))
    else:
        print('NO such a operator')
match_telephone()

#============================词频统计
def word_count():
    path ='D:/PycharmProjects/untitled/Week one/Walden.txt'
    with open(path,'r') as text:
        words= text.read().split()
        for word in words:
            print('{}-{}times'.format(word,words.count(word)))

word_count()