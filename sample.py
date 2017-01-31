import logging, sys
from logging import config

#* logging.debug()
#* logging.info()
#* logging.warning()
#* logging.error()
#* logging.critical()

#logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('coder')
hdlr = logging.FileHandler('coder.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.WARNING)
logger.error('We have a problem')
logger.info('While this is just chatty')
