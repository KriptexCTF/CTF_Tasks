block = [ ';', '"', 'os', '_', '\\', '/', '`', ' ', '-', '!', '[', ']', '*',
          'eval', 'banner', 'echo', 'cat', '%', '&', '>', '<', '+', '1', '2', '3', '4',
          '5', '6', '7', '8', '9', '0', 'b', 's', 'lower', 'upper', 'system', '}', '{' ]

not_today = '''
███╗░░██╗░█████╗░████████╗  ████████╗░█████╗░██████╗░░█████╗░██╗░░░██╗██╗
████╗░██║██╔══██╗╚══██╔══╝  ╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝██║
██╔██╗██║██║░░██║░░░██║░░░  ░░░██║░░░██║░░██║██║░░██║███████║░╚████╔╝░██║
██║╚████║██║░░██║░░░██║░░░  ░░░██║░░░██║░░██║██║░░██║██╔══██║░░╚██╔╝░░╚═╝
██║░╚███║╚█████╔╝░░░██║░░░  ░░░██║░░░╚█████╔╝██████╔╝██║░░██║░░░██║░░░██╗
╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░  ░░░╚═╝░░░░╚════╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝
'''

print("Lets go!\n")
while True:
	ans = input('=> ').strip()
	if any(char in ans for char in block):
		print(not_today)
	else:
		try:
			ans = ans + '()'
			eval(ans)
			print('You did this!\n')
		except:
			print("Oh-Oh....\n")
