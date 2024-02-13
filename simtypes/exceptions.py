class SimException(Exception):
    """
    Basic exception type for simplesim apps.
    """
    def __init__(self, errno, msg):
        self.args = (errno, msg)
        self.errno = errno
        self.errmsg = msg


class SimValueError(SimException):
    """
    Exception type for type errors in app.
    """
    def __init__(self, errno, msg):
        super().__init__(errno, msg)
