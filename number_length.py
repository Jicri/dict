data = []
sum_len = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
    # for row in data:
        #sum_len += len(row)
        # print(sum_len)
#print("平均是:", sum_len / len(data))

word_count = {}
for d in data:
    words = d.split(' ')
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
for word in word_count:
    if word_count[word] > 1000:
        print(word, word_count[word])

while True:
    word = input("請輸入要查的字:")
    if word == 'q':
        break
    elif word in word_count:
        print(word, "出現了", word_count[word], "次")
    else:
        print("該字典中沒有這個字")
print("感謝你的使用")
