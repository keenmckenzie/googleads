from googleads import adwords


class Campaign:
    def __init__(self, campaign_id):
        self.campaign_id = campaign_id

    def update_target(self, client, target):
        # Initialize appropriate service.
        campaign_service = client.GetService('CampaignService', version='v201809')
        # Construct operations and add campaigns.
        operations = [{
            'operator': 'SET',
            'operand': {
                'id': self.campaign_id,
                'biddingStrategyConfiguration': {
                    'biddingStrategyType': 'TARGET_ROAS',
                    'biddingScheme': {
                        'xsi_type': 'TargetRoasBiddingScheme',
                        'targetRoas': target,
                    }
                }
            }
        }]
        campaigns = campaign_service.mutate(operations)
        for campaign in campaigns['value']:
            print('Campaign with name "%s" and id "%s" is now "%s".'
                  % (campaign['name'], campaign['id'], campaign['biddingStrategyConfiguration']))
