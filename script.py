#This script will filter out the noise generated from 6 pairs of keys#

#copy and paste keys and caste them to arrays
num1 = input("number1:")
array1 = list(map(str, num1))
num2 = input("number2:")
array2 = list(map(str, num2))
num3 = input("number3:")
array3 = list(map(str, num3))
num4 = input("number4:")
array4 = list(map(str, num4))
num5 = input("number5:")
array5 = list(map(str, num5))
num6 = input("number6:")
array6 = list(map(str, num6))
#compare the numbers and output the keys.
for i in range(len(array1)):
    if array1[i] == array2[i] and array1[i] == array3[i] and array1[i] == array4[i] and array1[i] == array5[i] and array1[i] == array6[i]:
        print(array1[i], end="")

