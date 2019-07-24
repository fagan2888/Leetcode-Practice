cat file.txt | grep -P '^\(\d{3}\) \d{3}-\d{4}$'

'''

^ 開頭
(A|B) A或是B
\d{3}- 有三個數字 "xxx"
\(\d{3}\) "(xxx) "
$ 結尾
'''