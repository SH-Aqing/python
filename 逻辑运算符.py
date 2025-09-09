# # 逻辑运算符 and or not
# # and   条件比较严格
# # 定义四个变量
# a,b,c,d=23,18,10,3
# #
# # print(a+b>c and c<d)
# # print(c>d and a>b)
# #
# # # or 条件有一个为真 结果就为真
# # print(a<b or b>d)  #true 有一个满足即可
# # print(a<b or b<d)
#
# # not  取反   真假切换
# print(not  a<b)
# print(not  a>b)
#
# # 优先级,2
# print(2>1 and 1<4    or 2<3 and  9>6  or  2<4  and  3<2)
#
#
# input练习  获取键盘输入的内容
name=input('请输入你的名字：')
age=input('请输入你的年龄：')
adderss=input('请输入你的地址：')
phone=input('请输入你的电话：')

print('姓名：{} 年龄：{}'.format(name,age))
print('地址：{} 电话：{}'.format(adderss,phone))


