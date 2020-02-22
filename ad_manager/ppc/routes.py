from flask import Blueprint, jsonify, render_template, request

mod = Blueprint('espn', __name__)

@mod.route('/home')
def home():
  return render_template('index.html')
