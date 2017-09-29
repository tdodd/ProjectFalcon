from os import getcwd
from .messages import MESSAGES
from .directory_helper import DirectoryHelper

class CommandHandler:
	"""
	Command handling class
	Receives command and argument, then performs the necessary actions with a controller if necessary
	"""
	def __init__(self, directory_helper=None):
		self.messages = MESSAGES

		# Inject DirectoryHelper
		if directory_helper == None:
			self.dhelper = DirectoryHelper(getcwd())
		else:
			self.dhelper = directory_helper

	def process_command(self, command, argument=''):
		"""
		Handle a command to the program
		:param command: the PF command
		:param argument: the PF command argument
		:return: void
		"""

		# new
		if command == 'new':
			# Check for project name
			if argument != '':
				self.dhelper.create_project(argument)

			# No project name
			else:
				print(self.get_message('no_project_name'))

		# help
		elif command == 'help':
			# No arguments
			if argument == '':
				print(self.get_message('help'))

			# Unnessesary args
			else:
				print(self.get_message('invalid_command'))

		# generate
		elif command == 'g':
			# Check for component name
			if argument != '':
				self.dhelper.create_component(argument)
			else:
				print(self.get_message('no_component_name'))

		else: # No command name
			print(self.get_message('invalid_command'))

	def get_message(self, message):
		"""
		Get a message from the list of pre-defined messages
		:param message: the message to display
		:return: the message if it exists, and false otherwise
		"""
		if message in self.messages:
			return self.messages[message]
		else:
			return False
