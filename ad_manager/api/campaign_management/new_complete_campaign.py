from googleads import adwords
import add_adgroup, keyword_add, ad_add
from ad_manager.api.campaign_management import add_campaign

CAMPAIGN_NAME = 'Kamryn Demo Test Campaign'


def build_campaign(client, campaign_name, num_adgroups=2, num_keywords=3):
    campaign_id = add_campaign.add_campaign(client, campaign_name)
    adgroup_count = 0
    while adgroup_count <= num_adgroups:
        adgroup_id = add_adgroup.main(client, campaign_id, campaign_name + " - AdGroup " + str(adgroup_count + 1))
        keyword_count = 0
        while keyword_count <= num_keywords:
            keyword_add.main(client, adgroup_id, "Keyword " + str(keyword_count + 1), "EXACT", "www.example.com")
            keyword_count += 1
        adgroup_count += 1
        ad_add.main(client, adgroup_id, "Headline 1", "Headline 2", "This is the description",
                    "This is the second.", "https://www.example.com")


if __name__ == '__main__':
    # Initialize client object.
    adwords_client = adwords.AdWordsClient.LoadFromStorage('/Users/keenan/dev/ads/auth/googleads.yaml')
    build_campaign(adwords_client, CAMPAIGN_NAME)
