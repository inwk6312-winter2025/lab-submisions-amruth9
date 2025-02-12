import logging
logging.basicConfig(level=logging.INFO, format= '%(asctime)s - %(message)s')
a = 5
b = 0
try:
    c = a / b
except Exception as e:
    logging.exception("Exception occurred")
