#!/usr/bin/env python

"""
This is ProjectFalcon! The tool for scaffolding your projects in a logical manner.
	Focus on development, not on files and folder structure

Usage: Start the script from inside the project's parent folder
	ex: ~/Projects/Angular if you want to create ~/Projects/Angular/MyProject
	Run pf new MyProject
"""
import sys
from scripts.command_handler import CommandHandler

if __name__ == '__main__':
	cmd_handler = CommandHandler()

	# 1 arg
	if len(sys.argv) == 2:
		cmd_handler.process_command(sys.argv[1])

	# 2 args
	elif len(sys.argv) == 3:
		cmd_handler.process_command(sys.argv[1], sys.argv[2])

	# Invalid command
	else:
		print(cmd_handler.get_message('invalid_command'))
