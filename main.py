# syntax error
# print(Hello world) - a string has to have quotes around them

# this is the correct entry
print("Hello world")


# runtime error
# 10 * (2/0) - any number divided by 0 is undefined 

# this is the correct entry / added the print command to see it
answer = 10 * (10/2)
print(answer)

# semantic error
# name = "Alice"
# print("Hello name") - wanted to see "Hello Alice" so this means that i didn't get the expected results in my program

# this is the correct way
name = "Alice"
print("Hello " + name)