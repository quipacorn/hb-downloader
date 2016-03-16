__author__ = "Joel Pedraza"
__copyright__ = "Copyright 2014, Joel Pedraza"
__license__ = "MIT"


class HumbleException(Exception):
    """ An unspecified error occurred. """

    def __init__(self, *args, **kwargs):
        """
            Parameterized constructor for HumbleException.

            :param list args: (optional) Extra positional args to pass to the request.
            :param dict kwargs: (optional) Extra keyword args to pass to the request.
        """
        super(HumbleException, self).__init__(*args, **kwargs)