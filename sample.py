import logging, sys
from logging import config

#* logging.debug()
#* logging.info()
#* logging.warning()
#* logging.error()
#* logging.critical()

logging.basicConfig(level=logging.INFO)

logging.error('We have a problem')
logging.info('While this is just chatty')
