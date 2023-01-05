n = int(input())
words = []
for i in range(n):
    words.append(input())

set_words = sorted(list(set(words)))
set_words.sort(key=len)

for word in set_words:
    print(word)