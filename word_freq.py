def freq_word(str):
    word_freq={}
    words=str.split()
    for word in words:
        if word in word_freq:
            word_freq[word]+=1
        else:
            word_freq[word]=1
    return word_freq
 
print(freq_word("hello world hello"))