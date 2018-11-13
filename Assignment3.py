def palindrome_checker(word):
    word = word.lower()
    palindrome = True 
    i = 0 
    while i < len(word)/2:
        print(word[i] + word[len(word)-i-1])
        if word[i] != word[len(word)-i-1]:
            palindrome = False
        i += 1
    return palindrome
#TESTCASES
#print(palindrome_checker("Hannah"))
#print(palindrome_checker("Racecar"))
    
def palindrome_checker_user():
    word = input("Enter a word that might be a palindrome:     ")
    print(palindrome_checker(word))
palindrome_checker_user()
print("Boobies")