def is_palindrome(text):

    text = text.replace(" ", "").lower()
    return text == text[::-1]

user_input = input("Enter a word or phrase to check for palindrome: ")


if is_palindrome(user_input):
    print("✅ It is a palindrome.")
else:
    print("❌ It is not a palindrome.")

