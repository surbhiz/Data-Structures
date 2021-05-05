word_list = ['cat', 'dog', 'rabbit']
letter_list = []
for word in word_list:
    for i in range(len(word)):
        if word[i-1] != word[i]:
            letter_list.append(word[i])

print(letter_list)


lst = [(letter_a) for word_a in word_list for letter_a in word_a]
print(lst)

lst1 = [(word_a[i]) for word_a in word_list for i in range(
    len(word_a)) if word_a[i-1] != word_a[i]]
print(lst1)
