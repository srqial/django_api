import logging

logger = logging.getLogger("mylogger")

def exception(error_message, return_value={}, exceptions=Exception):
    def inner_function(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exceptions as e:
                logger.error(e, exc_info=True)
                logger.error(error_message)
                return return_value
        return wrapper
    return inner_function