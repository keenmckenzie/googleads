from googleads import adwords

PAGE_SIZE = 100


def get_campaigns(client):
    campaign_list = []
    campaign_data = {}
    # Initialize appropriate service.
    campaign_service = client.GetService('CampaignService', version='v201809')
    # Construct selector and get all campaigns.
    offset = 0
    selector = {
        'fields': ['Id', 'Name', 'Status', 'BudgetId', 'Amount', 'BiddingStrategyType', 'BiddingStrategyId',
                   'BiddingStrategyName', 'TargetRoas'],
        'predicates': [
            {
                'field': 'Status',
                'operator': 'EQUALS',
                'values': ['ENABLED']
            },
            {
                'field': 'BiddingStrategyType',
                'operator': 'EQUALS',
                'values': 'TARGET_ROAS'
            },
            {
                'field': 'BiddingStrategyName',
                'operator': 'DOES_NOT_CONTAIN',
                'values': 'tROAS'
            },
            {
                'field': 'BiddingStrategyName',
                'operator': 'DOES_NOT_CONTAIN',
                'values': 'OSBO'
            }
        ]
    }
    campaign_selector = client.GetService('CampaignService').get(selector)
    if int(campaign_selector['totalNumEntries']) > 0:
        campaigns = campaign_selector['entries']
        for campaign in campaigns:
            targetRoas = campaign['biddingStrategyConfiguration']['biddingScheme']['targetRoas']
            campaign_data = {
                "name": campaign['name'],
                "status": campaign['status'],
                "id": campaign['id'],
                "targetRoas": str(targetRoas * 100) + '%'
            }
            campaign_list.append(campaign_data)
        return {'campaigns': campaign_list}
    else:
        print('No campaigns were found.')


def get_campaign(client, campaign_id):
    ind_selector = {
        'fields': ['Id', 'Name', 'Status', 'BudgetId', 'Amount', 'BiddingStrategyType', 'BiddingStrategyId',
                   'BiddingStrategyName', 'TargetRoas'],
        'predicates': [
            {
                'field': 'Id',
                'operator': 'EQUALS',
                'values': campaign_id
            }
        ]
    }
    ind_campaign_selector = client.GetService('CampaignService').get(ind_selector)
    if int(ind_campaign_selector['totalNumEntries']) > 0:
        campaigns = ind_campaign_selector['entries']
        for campaign in campaigns:
            print(campaign)
            targetRoas = campaign['biddingStrategyConfiguration']['biddingScheme']['targetRoas']
            campaign_data = {
                "name": campaign['name'],
                "status": campaign['status'],
                "id": campaign['id'],
                "targetRoas": str(targetRoas * 100) + '%'
            }
        return {'campaigns': campaign_data}
    else:
        print('No campaigns were found.')


if __name__ == '__main__':
    adwords_client = adwords.AdWordsClient.LoadFromStorage('/Users/keenan/dev/googleads/auth/googleads.yaml')
    campaigns = get_campaign(adwords_client, '13777802')
    ##campaigns = get_campaigns(adwords_client)
    print(campaigns)
