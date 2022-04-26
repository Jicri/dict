import time
import progressbar

data = []
sum_len = 0
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
start_time = time.time()
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        bar.update(count)
        # if count % 1000 == 0:
        #     print(len(data))
    print("檔案讀取完了，總共", len(data), "筆" )
end_time = time.time()
print("總共花費", end_time - start_time, "s的時間")
    # for row in data:
        #sum_len += len(row)
        # print(sum_len)
#print("平均是:", sum_len / len(data))

# word_count = {}
# for d in data:
#     words = d.split(' ')
#     for word in words:
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
# for word in word_count:
#     if word_count[word] > 1000:
#         print(word, word_count[word])

# while True:
#     word = input("請輸入要查的字:")
#     if word == 'q':
#         break
#     elif word in word_count:
#         print(word, "出現了", word_count[word], "次")
#     else:
#         print("該字典中沒有這個字")
# print("感謝你的使用")
