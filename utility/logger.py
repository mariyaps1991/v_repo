import logging


class Logging:

    logger = logging.getLogger("billing_system")

    def __init__(self):
        # initialize logging and configuration
        Logging.logger.setLevel(logging.DEBUG)      # INFO, WARN, ERROR, CRITICAL
        FORMAT = "%(asctime)s %(levelname)s %(message)s"
        logging.basicConfig(format=FORMAT)

        # add file handler if logs should be in a file
        fh = logging.FileHandler("debug.log")
        formatter = logging.Formatter(FORMAT)
        fh.setFormatter(formatter)
        Logging.logger.addHandler(fh)

    def get_logger(self):
        return Logging.logger


if __name__ == '__main__':
    obj = Logging()
    logger = obj.get_logger()
    logger.info("This is working fine as info")
    logger.error("I have found an error at this line")
    logger.warning("We found the error but impact is minimal.")
    logger.critical("Oh no.. System/deamon is corrupted.")

