# hognose

A fully ai driven programming language that sometimes produces working code

requires python3 (tested with version 3.11) and the openai pip package.

# Getting started

Clone the repo install the required packages with:

```
pip install -r requirements.txt
```

then write some hognose code or try one of the examples!

to compile hognose code into real code simply run

```
hognose/main.py [code.hogn] [output.py] [openai api key]
```

# Language features

Hognose is a fully feature complete programming laguage that can do anything python can! this is because it compiles directly to python using AI.
(Disclaimer: hognose won't be able to do anything remotely useful in practice. But in theory it could.)

# Syntax

## Hognose operator

The most basic operator in Hognose is the Hognose operator. it lookes like this: ||^/ because I thought it kind of looked like a hognose snake.
I also based all other operators on this design even though they don't end up looking like snakes. This is because I am an idiot.

to use the hognose operator simply start a line with it and then follow it with a description of the code you want to be written
```
||^/ output "hello world" to the console

might compile to:

print("hello world")
```
## Variables

Hognose allows you to create variables which can be reused between different prompts. This could allow Hognose to generate larger and more coherant code than would otherwise be possible.
It doesn't. But it could.

Variables are declared with a name and a description. Unlike normal languages you may have worked with before Hognose does not allow you to instantiate variables with a value.
This is because the Hognosonic way to write code is by providing a description that will allow hognose to generate a sensible value for your variable.
```
<||variablename/ a description of your variable

for example:

<||username/ the name of the user

might compile to:

name = "John Doe"  # Replace this with the actual user's name
username = name.lower().replace(" ", "_")
```

Variables can be referenced at any point when writing hognose code using the sytax: ||variablename/
This can be helpful as it lets hognose know that a variable already exists and it shouldn't create a new value for it.
```
<||username/ the name of the user

||^/ take a user input and save the value to ||username/

might compile to:

username = "john_doe"  # Replace with the user's name or a sensible value
username = input()
```

Hognose variables cannot contain numbers or special characters.

## Functions

Attempting to use functions in Hognose is not a good idea and will not result in functional (pun not intended) code. That said no Hognose code is functional so it doesn't really matter.

Functions are defined similarly to variables with a name and a description but with <!!func/. Similarly to variables hognose will generate all the function logic from the description.
```
<!!functionname/ description of the function

<!!coinflip/ return a random value of either true or false

might compile to:

import random

def coinflip():
    return random.choice([True, False])
```

With functions there is also the option to define inputs. This is done by including <var|desc> in the function declaration.
```
<!!functionname<var|description><var2|description2>/ description of the function

<!!iseven<num|number to check is even>/ return true is num is even

might compile to:

def iseven(num):
    return num % 2 == 0
```

Like variables functions can be referenced in other code using !!func/

```
<!!diceroll/ return a random number between 1 and 6

||^/ call !!diceroll/ twice and add the results and print the result to the console

might compile to:

import random

def diceroll():
    return random.randint(1, 6)
result = diceroll() + diceroll()
print(result)
```

## Static values

Sometime you might want Hognose to be extra sure that you are giving it a value and not something else. It doesn't seem to help in my experience but it might help you!
To do this simply wrap your value as ;;val/

```
<!!isprime<num|number to test if its prime>/ return true if the number is prime

||^/ run !!isprime/ on all values between ;;1/ and ;;100/ count how many results are true and output that

might compile to:

def isprime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):

        if num % i == 0:
            return False
    return True
count = sum(1 for num in range(1, 101) if isprime(num))
print(count)
```

## multiline

By default all Hognose instructions must be on the same line. To get around this simply end a line with && and it will continue on to the next line
```
||^/ write some code here &&
then keep writing it here

||^/ output the name of &&
a random species of snake

might compile to:

import random

# List of snake species
snake_species = [
    "Burmese Python",
    "King Cobra",
    "Black Mamba",
    "Garter Snake",
    "Corn Snake",
    "Rattlesnake",
    "Green Anaconda",
    "Eastern Diamondback Rattlesnake",
    "Cottonmouth",
    "Boa Constrictor"
]

# Output a random species of snake
print(random.choice(snake_species))
```

# Community

The hognose community is an active and thriving group of exactly 0 individuals. Even James Pursglove, creator of Hognose, has no intention of ever writing and real code with this language.

If you want to push that number from a 0 to a 1 I recommend seriously reconsidering your life decisions.

If you have any bug reports or feature requests email them to jamespursglove2@gmail.com
I won't fix anything but I might respond with a cool picture of a lizard.
