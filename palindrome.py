word=input("Enter a word to check if it is a palindrome:")
if word==word[::-1]:
    print("Given word is a palindrome")
else:
    print("Given word is not a palindrome")