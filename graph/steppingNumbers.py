def bfs(n, m, num) :

	q = []
	q.append(num)
	while len(q) > 0 :
	
		stepNum = q[0]
		q.pop(0);

		if (stepNum <= m and stepNum >= n) :
			print(stepNum, end = " ")

		if (num == 0 or stepNum > m) :
			continue

		lastDigit = stepNum % 10

		stepNumA = stepNum * 10 + (lastDigit- 1)
		stepNumB = stepNum * 10 + (lastDigit + 1)

		if (lastDigit == 0) :
			q.append(stepNumB)

		elif (lastDigit == 9) :
			q.append(stepNumA)

		else :
			q.append(stepNumA)
			q.append(stepNumB)

def displaySteppingNumbers(n, m) :

	for i in range(10) :
		bfs(n, m, i)

n, m = 0, 21

displaySteppingNumbers(n, m)

