from googleads import adwords
from flask import Blueprint, request
from ad_manager.api.campaign_management.get_campaigns import get_campaigns
from ad_manager.api.campaign_management.set_campaign_status import update_status
from ad_manager.api.campaign_management.new_complete_campaign import build_campaign

mod = Blueprint('api', __name__)


@mod.route('/get-campaigns')
def campaigns():
    adwords_client = adwords.AdWordsClient.LoadFromStorage('/Users/keenan/dev/ads/auth/googleads.yaml')
    campaign_list = get_campaigns(adwords_client)
    return campaign_list


@mod.route('update-campaign-status')
def update_campaign_status():
    status = request.args.get('status')
    campaign_id = request.args.get('id')
    adwords_client = adwords.AdWordsClient.LoadFromStorage('/Users/keenan/dev/ads/auth/googleads.yaml')
    update_status(adwords_client, status, campaign_id)
    return {"status": "success"}


@mod.route('new-campaign')
def new_campaign():
    campaign_name = request.args.get('name')
    adwords_client = adwords.AdWordsClient.LoadFromStorage('/Users/keenan/dev/ads/auth/googleads.yaml')
    build_campaign(adwords_client, campaign_name)
    return {"status": campaign_name + " built successfully"}
