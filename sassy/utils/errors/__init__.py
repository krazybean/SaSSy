class SassyError(Exception):
    def __init__(self, msg, base_exception):
        super(SassyError, self).__init__(f"{msg}: {base_exception}")
        self.base_exception = base_exception
        logger.exception(self.base_exception)


# Import attempts since these aren't to be used after the baseClass is built
try:
    from sassy.utils.errors.database import *
    from sassy.utils.errors.communications import *
except ImportError as e:
    msg = "Error import error modules"
    raise SassyError(msg, e)

