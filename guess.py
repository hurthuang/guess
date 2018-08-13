import random
r = random.randint(1, 100)
t = 0
while True:
	num = input('請猜數字(1~100)：')
	num = int(num)
	if num == r:
		print('恭禧答對了！')
		break
	else:
		if num > r:
			print('太大了！')
		if num < r:
			print('太小了！')
		t = t + 1
		print('你猜錯了', t, '次')