from googleads import adwords

CAMPAIGN_ID = '9328039918'


def main(client, campaign_id):
    # Initialize appropriate service.
    campaign_service = client.GetService('CampaignService', version='v201809')
    # Construct operations and add campaigns.
    operations = [{
        'operator': 'SET',
        'operand': {
            'id': campaign_id,
            'biddingStrategyConfiguration': {
                'biddingStrategyType': 'MAXIMIZE_CONVERSIONS',
                'biddingScheme': {
                    'xsi_type': 'MaximizeConversionsBiddingScheme'
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
    main(adwords_client, CAMPAIGN_ID)
