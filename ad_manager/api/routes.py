from googleads import adwords
from flask import Blueprint
from ad_manager.api.campaign_management.get_campaigns import get_campaigns

mod = Blueprint('api', __name__)


@mod.route('/get_campaigns')
def campaigns():
    adwords_client = adwords.AdWordsClient.LoadFromStorage('/Users/keenan/dev/ads/auth/googleads.yaml')
    campaign_list = get_campaigns(adwords_client)
    return campaign_list
