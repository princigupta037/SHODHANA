# Armstrong Numbers

num = int(input("Enter a number: "))
# initialize sum
sum = 0
# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   print(digit)
   sum += digit ** 3
   print(sum)
   temp //= 10
   print(temp)
# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
   