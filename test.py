# n,m = map(int,input().split(' '))
# a_i = [input() for i in range(n)]
# b_i = [input() for i in range(m)]

# for i in range(n):
#     ans = 0
#     a = a_i[i].split(' ')
#     for j in range(m):
#         ans = ans + int(a[j]) * int(b_i[j])
#     print(ans)

# while True:
#     a,b,c = map(int, input().split(' '))
#     score = []

#     if a==-1 and b==-1 and c==-1:
#         break
#     else:
#         if a==-1 or b==-1:
#             score = 'F'
#         elif a+b >= 80:
#             score = 'A'
#         elif a+b >= 65:
#             score = 'B'
#         elif a+b >= 50:
#             score = 'C'
#         elif a+b >= 30:
#             if c >= 50:
#                 score = 'C'
#             else:
#                 score = 'D'
#         else:
#             score = 'F'

#     print(score)


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
