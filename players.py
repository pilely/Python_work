# coding=gbk
players = ['euadf', 'nchbwe', 'qiudh', 'cxywb']
print(players[0 : 2])   #输出下标为0和1的元素  称为切片
print(players[: -1])  #切片范围可以是任意合法的范围
print(players[2 : ])

for player in players[0:3]:
	print(player)
