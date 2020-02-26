from googleads import adwords
from ad_manager.api.keyword_management import keyword_add
from ad_manager.api.ad_management import ad_add
from ad_manager.api.adgroup_management import add_adgroup
from ad_manager.api.campaign_management import add_campaign

def dynamic_campaign(client, event_name, num_adgroups=2, num_keywords=3):
    campaign_name = event_name + " - Dynamic"
    campaign_id = add_campaign.add_campaign(client, campaign_name)
    adgroups = {
          "ExactTargeted": ["tickets", "tix", "ticket", "concert ticket"],
          "General": ["", "show", "2020"],
          "Tour": ["tour", "tour dates", "tour 2020"]
    }

    for adgroup in adgroups:
        adgroup_id = add_adgroup.main(client, campaign_id, event_name + " - Dynamic_" + adgroup)
        keywords = adgroups[adgroup]
        for keyword in keywords:
            keyword_add.main(client, adgroup_id, event_name + " " + keyword
                             , "EXACT", "www.example.com/" + event_name.replace(" ", "-"))
            keyword_add.main(client, adgroup_id, event_name + " " +  keyword
                             , "PHRASE", "www.example.com/" + event_name.replace(" ", "-"))
            keyword_add.main(client, adgroup_id, event_name + " " +  keyword
                             , "BROAD", "www.example.com/" + event_name.replace(" ", "-"))
        ad_add.main(client, adgroup_id, event_name, " Dynamic Ad", "Description of the ad",
                    event_name + " description two.", "https://www.example.com/"+event_name.replace(" ", "-"))
"""
    while adgroup_count <= num_adgroups:
        adgroup_id = add_adgroup.main(client, campaign_id, campaign_name + " - AdGroup " + str(adgroup_count + 1))
        keyword_count = 0
        while keyword_count <= num_keywords:
            keyword_add.main(client, adgroup_id, "Keyword " + str(keyword_count + 1), "EXACT", "www.example.com")
            keyword_count += 1
        adgroup_count += 1
        ad_add.main(client, adgroup_id, "Headline 1", "Headline 2", "This is the description",
                    "This is the second.", "https://www.example.com")
"""

if __name__ == '__main__':
    # Initialize client object.
    adwords_client = adwords.AdWordsClient.LoadFromStorage('/Users/keenan/dev/googleads/auth/googleads.yaml')
    dynamic_campaign(adwords_client, "Test Event")
