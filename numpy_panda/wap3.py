'''
check whether a string is palindrom
that the first and last elemnet are same, second and second last
'''
user_string = input("enter the string:-")
#racecar
print("The string you entered is :-",user_string)
rev_string = user_string[-1::-1]
if user_string == rev_string:
    print("The given string is palindrome")
else:
    print("The string is not a palindrome")
