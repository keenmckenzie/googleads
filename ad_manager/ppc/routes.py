from flask import Blueprint, jsonify, render_template, request

mod = Blueprint('espn', __name__)


@mod.route('/home')
def home():
    return render_template('index.html')


@mod.route('/campaigns')
def campaigns():
    return render_template('campaigns.html')


@mod.route('/new_campaign')
def new_campaign():
    return render_template('new_campaign_form.html')
