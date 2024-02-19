x = "There are %d types of people." % 10 # 帶入整數10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # 帶入文字binary以及don't

print (x) # 印出完整的"There are 10 types of people."
print (y) # 印出完整的"Those who know binary and those who don't."

print ("I said: %r." %x) # 印出完整的"I said: 'There are 10 types of people.'."
print ("I also said: '%s'." % y) # 印出完整的"I also said: 'Those who know binary and those who don't.'."

hilarious = False

joke_evaluation = "Isn't that joke so funny?! %r" # %r 將帶入任意參數

print (joke_evaluation % hilarious) # 讓 hilarious 這個變量帶入 %r

w = "This is the left side of..."
e = "a string with a right side."

print (w + e) # 印出w與e兩字串合併後的內容
