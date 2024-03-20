def is_palindrome(word):
    length = len(word)
    if type(word) is not str or length == 0 or length % 2 != 0:
        return False
    for i in range(length):
        if word[i] != word[length-i-1]:
            return False
    return True
