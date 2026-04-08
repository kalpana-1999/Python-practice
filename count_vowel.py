def count_vowels(str):
    count=0
    for i in str:
        if i in "aeiouAEIOU":
            count+=1
    return count

print(count_vowels("Appleou"))
