# CS5 Gold, hw1pr1
# Filename: hw1pr1.py
# Name: Joseph Konieczny
# Problem description: First Python lab!

pi = [3,1,4,1,5,9]
e = [2,7,1]

# Example problem (problem 0):  [2,7,5,9]
answer0 = e[0:2] + pi[-2:]  
print(answer0)

# Problem 1: creating [7,1]
answer1 =   e[1:2] + pi[-3:-2]
print(answer1)

# Problem 2: creating [9,1,1]
answer2 =   pi[-1:] + e[-1:] + pi[-3:-2]
print(answer2)

# Problem 3: creating [1,4,1,5,9]
answer3 =   pi[-5:]
print(answer3)

# Problem 4: creating [1,2,3,4,5]
answer4 =   e[-1:] + e[-3:-2] + pi[0:1] + pi[2:3] + pi[-2:-1]
print(answer4)


# Lab1 string practice

h = 'harvey'
m = 'mudd'
c = 'college'

# Problem 5:  'hey'
answer5 = h[0] + h[4:6]
print(answer5)

# Problem 6: 'collude' Trump??
answer6 = c[0:4] + m[1:3] + h[-2:-1]
print(answer6)

# Problem 7: 'arveyudd'
answer7 = h[1:] + m[1:]
print(answer7)

# Problem 8: 'hardeharharhar'
answer8 = h[0:3] + m[-1] + c[-1] + h[0:3] + h[0:3] + h[0:3]
print(answer8) 

# Problem 9: 'legomyego' not eggo???
answer9 = c[-4:-1] + c[1] + m[0] + h[-1] + c[-3:-1] + c[1]
print(answer9)

# Problem 10: 'clearcall'
answer10 = c[0] + c[-4:-2] + h[1:3] + c[0] + h[1] + c[2:4]
print(answer10)