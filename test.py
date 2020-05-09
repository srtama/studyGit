# google 回文生成
letters = [chr(i) for i in range(97, 97+26)]
k = int(input())    # kー1番目のアルファベットまで使用
c_list = input()     # 入力文字列
s = len(c_list)

# print(letters)
use_letters = [0]*len(letters)

# print(letters.index(c_list[0]))

ans = [None]*s

for i in range(s):
    if c_list[i] == '?':
        if i<s//2:
            ans[i] = c_list[-1-i]
        else:
            ans[i] = c_list[s-i-1]
    else:
        ans[i] = c_list[i]
        use_letters[letters.index(c_list[i])] = 1
# print(ans)
# print(type(ans))

if '?' in ans == True:
    for i in range(k):
        if use_letters[i] == 0:
            ans[i] = letters[i]
            use_letters[letters.index(ans[i])] = 1

if sum(use_letters) != k:
    print('Impossible')
else:
    print(" ".join(ans))
