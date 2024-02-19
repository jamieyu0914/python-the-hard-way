my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print ("Let's talk about %r." % my_name)
print ("He's %r inches tall." % my_height)
print ("He's %r pounds heavy." % my_weight)
print ("Actually that's not too heavy.")
print ("He's got %r eyes and %r hair." % (my_eyes, my_hair))
print ("His teeth are usually %r depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print ("If I add %r, %r, and %r I get %r." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight))

# %% 百分號標記 # 就是輸出一個%
# %c 字符及ASCII碼
# %s 字符串
# %d 有符號的整數(十進位制)
# %u 無符號的整數(十進位制)
# %o 無符號的整數(八進位制)
# %x 無符號的整數(十六進位制)
# %X 無符號的整數(十六進位制大寫字符)
# %e 浮點數字(科學記號表示法)
# %E 浮點數字(科學記號表示法，用E代替e)
# %f 浮點數字(用小數點符號表示)
# %.2f 浮點數字(指定小數點後2位數)
# %.3f 浮點數字(指定小數點後3位數)
# %.4f 浮點數字(指定小數點後4位數)
# %g 浮點數字(根據值的大小採用%e或%f)
# %G 浮點數字(類似於%g)
# %p 指針(用十六進位制打印值的內存地址)
# %n 儲存輸出字符的數量放進參數列表的下一個變量中
# %  格式化的符號也可以用於字典，可用%(name)引用字典中的元素進行格式化輸出


#嘗試使用變量進行單位轉換

Lenth = 39
Weight = 200

IN = 1
CM = 2.54

LB = 1
KG = 0.45

print ('%.2f' % (Lenth*IN), "IN", "----->", '%.2f' % (Lenth*CM), "CM")
print ('%.3f' % (Weight*LB), "LB", "----->", '%.3f' % (Weight*KG), "KG")

# 輸出結果是
# 39.00 IN -----> 99.06 CM
# 200.000 LB -----> 90.000 KG
