import logging

# create a logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)      # INFO, WARN, ERROR, CRITICAL

FORMAT = "%(asctime)s %(levelname)s %(message)s"
logging.basicConfig(format=FORMAT)

# log the information (only to console)
logger.info("My logging mechanism")
logger.error("There is no line after this.")

# add file handler if logs should be in a file
fh = logging.FileHandler("debug.log")
formatter = logging.Formatter(FORMAT)
fh.setFormatter(formatter)
logger.addHandler(fh)

# log the information
logger.info("Line after adding file handler")
logger.error("There is no line after this.")

