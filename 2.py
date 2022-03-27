#Write a Python program to get the volume of a sphere with radius 6

from math import pi
r = 6
volume = pi*(r*r)
print("The volume is: ")
print(volume)

#Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

i = 5 #float(input("Escreva um número: "))
if i > 17:
    print(2*(i - 17))
else:
    print(i - 17)

#Write a Python program to test whether a number is within 100 of 1000 or 2000

i = 1234 #float(input("Escreva um número: "))

if i in range (1000,2000):
    print(True)
else:
    print(False)

#Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum

a = 4 #float(input("escreve um numero: "))
b = 4 #float(input("escreve um numero: "))
c = 4 #float(input("escreve um numero: "))
soma = (a + b + c)

if a == b == c:
    print(3* soma)
else:
    print(soma)

#Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.

strin = 'meurabo' #input("Escreva uma palavra: ")
new_string = "Is" + strin

if strin[0] == "I" and strin[1] == "s":
    print(strin)
else:
    print(new_string)

#Write a Python program to get a string which is n (non-negative integer) copies of a given string.

n = int(float(3.14))#input("Escreva um número positivo: ")))
st = 'amanda' #input('Escreva um nome qualquer: ')

if n > 0:
    print(st*n)
else:
    print("Número inválido.")

#Write a Python program to count the number 4 in a given list.

a = [1,2,3,4,5,6,7,3,4]

if 4 in a:
    print(a.count(4))
else:
    print("Não tem '4' nessa lista.")

# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
# #Return the n copies of the whole string if the length is less than 2.

a = 'abububle' #input("Escreva qualquer merda: ")
b = 3 #int(float(input("Escreva qualquer número: ")))
c = a[0:2]

if b >= 2:
    print(c*b)
else:
    print(a*b)

#Write a Python program to test whether a passed letter is a vowel or not.

vogais = ['a', 'e', 'i', 'o', 'u']
l = "a" #input("escreva qualquer letra, porra: ")

if l in vogais:
    print('A letra é uma VOGAL')
else:
    print('A letra é uma CONSOANTE')

#Write a Python program to check whether a specified value is contained in a group of values

a = 2 #float(input('escreva qualquer porra de número: '))
listinha = [0, 1, 2, 3, 5, 6, 84, 22]

if a not in listinha:
    print(False)
else:
    print(True)

#Write a Python program to display your details like name, age, address in three different lines.

a = (['name: ', 'amanda' ], ['age: ', '29'], ['cidade: ', 'são josé dos pinhais'])

for (x,y) in a:
    print(y)

#Write a Python program to solve (x + y) * (x + y)

x = 3 #int(float(input("escolha um number: ")))
y = 4 #int(float(input("escolha um number: ")))
s = x + y
print(s**2)

#Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years

i =  int(float(input("Escreva seu valor inicial: ")))
j =  1 + ((float(input('taxa de juros anual: '))) / 100)
t =  int(float(input("Escreva o tempo em anos que o investimento permanecerá: ")))
f = i*(j**t)
print('Seu montante final será de:')
print(int(f))

lucro = f - int(i)

print("Seu lucro será de: ")
print(int(lucro))

print("Que equivale, por ano, a: ")
print((int(lucro))/t)

