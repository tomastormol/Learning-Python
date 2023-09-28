def no_space(text):
    new_text = ""
    for letter in text:
        if letter != " ":
            new_text += letter
    return new_text

def reverseText(text):
    rev_text = ""
    for char in text:
        rev_text = char + rev_text
    return rev_text

def isPalindrome(text):
    no_space_text = no_space(text)
    reverse_text = reverseText(no_space_text)
    return text == reverse_text

print(isPalindrome("ReconoceR"))
print(isPalindrome("Reconoce"))
print(isPalindrome("abba"))
