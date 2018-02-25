#!/usr/bin/env python3

import platform

def main():
	message()

def message():
	print('This is Python {}'.format(platform.python_version()))
	print('Line 2')
	if False:
		print('Line 3')
	else:
		print('Not in the if-block')

if __name__ == '__main__': main()