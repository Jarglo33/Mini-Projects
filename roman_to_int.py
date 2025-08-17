romanNum = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

romanList =[['M','D','C','L','X','V','I'],[1000,500,100,50,10,5,1]]
	
def roman_to_integer(num):
	output = 0
	skip = False
	for i in range(len(num)):
		if skip:
			skip = False
			continue
		try:
			if romanNum[num[i]] < romanNum[num[i+1]]:
				output += romanNum[num[i+1]]-romanNum[num[i]]
				skip = True
			else:
				output += romanNum[num[i]]
		except:
			output += romanNum[num[i]]
	return output

def roman_converter(out, v, ovl='\u0305',m=0):
	output, value = out, v
	for i in range(len(romanList[0])):
		if romanList[1][i]*(3*(1000**m)) <= value:
			value -= romanList[1][i]*(3*(1000**m))
			output += f'{romanList[0][i]}{ovl*m}'*3
		elif romanList[1][i]*(2*(1000**m)) <= value:
			value -= romanList[1][i]*(2*(1000**m))
			output += f'{romanList[0][i]}{ovl*m}'*2
		elif romanList[1][i]*(1000**m) <= value:
			value -= romanList[1][i]*(1000**m)
			output += f'{romanList[0][i]}{ovl*m}'

		if value > (300*(1000**m)) and (romanList[1][i]*(1000**m))-(100*(1000**m)) <= value:
			value -= (romanList[1][i]*(1000**m))-(100*(1000**m))
			output +=  f'{romanList[0][2]}{ovl*m}{romanList[0][i]}{ovl*m}'
		elif value > (30*(1000**m)) and (romanList[1][i]*(1000**m))-(10*(1000**m)) <= value:
			value -= (romanList[1][i]*(1000**m))-(10*(1000**m))
			output +=  f'{romanList[0][4]}{ovl*m}{romanList[0][i]}{ovl*m}'
		elif value > (3*(1000**m)) and (romanList[1][i]*(1000**m))-(1000**m) <= value:
			value -= (romanList[1][i]*(1000**m))-(1000**m)
			output +=  f'{romanList[0][6]}{ovl*m}{romanList[0][i]}{ovl*m}'
	return (output, value)

def integer_to_roman(num):
	value = num
	m=0
	output = ''
	while value > int('3999'+('999'*m)):
		m+=1
	for i in range(m,-1,-1):
		output,value=roman_converter(output,value,m=i)
		
	return f'{output}\nAmount Left:{value}'

def printRoman(num):
	print(f'\n{num} = {integer_to_roman(num)}')

def saveRoman(num):
	print(f'\n{num} = {integer_to_roman(num)}')

	with open('output.txt','w') as f:
		f.write('\n'*50+f'{integer_to_roman(num)}')
	
printRoman(3999)