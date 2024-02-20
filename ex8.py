formatter = "%r %r %r %r"

print (formatter % (1, 2, 3, 4))
print (formatter % ("one", "two", "three", "four"))
print (formatter % (True, False, False, True))
print (formatter % (formatter, formatter, formatter, formatter))
print (formatter % (
    "I had this thing.",
    "That you could type up right,",
    "But it did't sing.", # didin't 有使用到'符號，變成""以概括句首與句尾
    "So I said goodnight."
))
