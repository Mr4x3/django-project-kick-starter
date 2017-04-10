# Python Imports
import re

# Django Imports
from django.core.exceptions import ValidationError

# Third Party Django Imports

# Inter App Imports

# Local Imports


def name_validator(data):
    """
    validates name by matching to ^[a-zA-Z\s]+$ regex
    """

    if not re.match('^[a-zA-Z\.\s]+$', data):
        raise ValidationError('{0} is not a valid name'.format(data))
    return data


def mobile_number_validator(data):
    """
    validates mobile number by matching to ^\d{5,20}$ regex
    """

    if not re.match('^\d{5,20}$', data):
        raise ValidationError('{0} is not a valid mobile number'.format(data))
    return data
