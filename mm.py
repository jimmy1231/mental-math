import pyttsx3
import random
import math

if __name__ == "__main__":
	ops = ['+', '-', '*', '/'];

	engine = pyttsx3.init()
	engine.setProperty('volume', 1.0)
	engine.setProperty('rate', 130)

	eval = random.randint(0, 20)
	print('Start with {}'.format(eval))
	engine.say('Start with {}'.format(eval))
	engine.runAndWait()
	for i in range(0, 10):
		op = ops[random.randint(0,len(ops)-1)]
		str = ''

		if op == '+':
			num = random.randint(1, 20)
			eval = eval + num
			str += 'plus {}'.format(num)
		elif op == '-':
			num = random.randint(1, 20)
			eval = eval - num
			str += 'minus {}'.format(num)
		elif op == '*':
			num = random.randint(1, 3)
			eval = eval * num
			str += 'times {}'.format(num)
		elif op == '/':
			num = random.randint(1, 3)
			if math.fmod(eval/num, 1) != 0:
				continue
			eval = eval / num
			str += 'divide by {}'.format(num)

		print(str)
		engine.say(str)
		engine.runAndWait()

	print('Did you get {}?'.format(int(eval)))
	engine.say('Did you get {}?'.format(int(eval)))
	engine.runAndWait()