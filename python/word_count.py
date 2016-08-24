d ={i:i+1 for i in range(4)}
#{i为键，i+1 值}
print(d)
#============================词频统计
import string
def word_count():
    path ='D:\PycharmProjects/a month\Walden.txt'
    with open(path,'r',encoding='UTF-8') as text:
        words=[raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
        # strip(string.punctuation) 删除标点符号
        words_index = set(words)
        # 序列会自动删除重复
        count_dict = {index: words.count(index) for index in words_index}
        #词为键。 次数为值
        for word in sorted(count_dict,key= lambda x: count_dict[x],reverse= True):
            print('{}-{}times'.format(word,count_dict[word]))

word_count()