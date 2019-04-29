def four_letter_words(sentence):
    s=sentence.split()
    count=0
    for s1 in s:
        if(len(s1)==4):
            count+=1
    return count


i=four_letter_words("abcd sagdja asjdg a wecd")
print(i)
