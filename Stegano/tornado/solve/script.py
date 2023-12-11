import sys
file = open(sys.argv[1], 'rb')
qwe = bytearray(file.read())
for i in range(0, len(qwe)-1, 2):
	qwe[i], qwe[i+1] = qwe[i+1], qwe[i]
file.close()
file_res = open("res.png", 'wb')
file_res.write(qwe)

	
