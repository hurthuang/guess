import random
s = input('請輸入最小值：')
s = int(s)
e = input('請輸入最大值：')
e = int(e)
r = random.randint(s, e)
t = 0
print('範圍(', s, '~', e, ')')
while True:
	num = input('請猜數字：')
	num = int(num)
	if num == r:
		print('恭禧答對了！共答了', t + 1, '次')
		break
	else:
		if num > r:
			print('太大了！')
		if num < r:
			print('太小了！')
		t = t + 1
		print('你猜錯了', t, '次')