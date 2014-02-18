'''
	Swarm AI IPS - Blue Deer

	By Adam Ringwood
'''

import os
import logging

class Swarm_AI():

	logger = None
	settings = None

	def __init__(self):
		self.setup_logger()
		self.get_modules()

	# Gets the possible modules.
	def get_modules(self):
		# check if directory exists
		if (not os.path.isdir('modules')):
			self.logger.critical('Modules directory must exist in order to run.')
			exit(-1)

		possible_modules = os.walk('modules').next()[1]
		for mod in possible_modules:
			self.logger.debug('Possible mod: {0}'.format(mod))

			if (os.path.exists(os.path.join('modules',mod,'module.info'))):
				self.logger.debug('Mod: {0} has an info file.'.format(mod))
				self.process_info(os.path.join('modules',mod,'module.info'))

	# Most of this code was taken from: http://docs.python.org/2/howto/logging-cookbook.html
	def setup_logger(self):
		self.logger = logging.getLogger("swarm-ai")
		self.logger.setLevel(logging.DEBUG)

		fh = logging.FileHandler('results.log')
		fh.setLevel(logging.DEBUG)

		ch = logging.StreamHandler()
		ch.setLevel(logging.DEBUG)

		formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		fh.setFormatter(formatter)
		ch.setFormatter(formatter)

		self.logger.addHandler(fh)
		self.logger.addHandler(ch)

		self.logger.debug('Logger setup.')

	def process_info(self, path):
		self.settings = {}

		f = open(path, 'r')

		for line in f:
			if (not ":" in line):
				self.logger.error("Line is not formatted correctly, must have a \":\" between key and value.")
			else:
				self.settings[line.split(":")[0].strip()] = line.split(":")[1].strip()
				self.logger.debug("{0} has been added with value: {1}".format(line.split(":")[0].strip(),line.split(":")[1].strip()))

		for key in ["name","author","version"]:
			if not key in self.settings:
				self.logger.error("{0} is required in the settings file.".format(key))

if __name__ == '__main__':
	simulation = Swarm_AI()