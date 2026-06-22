# For Loop
# Example_01

for i in range(5):
    print(i)
print("\n")


# RANGE VARIATION

# =>> range(start, stop)
for i in range(1, 5):
    print(i)
print("\n")


# =>> range(start, stop, step)
for i in range(1,20,2):
    print(i)
print("\n")

# =>> Looping through strings
for char in "python":
    print(char)
print("\n")

# =>> Looping through lists
# =>> Nested loops

# =>> Breaking a loop with break & continue

# Note:-> loop will exit when x= "banana", Here it is printing the value of X before checking
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
print("\n")

# :-> Here it is checking before printing
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
print("\n")


''' :-> When we use break to break out of a loop, it will not print the next value or iterate over next value
  ie. Loop will be terminated when the condition is met but When we want to continue the loop with certain condition
  in this case we just don't want to print the value of X="banana" and want to print the next value so we will use continue.
'''

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
print("\n")
