#number Pallindrome
num = 12321
rev = 0
while(num):
    rev = rev * 10 + num%10
    num = num//10  #1232

print(rev)

#String Pallindrome
str = "malayalam"
rev = ""
for i in range(len(str)-1, -1, -1):
    rev = rev + str[i]

print(rev==str)
