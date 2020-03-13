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
        'fields': ['Id', 'Name', 'Status', 'BudgetId', 'Amount', 'BiddingStrategyType', 'BiddingStrategyId', 'BiddingStrategyName', 'TargetRoas'],
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
                "targetRoas": str(targetRoas*100) + '%'
            }
            campaign_list.append(campaign_data)
        return {'campaigns': campaign_list}
    else:
        print('No campaigns were found.')

    '''
    selector = {
        'fields': ['Id', 'Name', 'Status', 'BudgetId', 'Amount', 'BiddingStrategyType', 'TargetRoas'],
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
            }
        ],
        'paging': {
            'startIndex': str(offset),
            'numberResults': str(PAGE_SIZE)
        }
    }

    more_pages = True
    while more_pages:
        page = campaign_service.get(selector)

        # Display results.
        if 'entries' in page:
            for campaign in page['entries']:
                print(campaign['biddingStrategyConfiguration']['biddingScheme']['targetRoas'])
                campaign_status[campaign['name']] = {
                    "name": campaign['name'],
                    "status": campaign['status'],
                    "id": campaign['id']
                }
                ##print('Campaign with id "%s", name "%s", and status "%s" was '
                ##      'found.' % (campaign['id'], campaign['name'],
                ##                  campaign['status']))
        else:
            print('No campaigns were found.')
        offset += PAGE_SIZE
        selector['paging']['startIndex'] = str(offset)
        more_pages = offset < int(page['totalNumEntries'])
    for campaign in campaign_status:
        campaign_list.append(campaign_status[campaign])
    return {'campaigns': campaign_list}
    '''


if __name__ == '__main__':
    adwords_client = adwords.AdWordsClient.LoadFromStorage('/Users/keenan/dev/googleads/auth/googleads.yaml')
    campaigns = get_campaigns(adwords_client)
    print(campaigns)