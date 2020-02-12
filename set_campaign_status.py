from googleads import adwords

campaign_id = '9328039918'
status = 'ENABLED'


def main(client, campaign_status):
    # Initialize appropriate service.
    campaign_service = client.GetService('CampaignService', version='v201809')
    # Construct operations and add campaigns.
    operations = [{
        'operator': 'SET',
        'operand': {
            'id': campaign_id,
            'status': campaign_status
        }
    }]
    campaigns = campaign_service.mutate(operations)

    for campaign in campaigns['value']:
        print('Campaign with name "%s" and id "%s" was modified.'
              % (campaign['name'], campaign['id']))


if __name__ == '__main__':
    adwords_client = adwords.AdWordsClient.LoadFromStorage('/Users/keenan/dev/ads/auth/googleads.yaml')
    main(adwords_client, status)
