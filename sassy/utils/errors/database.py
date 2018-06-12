from sassy.utils.logger import logger


class SassyError(Exception):
    def __init__(self, msg, base_exception):
        super(SassyError, self).__init__(f"{msg}: {base_exception}")
        self.base_exception = base_exception
        logger.exception(self.base_exception)


class DatabaseConnectionError(SassyError):
    pass

