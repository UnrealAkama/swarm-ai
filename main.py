'''
	Swarm AI IPS - Blue Deer

	By Adam Ringwood
'''

import os
import logging

class Swarm_AI():

	logger = None

	def __init__(self):
		self.setup_logger()
		self.get_modules()

	# Gets the possible modules.
	def get_modules(self):
		# check if directory exists
		if (not os.path.isdir('modules')):
			logger.critical('Modules directory must exist in order to run.')
			exit(-1)

		possible_modules = os.walk('modules').next()[1]
		for mod in possible_modules:
			logger.debug('Possible mod: {0}'.format(mod))


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

if __name__ == '__main__':
	simulation = Swarm_AI()