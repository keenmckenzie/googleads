from googleads import adwords

campaign_id = '9366062070'
status = 'ENABLED'


def update_status(client, campaign_status):
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
        print('Campaign with name "%s" and id "%s" is now "%s".'
              % (campaign['name'], campaign['id'], campaign['status']))


if __name__ == '__main__':
    adwords_client = adwords.AdWordsClient.LoadFromStorage('/Users/keenan/dev/ads/auth/googleads.yaml')
    update_status(adwords_client, status)
