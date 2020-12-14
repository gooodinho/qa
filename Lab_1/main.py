# ZeroDivisionError - Raised when the second argument of a division or modulo operation is zero.
# KeyError - Raised when a mapping (dictionary) key is not found in the set of existing keys.
# TypeError - Raised when an operation or function is applied to an object of inappropriate type.


class ExceptionManager:
    def __init__(self):
        self.CRITICAL_ERRORS = (ZeroDivisionError, KeyError, TypeError)
        self.critical = 0
        self.non_critical = 0

    def check_critical(self, exception):
        if issubclass(exception, Exception) and exception in self.CRITICAL_ERRORS:
            return True
        else:
            return False

    def count_exceptions(self, exception):
        if self.check_critical(exception):
            self.critical += 1
        else:
            self.non_critical += 1
