# -*- coding: utf-8 -*-
#ex5.py
my_name = 'Zed A. Shaw'
my_age =35 # not a lie
my_hight = 74 # inches
my_weight =180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_hight
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d i get %d." %(my_age, my_hight, my_weight, my_age+my_hight+my_weight)
#---------------------------------------------------------------------------------------------------
#学习心得1：Python格式化字符
#         %%	百分号标记 #就是输出一个%
#         %c	字符及其ASCII码
#         %s	字符串(采用str()的显示)
#         %r	字符串(采用repr()的显示)
#         %d	有符号整数(十进制)
#         %u	无符号整数(十进制)
#         %o	无符号整数(八进制)
#         %x	无符号整数(十六进制)
#         %X	无符号整数(十六进制大写字符)
#         %e	浮点数字(科学计数法)
#         %E	浮点数字(科学计数法，用E代替e)
#         %f	浮点数字(用小数点符号)
#         %g	浮点数字(根据值的大小采用%e或%f)
#         %G	浮点数字(类似于%g)
#         %p	指针(用十六进制打印值的内存地址)
#         %n	存储输出字符的数量放进参数列表的下一个变量中
#学习心得2：下面是%r的一些例子
i = 5
print "%r" % i
s="abc"
print "%r" % s
d={}
print "%r" % d
x="汉字"
print "%r" % x
#学习心得3：浮点数四舍五入round函数
print round(1.7777,2), round(1.12345, 4)