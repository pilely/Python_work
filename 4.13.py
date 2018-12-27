# coding=gbk
print("origian:")
foods = ('A', 'V', 'G', 'R', 'T')    #元组将其所包含的元素使用小括号括起来
for food in foods:
	print(food)
#foods[0] = 'Y'   元组的值不可修改
print("New:")
foods = ('H', 'Q', 'G', 'R', 'T')  #但是可以重新赋值
for food in foods:
	print(food)
