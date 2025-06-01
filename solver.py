from itertools import permutations


def ev(start, it):
	x = start
	for i in it:
		if i[0] in ('/', '*', '-', '+'):
			y = int(i[1:])
			x = int(eval(str(x) + i))
			if x < 0:
				x = -100000
		else:
			y = int(i)
			x = x + y if x > y else -100000
	return x


start = int(input('input starting int\n'))

while True:
	ops = input('input all var\n').replace('x','*')
	inputs = ops.split(' ')

	maxv = -1
	max_iter = None

	for it in permutations(inputs):
		v = ev(start, it)
		if v > maxv:
			maxv, max_iter = v, it 

	print("maxv = " , maxv )
	print(max_iter )

	start = maxv
