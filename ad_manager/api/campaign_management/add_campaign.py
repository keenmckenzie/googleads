import datetime
import uuid
from googleads import adwords

CAMPAIGN_NAME = 'Another Test Campaign'


def add_campaign(client, campaign_name):
    # Initialize appropriate services.
    campaign_service = client.GetService('CampaignService', version='v201809')
    budget_service = client.GetService('BudgetService', version='v201809')

    # Create a budget ID with no name, specify that it is not a shared budget
    # Establish budget as a micro amount
    budget = {
        'name': None,
        'isExplicitlyShared': 'false',
        'amount': {
            'microAmount': 80000000
        }
    }

    budget_operations = [{
        'operator': 'ADD',
        'operand': budget
    }]

    budget_id = budget_service.mutate(budget_operations)['value'][0]['budgetId']

    # Construct operations and add campaigns.
    operations = [{
        'operator': 'ADD',
        'operand': {
            'name': campaign_name,
            # Recommendation: Set the campaign to PAUSED when creating it to
            # stop the ads from immediately serving. Set to ENABLED once you've
            # added targeting and the ads are ready to serve.
            'status': 'ENABLED',
            'advertisingChannelType': 'SEARCH',
            'biddingStrategyConfiguration': {
                'biddingStrategyType': 'MANUAL_CPC',
            },
            'endDate': (datetime.datetime.now() +
                        datetime.timedelta(365)).strftime('%Y%m%d'),
            'budget': {
                'budgetId': budget_id
            },
            'networkSetting': {
                'targetGoogleSearch': 'true',
                'targetSearchNetwork': 'true',
                'targetContentNetwork': 'false',
                'targetPartnerSearchNetwork': 'false'
            }
        }
    }
    ]
    campaigns = campaign_service.mutate(operations)

    # Display results.
    for campaign in campaigns['value']:
        print('Campaign with name "%s" and id "%s" was added.'
              % (campaign['name'], campaign['id']))
        return campaign['id']

if __name__ == '__main__':
    # Initialize client object.
    adwords_client = adwords.AdWordsClient.LoadFromStorage('/Users/keenan/dev/googleads-python-lib/googleads.yaml')

    add_campaign(adwords_client, CAMPAIGN_NAME)
