from .db import Dbcon
from random import randint
import bcrypt

#import app.flasksub as appfunctions
from app import flasksub as appfunctions

db = Dbcon()

def get_user_status(username):
  """ returns status of given user
  Args:
    username (str)
  Returns (only one):
    userstatus (int) otherwise False
      0 = not registered
      1 = registered
  """
  if not username: return False

  sql = "SELECT status FROM user WHERE email = '{}'".format(username)
  try:
    userstatus = db.get(sql)[0]['status']
  except: 
    return False

  return userstatus


def get_user_hash(username):
  """ returns password has of given user
  Args:
    username (str)
  Returns (only one):
    the hash (str) otherwise False
  """
  if not username: return False

  sql = "SELECT hash FROM user WHERE email = '{}'".format(username)
  try:
      hash_from_db = db.get(sql)[0]['hash']
  except IndexError:
      return False

  return hash_from_db


def get_user_mysqlid(username):
  """ returns userid of a given user
  Args:
    username (str)
  Returns:
    user_id (int) otherwise False 
  """
  if not username: return False

  sql = "SELECT id FROM user WHERE email = '{}'".format(username)
  try:
    user_id = db.get(sql)[0]['id']
  except:
    return False

  return user_id


def create_user(username, pwhash):
  """ creates a user with given user and password hash
  Args:
    username (str)
    pwhash (str)
  Returns:
    True for success or False for errors
  """
  if not username or not pwhash: return False

  sql = "INSERT INTO user (email, hash) VALUES('{}', '{}')".format(username, pwhash)
  try:
    db.set(sql)
  except:
    return False

  return True


def create_user_activationlink(username):
  """ creates an activation link for registering an user account
  Args:
    username (str)
  Returns:
    link (str) or False for errors
  """
  if not username: return False

  user_id_mysql = get_user_mysqlid(username)
  if not user_id_mysql:
    return False

  link = username.replace('@', '_') + '_' + str(randint(1000, 10000000))
  sql = "INSERT INTO activationlink (userid, link) VALUES('{}', '{}')".format(user_id_mysql, link)

  try:
    db.set(sql)
  except:
    return False

  return link


def register_user(link):
  """ registers users after calling the activation link
  Args:
    - link (str)
  Returns:
    True for success or False for all errors

  """
  if not link: return False
  if not appfunctions.check_valid_activationlink(link): return False

  sql = "SELECT userid FROM activationlink WHERE link ='{}'".format(link)
  try:
    user = db.get(sql)[0]['userid']
  except:
    return False

  sql_update = "UPDATE user SET status=1 WHERE id = '{}'".format(user)
  sql_remove = "DELETE FROM activationlink WHERE userid = '{}'".format(user)

  try: 
    db.set(sql_update)
    db.set(sql_remove)
  except:
    return False

  return True






