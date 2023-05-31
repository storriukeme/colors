import logging 

logFormatter = logging.Formatter(fmt='%(asctime)s:%(name)s:%(threadName)s:%(levelname)s:%(message)s')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)
consoleHandler.setFormatter(logFormatter)

logger.addHandler(consoleHandler)
