from googleads import adwords
import os
from flask import Blueprint, request, render_template, redirect, jsonify
from ad_manager.api.campaign_management.get_campaigns import get_campaigns, get_mlb_campaigns
from ad_manager.api.campaign_management.set_campaign_status import update_status
from ad_manager.api.campaign_management.new_complete_campaign import build_campaign
from ad_manager.api.campaign_management.new_dynamic import dynamic_campaign
from ad_manager.api.campaign_management.Campaign import Campaign
from auth.user_auth import username, password, secret_key
import datetime
import jwt
from functools import wraps
from ad_manager.api.campaign_management.update_troas_target_campaign import update_target

mod = Blueprint('api', __name__)
cwd = os.getcwd()
googleads_path = cwd + '/auth/googleads.yaml'


@mod.route('/get-campaigns')
def campaigns():
    adwords_client = adwords.AdWordsClient.LoadFromStorage(googleads_path)
    campaign_list = get_campaigns(adwords_client)
    return campaign_list


@mod.route('/mlb-campaigns')
def mlb_campaigns():
    adwords_client = adwords.AdWordsClient.LoadFromStorage(googleads_path)
    campaign_list = get_mlb_campaigns(adwords_client)
    return campaign_list


@mod.route('update-campaign-status')
def update_campaign_status():
    status = request.args.get('status')
    campaign_id = request.args.get('id')
    adwords_client = adwords.AdWordsClient.LoadFromStorage(googleads_path)
    update_status(adwords_client, status, campaign_id)
    return {"status": "success"}


@mod.route('/new-campaign')
def new_campaign():
    campaign_name = request.args.get('name')
    adwords_client = adwords.AdWordsClient.LoadFromStorage(googleads_path)
    build_campaign(adwords_client, campaign_name)
    return render_template('campaigns.html')


@mod.route('/dynamic-campaign')
def new_dynamic():
    event_name = request.args.get('name')
    adwords_client = adwords.AdWordsClient.LoadFromStorage(googleads_path)
    dynamic_campaign(adwords_client, event_name)
    return render_template('campaigns.html')


@mod.route('/update_target')
def update_target_api():
    new_target = int(request.args.get('target')) / 100
    campaign_id = request.args.get('campaignId')
    campaign = Campaign(campaign_id)
    adwords_client = adwords.AdWordsClient.LoadFromStorage(googleads_path)
    campaign.update_target(adwords_client, new_target)
    ##return render_template('update_target_form.html')
    return redirect('https://fast-refuge-34078.herokuapp.com/update_target')
    ##return "Update target to: " + str(new_target)


@mod.route('authorization', methods=['POST'])
def authorize():
    json = request.get_json()
    if username == json['username'] and password == json['password']:
        return {"auth": True}
    else:
        return {"auth": False}


@mod.route('/login', methods=['POST'])
def login():
    json = request.get_json()
    username_input = json['username']
    password_input = json['password']
    if username == json['username'] and password == json['password']:
        try:
            token = jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=30)}, secret_key)
            print(token)
            return jsonify({'token': str(token)}), 200
        except Exception as e:
            print(e)
            return jsonify({'error': "Server error"})
    else:
        return jsonify({'error': 'Invalid Username & Password'}), 401


@mod.route('/bulk_update_target', methods=['PUT'])
def bulk_update_target_api():
    json = request.get_json()
    adwords_client = adwords.AdWordsClient.LoadFromStorage(googleads_path)
    campaign_array = json['campaigns']
    for campaign in campaign_array:
        campaign_object = Campaign(campaign['id'])
        new_target = float(campaign['targetRoas'])
        print(str(campaign_object.campaign_id) + ": " + str(new_target))
        campaign_object.update_target(adwords_client, new_target)
    return {"result": "success"}
