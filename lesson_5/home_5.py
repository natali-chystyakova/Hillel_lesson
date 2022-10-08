# home 5_1 (д/з 3)
string = input("Введите предложение из двух слов: ")
print(string)
word_1 = string.split()[0]
word_2 = string.split()[1]
print(word_1)
print(word_2)
spos_1 = "! %s %s ?" % (word_1[::-1].upper(), word_2[::-1].title())
print(spos_1)
spos_2 = "! {0} {1} ?".format(word_1[::-1].upper(), word_2[::-1].title())
print(spos_2)
spos_3 = f"! {word_1[::-1].upper()} {word_2[::-1].title()} ?"
print(spos_3)

written_string = open("text_my_file.txt", "w")
print(string, spos_1, spos_2, spos_3, file=written_string, sep="<<<>>>", end="")
written_string.close()