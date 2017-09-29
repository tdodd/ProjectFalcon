import os, fileinput
from shutil import copy2

class DirectoryHelper:
	"""
	This class manipulates the file system
	It creates directories and files where needed
	"""
	def __init__(self, current_directory):
		self.root = current_directory
		self.template_root = '/home/tom/Dev/Python/ProjectFalcon/templates'

	def create_project(self, project_name):
		"""
		Creates a project with all subdirectories and files
		:param project_name: the name of the project
		:return void
		"""

		# Create directories
		if self.create_directories(project_name):
			print('Creating project ' + project_name + '..')

			# Create files once directories have been created
			if self.create_files(project_name):
				print('Done')

	def create_directories(self, project_name):
		"""
		Create all directories and subdirectories
		:param project_name: the name of the project
		:return void:
		"""

		# Project root directory
		r = self.root + '/' + project_name

		try:
			# Make project root
			os.mkdir(r)

			# Make project top-level directories
			os.mkdir(r + '/app')
			os.mkdir(r + '/bin')
			os.mkdir(r + '/config')
			os.mkdir(r + '/public')
			os.mkdir(r + '/test')

			# Make secondary directories
			os.mkdir(r + '/app/layouts')
			os.mkdir(r + '/app/helpers')
			os.mkdir(r + '/public/stylesheets')
			os.mkdir(r + '/public/javascripts')
			os.mkdir(r + '/public/images')
			os.mkdir(r + '/config/environments')
			os.mkdir(r + '/config/locales')
			os.mkdir(r + '/test/helpers')
			os.mkdir(r + '/test/integration')
		except: # Name conflict
			print('This project already exists in this folder')
			return False

		return True

	def create_files(self, project_name):
		"""
		Create all pre-made files
		:param project_name: the name of the project
		:return void:
		"""
		t_dest = self.root + '/' + project_name # Default template destination

		t_dest_public = t_dest + '/public' # Default public files dest
		t_dest_www = t_dest + '/bin' # Default server dest
		t_dest_layout = t_dest + '/app/layouts' # Default layout destination
		t_dest_app = t_dest + '/app'  # Default /app destination

		# Template file names
		template_files = os.listdir(self.template_root)

		# Loop and copy template files
		for file in template_files:
			try:
				# Skip component directory
				if file != 'component':
					# Current template file path
					file_path = self.template_root + '/' + file

					# Non-root destinations
					if file == 'layout.pug':
						copy2(file_path, t_dest_layout)

					elif file == 'index.pug':
						copy2(file_path, t_dest_app)

					elif file == 'index.js':
						copy2(file_path, t_dest_app)

					elif file == 'error.pug':
						copy2(file_path, t_dest_app)

					elif file == 'favicon.ico':
						copy2(file_path, t_dest_public)

					elif file == 'styles.css':
						copy2(file_path, t_dest_public + '/stylesheets')

					elif file == 'scripts.js':
						copy2(file_path, t_dest_public + '/javascripts')

					elif file == 'www':
						copy2(file_path, t_dest_www)

					# Default destination
					else:
						copy2(file_path, t_dest)
			except:
				print('Error creating files')
				return False

		return True

	def create_component(self, component_name):
		"""
		Generate a new component
		:param component_name: the name of the component
		:return void:
		"""

		# /app directory
		app_root = self.root + '/app'

		# New component destination
		component_root = app_root + '/' + component_name

		# Component template files
		index = self.template_root + '/component/index.js' # Router
		model = self.template_root + '/component/model.js' # Model
		view = self.template_root + '/component/view.pug' # View
		controller = self.template_root + '/component/controller.js' # Controller
		styles = self.template_root + '/component/styles.sass' # Styles
		test = self.template_root + '/component/test.spec.js' # Test

		try:
			# Create component directory and files in /app
			os.mkdir(component_root)
			copy2(index, component_root)
			copy2(model, component_root)
			copy2(view, component_root)
			copy2(controller, component_root)
			copy2(styles, component_root)

			# Project test directory
			test_root = self.root + '/test'

			# Component test directory
			component_test = test_root + '/' + component_name

			# Default template test name
			template_test_name = component_test + '/test.spec.js'

			# Component test name
			component_test_name = component_test + '/' + component_name + '.spec.js'

			# Create test directory and file
			os.mkdir(component_test)
			copy2(test, component_test)
			os.rename(template_test_name, component_test_name)

			# Replace {{component name}} in all /app files
			for f in os.listdir(component_root):
				f_name = component_root + '/' + f # File name

				with fileinput.FileInput(f_name, inplace=True) as file:
					for line in file:
						print(line.replace('{{component_name}}', component_name), end='')

			print(component_name + ' component created.')
		except():
			print('Could not create component')
			return False

		return True
