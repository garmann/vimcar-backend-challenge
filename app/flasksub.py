import bcrypt
from flask import Response
import re

from mysql import function as dbfunctions

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})


def check_account_registered(user):
    """ This function is called to check if an account is fully registered
        see dbfunctions.get_user_status() for status legend
    Args:
        user (string) means username
    Returns:
        True for account is registered and False for not registered or all errors
    """
    if not user: return False

    userstatus = dbfunctions.get_user_status(user)
    if not userstatus:
        return False
    elif userstatus == 1:
        return True
    else:
        return False


def check_auth(user, password, salt):
    """This function is called to check if a username /
    password combination is valid.
    Args:
        user (str) means username
        password (str)
        salt (str) salt from config
    Returns:
        True if login is okay and False if data is wrong or all errors
    """
    if not user or not password or not salt: return False

    if not check_valid_email(user): return False

    if not check_valid_password(password): return False

    hashed = bcrypt.hashpw(password.encode(), salt).decode()
    hash_from_db = dbfunctions.get_user_hash(user)

    if hashed == hash_from_db and check_account_registered(user):
      return True
    else:
      return False


def check_valid_email(input):
    # simple validation for sql injection
    if re.match('[a-zA-Z0-9@\-_.]*$', input) and len(input) > 5 and len(input) < 150:
        return True
    else:
        return False


def check_valid_password(input):
    # simple validation for sql injection
    if re.match('[a-zA-Z0-9\-_.]*$', input) and len(input) > 2 and len(input) < 150:
        return True
    else:
        return False


def check_valid_activationlink(input):
    # simple validation for sql injection
    if re.match('[a-zA-Z0-9\-_.]*$', input) and len(input) > 5 and len(input) < 150:
        return True
    else:
        return False
