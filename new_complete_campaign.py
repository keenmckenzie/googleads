from googleads import adwords
import campaign_add, add_adgroup, keyword_add, ad_add

CAMPAIGN_NAME = 'Kamryn Demo Test Campaign'

if __name__ == '__main__':
    # Initialize client object.
    adwords_client = adwords.AdWordsClient.LoadFromStorage('/Users/keenan/dev/ads/auth/googleads.yaml')

    campaign_id = campaign_add.main(adwords_client, CAMPAIGN_NAME)
    adgroup_id = add_adgroup.main(adwords_client, campaign_id, CAMPAIGN_NAME + " - AdGroup 1")
    keyword_add.main(adwords_client, adgroup_id, "Keyword 1", "EXACT", "www.example.com")
    ad_add.main(adwords_client, adgroup_id, "Headline 1", "Headline 2", "This is the description",
                "This is the second.", "https://www.example.com")
