"""
This module contains the Calculator class for performing four arithmetic operations.
"""


class Calculator:
    """
    This class is a simple calculator that performs four basic arithmetic operations on two numbers,
    which are passed as arguments to the corresponding methods of the class.
    """

    @staticmethod
    def add(first_addition, second_addition):
        """
        :param first_addition: first addition
        :type first_addition: float or integer
        :param second_addition: second addition
        :type second_addition: float or integer
        :return: add two numbers
        :rtype: float or integer
        """
        return first_addition + second_addition

    @staticmethod
    def subtract(reduction, subtractor):
        """
        :param reduction: reduction
        :type reduction: float or integer
        :param subtractor: subtractor
        :type subtractor: float or integer
        :return: add two numbers
        :rtype: float or integer
        """
        return reduction - subtractor

    @staticmethod
    def multiply(first_multiplier, second_multiplier):
        """
        :param first_multiplier: first multiplier
        :type first_multiplier: float or integer
        :param second_multiplier: second multiplier
        :type second_multiplier: float or integer
        :return: multiply two numbers
        :rtype: float or integer
        """
        return first_multiplier * second_multiplier

    @staticmethod
    def divide(divided, divider):
        """
        :param divided: divided
        :type divided: float or integer
        :param divider: divider
        :type divider: float or integer
        :return: add two numbers
        :rtype: float
        """
        try:
            return divided / divider
        except ZeroDivisionError:
            return 'Divider is zero'
