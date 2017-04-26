from flask import Flask, request, Response, make_response, jsonify
import bcrypt
import json

from mysql import function as dbfunctions
from app import flasksub as appfunctions

# import config
with open('config.json') as json_config:
    config = json.load(json_config)

salt = bytes(config["security"]["salt"], 'utf-8')

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register_user():

  if not request.form["username"] and request.form["password"]:
    return make_response(jsonify({'status': 'error','msg': 'no valid data for registration'}), 404)

  user = request.form["username"]
  
  # hash password
  try:
    hashed = bcrypt.hashpw(request.form["password"].encode(), salt).decode()
  except:
    return make_response(jsonify({'status': 'error','msg': 'could not create user, please check your password'}), 404)

  # create user in database
  if not dbfunctions.create_user(user, hashed):
    return make_response(jsonify({'status': 'error','msg': 'could not create user'}), 404)


  # create and log activation link
  link = dbfunctions.create_user_activationlink(user)
  if not link:
    return make_response(jsonify({'status': 'error','msg': 'could not create activation link'}), 404)

  print('XXX ACTIVATION LINK:', request.url_root + 'activationlink/' + link)

  return make_response(jsonify({'status': 'success','msg': 'user created'}), 200)
  


@app.route('/activationlink/<link>', methods=['GET'])
def activationlink(link):
  if dbfunctions.register_user(link):
    return make_response(jsonify({'status': 'success','msg': 'successfully registered account'}), 200)
  else:
    return make_response(jsonify({'status': 'error','msg': 'failed to register account, please check your link'}), 404)



@app.route('/data', methods=['GET'])
def data():

  auth = request.authorization

  if not auth or not appfunctions.check_auth(auth.username, auth.password, salt):
    return appfunctions.authenticate()
  else:
    return make_response(jsonify({'status': 'success','msg': 'hidden sauce'}), 200)


if __name__ == '__main__':
  app.run(debug = True, host = '0.0.0.0')



