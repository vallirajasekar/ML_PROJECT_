import sys
#from logger import logging
from src.logger import logging


def error_message_detail(error, error_detail: sys):
    """
    Extracts error details such as filename, line number, and error message.
    """
    _, _, exc_tb = sys.exc_info()  # Use sys.exc_info() directly
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in Python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error, error_detail: sys):
        """
        Custom Exception class that provides detailed error messages.
        """
        super().__init__(str(error))  # Pass the original error message
        self.error_message = error_message_detail(error, error_detail)  # Pass exception, not string

    def __str__(self):
        return self.error_message

# if __name__ == "__main__":
#     try:
#         a = 1 / 0
#         logger.info('This line will not execute due to exception above')
#     except Exception as e:
#         raise CustomException(e, sys)
