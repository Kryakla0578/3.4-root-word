def single_root_word(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.upper() in i.upper() or i.upper() in root_word.upper():
            same_words.append(i)
    return same_words


result1 = single_root_word('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result1)
result2 = single_root_word('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result2)