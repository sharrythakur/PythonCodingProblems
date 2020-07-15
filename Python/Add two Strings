
num1 = "1457853368567"
num2 = "9346745467"

# appending 0s in the beginning of the shorter string
if len(num1) > len(num2):
    num2 = "0" * (len(num1) - len(num2)) + num2
else:
    num1 = "0" * (len(num2) - len(num1)) + num1

# zipping both the strings and converting each digit to integer type using map
zipped = list(map(lambda x: (int(x[0]), int(x[1])), zip(num1,num2)))


summ = []
carry = 0
for x,y in zipped[::-1]:
    s = x + y + carry
    carry = s//10   # updating carry 
    summ.append(s%10) # appending the sum of two digits in summ list

summ.append(carry) if carry != 0 else summ # if there is any carry in the end we need to append at last

print("".join(map(str,summ[::-1]))) # reversing the list to get the sum

