# #自己尝试
# name='刘少卿'
# age=25
# print("你好！我叫%s,今年%s岁"%(name,age))
#
#
# # 错误版本
# name='刘少卿'
# age=25
# print(你好！我叫%s,今年%s岁%(name,age))
#
# #AI提供版本 （不行）
# name='刘少卿'
# age=25
# print(f"你好!我叫{name}，今年{age}岁了!")

# 根据教程调整版本
name='刘少卿'
age=25
print("你好!我叫{}，今年{}岁了!".format(name,age))


name='lsq'
age='1999'
phone='131213121'
print('你好，我叫{}~ 今年{}岁了，这是我的电话{}'.format(name,age,phone))

name=input('输入你的昵称')
SexTime=input('一共做过多少次')
# 变量名字不能随便空格，否则会报错
phone=input('手机号填一下')
print('姓名：{}  做爱次数：{} 手机号：{}'.format(name,SexTime,phone))

