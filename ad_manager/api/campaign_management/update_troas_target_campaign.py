from googleads import adwords
import time

CAMPAIGN_ID = 13777802
TARGET_ROAS = 7.5


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
                }
            }
        }
    }]
    campaigns = campaign_service.mutate(operations)
    for campaign in campaigns['value']:
        print('Campaign with name "%s" and id "%s" is now "%s".'
              % (campaign['name'], campaign['id'], campaign['biddingStrategyConfiguration']))


def get_target(client, campaign_id):
    today = time.strftime('%Y%m%d', time.localtime())
    selector = {
        'fields': ['Id', 'Name', 'Status', 'BudgetId', 'Amount', 'BiddingStrategyType', 'TargetRoas'],
        'predicates': [
            {
                'field': 'Status',
                'operator': 'NOT_EQUALS',
                'values': ['REMOVED']
            },
            {
                'field': 'Id',
                'operator': 'EQUALS',
                'values': campaign_id
            }
        ],
        'dateRange': {
            'min': today,
            'max': today
        }

    }
    campaigns = client.GetService('CampaignService').get(selector)
    if int(campaigns['totalNumEntries']) > 0:
        return campaigns['entries']
    else:
        return None


if __name__ == '__main__':
    adwords_client = adwords.AdWordsClient.LoadFromStorage('/Users/keenan/dev/googleads/auth/googleads.yaml')
    update_target(adwords_client, CAMPAIGN_ID, TARGET_ROAS)
    ##print(campaign_info)
    ##print(campaign_info[0]['biddingStrategyConfiguration']['biddingScheme']['targetRoas'])
