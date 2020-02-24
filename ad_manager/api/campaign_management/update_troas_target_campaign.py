from googleads import adwords

CAMPAIGN_ID = '9328039918'
TARGET_ROAS = 600


def update_target(client, campaign_id, target_roas):
    # Initialize appropriate service.
    campaign_service = client.GetService('CampaignService', version='v201809')
    # Construct operations and add campaigns.
    operations = [{
        'operator': 'SET',
        'operand': {
            'id': campaign_id,
            'biddingStrategyConfiguration': {
                'biddingStrategyType': 'TARGET_ROAS',
                'biddingScheme': {
                    'xsi_type': 'TargetRoasBiddingScheme',
                    'targetRoas': target_roas,
                    'bidCeiling': 10,
                    'bidFloor': 1
                }
            }
        }
    }]
    campaigns = campaign_service.mutate(operations)

    for campaign in campaigns['value']:
        print('Campaign with name "%s" and id "%s" is now "%s".'
              % (campaign['name'], campaign['id'], campaign['biddingStrategyConfiguration']))


if __name__ == '__main__':
    adwords_client = adwords.AdWordsClient.LoadFromStorage('/Users/keenan/dev/ads/auth/googleads.yaml')
    update_target(adwords_client, CAMPAIGN_ID, TARGET_ROAS)
