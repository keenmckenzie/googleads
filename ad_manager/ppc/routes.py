from flask import Blueprint, jsonify, render_template, request

mod = Blueprint('web', __name__)


@mod.route('/')
def index():
    return render_template('index.html')


@mod.route('/home')
def home():
    return render_template('index.html')


@mod.route('/campaigns')
def campaigns():
    return render_template('campaigns.html')


@mod.route('/dynamic_campaign')
def new_campaign():
    return render_template('new_campaign_form.html')


@mod.route('/update_target')
def update_target_form():
    return render_template('update_target_form.html')
