from sys import argv

script, user_name = argv
prompt = '> '

# % 是字串的格式化工具
print ("Hi %s, I'm the %s script." % (user_name, script))
print ("I'd like to ask you a few questions.")
print ("Do you like me %s?" % user_name)
likes = input(prompt)

print ("Where do you live %s?" % user_name)
lives = input(prompt)

print ("What kind of computer do you have?")
computer = input(prompt)

print ("What kind of cellphone do you have?")
cellphone = input(prompt)

# 可以透過 """ 來定義多行字串
print ("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer, a %r cellphone. Nice.
""" % (likes, lives, computer, cellphone))


