def encryption(word,mpass):
	key = mpass[0] + mpass[-1] + mpass[3] + mpass[2]
	
	word_array = []
	key_array = []
	
	for c in word:
		word_array.append(ord(c))
	for c in key:
		key_array.append(ord(c))
	
	j = 0
	
	for i in range(len(word_array)):
		if i%2 == 1:
			word_array[i] += key_array[j]
			if word_array[i] > 126:
				while word_array[i]<40 or word_array[i]>126: 
					word_array[i] = word_array[i]%126 + 39 
				#word_array[i] = chr(word_array[i])
		
		if i%2 == 0:
			word_array[i] -= key_array[j]
			if word_array[i] < 40:
				word_array[i] += (127 - 40)
				#word_array[i] = chr(word_array[i])
		
		word_array[i] = chr(word_array[i])		
		j += 1
		if j == len(key_array):
			j = 0
	
	encryp = ''
	for c in word_array:
		encryp += str(c)
	return encryp

			
		
	


