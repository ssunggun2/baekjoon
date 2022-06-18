# 그룹 단어 체커
def get_continue_index(word, num):
    length = len(word)
    for i in range(num,length):
        character=word[i]
        for j in range(i, length):
            cha2 = word[j]
            # print(character)
            # print(cha2)
            if character != cha2:
                return j
            else:
                continue
    return length

# print(get_continue_index('aaaaaaaa', 0))

def group_word_checker(word):
    length = len(word)
    for i in range(length):
        cha = word[i]
        lastIndex = get_continue_index(word, i)
        # print(f"word:{word}")
        # print(f"cha:{cha}")
        # print(f"lastIndex:{lastIndex}")
        for j in range(length-1, lastIndex, -1):
            # print(f"word:{word}")
            # print(f"cha:{cha}")
            # print(f"lastIndex:{lastIndex}")
            
            if word[j] == cha:
                return word
            else:
                continue

N = int(input())
count = 0
for _ in range(N):
    word = input()
    if group_word_checker(word) == None:
        count+=1
print(count)