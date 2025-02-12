import logging
# logging.basicConfig(level=logging.DEBUG)
# logging.critical('This will get logged')
logging.basicConfig(filename='app.log',
filemode='a',
format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')
