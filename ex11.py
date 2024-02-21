print ("How old are you?"),
# age = raw_input()
age = input()
print ("How tall are you?"),
# height = raw_input()
height = input()
print ("How much do you weight?"),
# weight = raw_input()
weight = input()

print ("So, you're %r old, %r tall and %r heavy." % (age, height, weight))

# 在 Python3.x 中 raw_input( ) 和 input( ) 進行了整合，去除了 raw_input( )，僅保留了 input( ) 函數，其接收任意任性輸入，將所有輸入都默認爲字串處理，並返回字串的類型。

# 輸入 6'2" 顯示 '6\'2"' 是因為單引號必須被轉譯，那是跳脫字元，以防止它被視為字串的結尾
