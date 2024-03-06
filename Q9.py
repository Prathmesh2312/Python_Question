#Write a Python program to check if a string is a palindrome or not.
def palindeome(string):
    string = string.lower()
    return string == string[::-1]

string = input("Enter your String:")
checking = palindeome(string)
if checking:
    print("Yes it is palindrome")
else:
    print("No it is not palindronme")

