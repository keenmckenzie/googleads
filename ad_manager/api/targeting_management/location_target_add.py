from googleads import adwords

CAMPAIGN_ID = '9366062070'


def main(client, campaign_id):
    campaign_criterion_service = client.GetService(
        'CampaignCriterionService', version='v201809')

    california = {
        'xsi_type': 'Location',
        'id': '21137'
    }
    mexico = {
        'xsi_type': 'Location',
        'id': '2484'
    }

    english = {
        'xsi_type': 'Language',
        'id': '1000'
    }
    spanish = {
        'xsi_type': 'Language',
        'id': '1003'
    }

    criteria = [california, mexico, english, spanish]

    # Create operations
    operations = []
    for criterion in criteria:
        operations.append({
            'operator': 'ADD',
            'operand': {
                'campaignId': campaign_id,
                'criterion': criterion
            }
        })

    # Make the mutate request.
    result = campaign_criterion_service.mutate(operations)

    # Display the resulting campaign criteria.
    for campaign_criterion in result['value']:
        print('Campaign criterion with campaign id "%s", criterion id "%s", '
              'and type "%s" was added.'
              % (campaign_criterion['campaignId'],
                 campaign_criterion['criterion']['id'],
                 campaign_criterion['criterion']['type']))


if __name__ == '__main__':
    adwords_client = adwords.AdWordsClient.LoadFromStorage('/Users/keenan/dev/ads/auth/googleads.yaml')

    main(adwords_client, CAMPAIGN_ID)
