# fundamental of python

## The first thing you have to know is 
### what is python?

Python is a high level language with his user friendly English like syntax 


Ok know let talk about python syntax 

## syntax 

The first thing you learn in python is the print statement

So if you want to print something to the screen you just say

```
Print("Hello world")
```

Out put.  `Hello world`


> [!remeber]
>  ***you can change the text `Hello world` to any thing you want*** 


So here we have our first code but wait a second what is this ok let me show you what it is 
 
There are three things you have to consider they are 

1. The `print` statement 
2. The brackets `( )` and
3. The cotes `" "` or `' '`

###### the `print` statement 

There is a `print` statement is predefined so you just have to write 
The `print` statement is say to compiler that the text inside needs to be displayed 
###### the brackets `( )` 

the brackets are next to the `print` statement 
In side the brackets is where the text you want to display goes to 

###### the cotes `" "` or `' '`

 and there is the cotes it can be ether the
- double Cote `" "` or  
- single cote `' '`
it is not a problem 

Inside the double cote or the single cote there goes the text you want to display on the screen every thing you write inside it is going to displayed on the screen

## variables 

Variables are some kind of magician they can store any thing 

Let's see how to store things in variables 

To store things inside variables we need a name for the variable 
Something like 
- pizza           
- you 
- hi
- what 
- ever
- you 
- want 
- x 
- y 
After that do this

```
Bro = 'hello world'
```

If do that you successfully created a variable called bro inside it is the `hello world` text

Then you can print it out like i show you before but this time without cotes 

```
Print(bro)
```

Output.  `hello world`

This is how store things in variable and print it to the screen 

But I said you can store any thing inside a variable so let me show you what can we store in variables 


|    *Type*     |   *Example*   |
| :-----------: | :-----------: |
|    Strings    | 'hello world' |
|    boolean    | True or False |
|    Float's    |     3.14      |
| Whole numbers |       7       |
- **strings** are any text inside a cote
	- example 
```
name = 'python'
```
- **Boolean** can be ether True or False
	- example 
```
Condition = True
```
- **Float** are any number with decimals point
	- example 
```
Pi = 3.14
```
- **Whole numbers** are any whole number 
	- example 
```
Age = 27
```

I want to ask you a question what is the difference between 
			`X` and `x` 
one of them is capital and the other is small case 


> And in python case is important and python See's the tow like different things so be aware you can't defend `Age` as a capital `A` and call it with small later `a` python will throw an error 


## loops
Loops are a very power full thing in python 
There are two type of loops 
1. For loop and 
2. While loop
### For loops 
We use For loop when we want to do something over and over again 
Or in another word we can use for loop to do something limited times
#### structure 
The structure of for loop is simple 
```
for i in range(0,10):
	print(i)
```
Output. 
`
0
1
2
3
4
5
6
7
8
9`
### while loops
We use while loop when we want to do something thing unlimited times
It ends when a certain condition is met
```
X = 0

while X == 5:
	print(X)
	X = X + 1
```
Let's brake it down line by line

- In The first line is `X = 0` we just define a variable called x 

> [! Remember] 
> ***if you want you can change*** X ***to any thing else you can***

- Then the second line is the while loop it's self and it begins with while and ends with `:` in the middle there is the condition that ends the while loop or in another word if the condition is met the while loop will end 

- the third line is the print statement 

> [! Remember]
> ***you can change the print statement to any thing that doesn't throw error to the terminal ***

- The last line increments the X by one or in another word it adds one ever time
## functions 

Functions are instructions but in sorted way or in organized way 
And the benefits of functions is in it's reusability wans you define a function you can use it again and again any ware in the code

Let's see how to define functions 
```
def [name_of_the_function](parameter):
	print('any text you want')
```

Let's break it down
- The first line is the function it's self and it begins with `def` and ends with `:` inside there is the name `[name_of_the_function]`

Example
```
def happy():
	print('happy birthday')
```
In this example i replaced `[name_of_the_function]` by `happy` the when we want to call the function we just type the name then brackets 
```
happy()
```
This will call the function and the output will be
		`happy birthday`
		
And you can call it as many times as you want you can call it five times ten times a million if you can even you can use loops to call it I don't recommend using a while loop but it works 

Example 
```
for i in range(0, 10):
	happy()
```
This will output happy birthday ten times 
`
happy birthday 
happy birthday 
happy birthday 
happy birthday 
happy birthday 
happy birthday 
happy birthday 
happy birthday 
happy birthday 
happy birthday 
`
Functions help organize the code and reduce hand type and most of all it helps the reader more efficient reading scenario

This are the syntax of python 

> [! Remember]
> ***Python is case sensitive ***

You can ask me any questions in my Instagram or telegram account 

	Telegram :- @yabd2000
	Instagram :- yabu_hat


