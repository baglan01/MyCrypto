check = int(input("for enc = 1 , for dec = 2 "))
if check == 1 : 
	p = 991 
	q = 997
	N = p*q # 988 027
	f = (p-1)*(q-1) # 990 * 996 = 986 040
	d = 0 
	e = 986023 
	for i in range(0 , 10000000) : 
		if (i * e) % f == 1: 
			d = i 
			print("d is " , d)
			break

	def encode_RSA(word):
	    ret = []
	    for v in word:
	        n = ord(v)
	        ret.append(int(n**d%N))
	    return ret

	def decode_RSA(word):
	    ret = []
	    for v in word:
	        sim = (v**e)%N
	        ret.append(chr(sim))
	    return ret
	#сетка эратасфена не заюзана в коде юзал отдельно 
	def ertas(n): 
		a = []
		for i in range(n + 1):
		    a.append(i) 
		a[1] = 0
		#Заполняем массив , 0-n , 1й элемент у нас 1 это не простое число а 0ой это 0 поэтому идем с3го эелемента
		i = 2
		while i <= n:
		    if a[i] != 0:
		        # составное число это плюсы двух не составных и поэтому берем составное как j а потом после этого приравниваем его к 0ю а потом идем дальше
		        j = i + i
		        while j <= n:
		            a[j] = 0
		            j = j + i
		    i += 1
		a.sort()
		a = set(a)
		# делаем из массива лист что бы легче было удалить 0 и собственно удаляем его 
		a.remove(0)
		p = max(a)
		print(p)
		a.remove(p)
		q = max(a)
		print(q)	
	b = int(input("Max diapation of P and Q : "))
	ertas(b)
	print("Your e : ")
	a = []
	for i in range(f+1):
		a.append(i) 
	a[1] = 0
	#Заполняем массив , 0-n , 1й элемент у нас 1 это не простое число а 0ой это 0 поэтому идем с3го эелемента
	i = 2
	while i <= f:
		if a[i] != 0:
			# составное число это плюсы двух не составных и поэтому берем составное как j а потом после этого приравниваем его к 0ю а потом идем дальше
			j = i + i
			while j <= f:
				a[j] = 0
				j = j + i
		i += 1
	a.sort()
	a = set(a)
		# делаем из массива лист что бы легче было удалить 0 и собственно удаляем его 
	a.remove(0)
	e = max(a)	
	print(e)
	word = input("Your word is ")
	l = encode_RSA(word)
	print(l)
	print(decode_RSA(l))
if check == 2 : 
	p = 991 
	q = 997
	N = p*q # 988 027
	f = (p-1)*(q-1) # 990 * 996 = 986 040
	d = 0 
	e = 986023 
	A = list(map(int, input("Your numbers ").split()))
	def decode_RSA(word):
	    ret = []
	    for v in word:
	        sim = (v**e)%N
	        ret.append(chr(sim))
	    return ret
	print(decode_RSA(A))