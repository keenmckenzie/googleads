from googleads import adwords
from flask import Blueprint, request, render_template
from ad_manager.api.campaign_management.get_campaigns import get_campaigns
from ad_manager.api.campaign_management.set_campaign_status import update_status
from ad_manager.api.campaign_management.new_complete_campaign import build_campaign
from ad_manager.api.campaign_management.new_dynamic import dynamic_campaign
from ad_manager.api.campaign_management.Campaign import Campaign
from ad_manager.api.campaign_management.update_troas_target_campaign import update_target

mod = Blueprint('api', __name__)


@mod.route('/get-campaigns')
def campaigns():
    adwords_client = adwords.AdWordsClient.LoadFromStorage('/Users/keenan/dev/googleads/auth/googleads.yaml')
    campaign_list = get_campaigns(adwords_client)
    return campaign_list


@mod.route('update-campaign-status')
def update_campaign_status():
    status = request.args.get('status')
    campaign_id = request.args.get('id')
    adwords_client = adwords.AdWordsClient.LoadFromStorage('/Users/keenan/dev/googleads/auth/googleads.yaml')
    update_status(adwords_client, status, campaign_id)
    return {"status": "success"}


@mod.route('/new-campaign')
def new_campaign():
    campaign_name = request.args.get('name')
    adwords_client = adwords.AdWordsClient.LoadFromStorage('/Users/keenan/dev/googleads/auth/googleads.yaml')
    build_campaign(adwords_client, campaign_name)
    return render_template('campaigns.html')


@mod.route('/dynamic-campaign')
def new_dynamic():
    event_name = request.args.get('name')
    adwords_client = adwords.AdWordsClient.LoadFromStorage('/Users/keenan/dev/googleads/auth/googleads.yaml')
    dynamic_campaign(adwords_client, event_name)
    return render_template('campaigns.html')


@mod.route('/update_target')
def update_target():
    new_target = int(request.args.get('target'))/100
    campaign_id = request.args.get('campaignId')
    campaign = Campaign(campaign_id)
    adwords_client = adwords.AdWordsClient.LoadFromStorage('/Users/keenan/dev/googleads/auth/googleads.yaml')
    campaign.update_target(adwords_client, new_target)
    return render_template('campaigns.html')
    ##return "Update target to: " + str(new_target)
