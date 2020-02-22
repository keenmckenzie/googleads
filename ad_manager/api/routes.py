from googleads import adwords
from flask import Blueprint, jsonify, render_template, request
from ad_manager.api.get_campaigns import main

mod = Blueprint('api', __name__)

@mod.route('/get_campaigns')
def campaigns():
   adwords_client = adwords.AdWordsClient.LoadFromStorage('/Users/keenan/dev/ads/auth/googleads.yaml')
   campaigns = main(adwords_client)
   return campaigns
