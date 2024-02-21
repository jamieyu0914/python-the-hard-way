"I am 6'2\" tall." # 將字串中的雙引號轉譯
'I am 6\'2" tail.' # 將字串中的單引號轉譯

# \     # (行尾的)續行符號
# \\    # 反斜槓符號
# \'    # 單引號
# \"    # 雙引號
# \a    # 響鈴一聲
# \b    # 退格(Backspace)
# \e    # 轉譯
# \000  # 空
# \n    # 換行
# \v    # 縱向制
# \t    # 橫向制
# \r    # 回車
# \f    # 換頁
# \oyy  # 八進制，y代表0~7的字符，例如: \012代表換行
# \xyy  # 十六進制，以\x開頭，yy代表的字符，例如: \x0a代表換行
# \other # 其他的字符以普通格式輸出 

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)

print("""[aaa bbb]""")
print('''[aaa bbb]''')

print("""[aaa\n bbb] 換行""")
print("""[aaa\t bbb] 空白""")

a = "雙引號"
b = "單引號"
print("""[%r aaa\n bbb 換行 r]""" % a)
print('''[%r aaa\t bbb 空白 r]''' % b)

print("""[%s aaa\n bbb 換行 s]""" % a)
print('''[%s aaa\t bbb 空白 s]''' % b)
