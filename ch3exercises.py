#Chapter 3 Exercises

#Exercises Pg 36

def print_right(text, spaces = 40):
    spaces -= len (text)
    ws = ""
    while spaces > 0:
        ws += ' '
        spaces -= 1
    print(ws + text)

print_right('Monty')
print_right("Python's")
print_right("Flying Circus")

#Exercise top of pg 37

def triangle(letter, steps):
    for i in range(steps):
        print(letter*(i+1))
triangle('L', 5)

#Exercise middle of pg 37

def rectangle(another_letter, height, width):
    for j in range(height):
        for i in range(width):
            print(another_letter, end='')
        print()

rectangle('H', 5, 4)

#Exercise bottom of pg 37

def bottle_verse(n):
    if n == 0:
        print('No more bottles of beer on the wall')
        return
    print(f"""{n} bottle{' ' if n == 1 else 's'} of beer on the wall
    {n} bottle{' ' if n == 1 else 's'} of beer""")
    print(f"""Take one down, pass it around 
    {n-1} bottle{' ' if n == 1 else 's'} of beer on the wall""")

def bottle_song(n):
    for n in range(n, -1, -1):
        bottle_verse(n)
        print()

bottle_song(99)