#!/usr/bin/env python3

import sys

def main():
	if len(sys.argv)<2:
                print("usage: python3 ParamChanger.py <payload>")
                sys.exit(1)
        else:
		for line in sys.stdin:
			try:
				params = dict(x.split('=') for x in line.split('&'))
				for key, value in params.items():
					params[key]=sys.argv[1]
				url = '&'.join('{}={}'.format(key, value) for key, value in params.items())
				print(url)
			except:
				pass

if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		print("A problem has occured.")
		print("Error info:")
		print(e)
	except KeyboardInterrupt:
	       	print("Script canceled.")	
