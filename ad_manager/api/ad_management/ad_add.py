import uuid

from googleads import adwords

AD_GROUP_ID = 95008684935
HEADLINE_1 = 'Test Ad Headline'
HEADLINE_2 = 'Headline 2'
DESCRIPTION = 'This is a test ad.'
DESCRIPTION_2 = 'This is the second description.'
FINAL_URL = 'https://www.example.com/test_ETA'


def main(client, ad_group_id, headline_1, headline_2, description, description_2, final_url):
    # Initialize appropriate service.
    ad_group_ad_service = client.GetService('AdGroupAdService', version='v201809')

    operations = [
        {
            'operator': 'ADD',
            'operand': {
                'xsi_type': 'AdGroupAd',
                'adGroupId': ad_group_id,
                'ad': {
                    'xsi_type': 'ExpandedTextAd',
                    'headlinePart1': headline_1,
                    'headlinePart2': headline_2,
                    'description': description,
                    'description2': description_2,
                    'finalUrls': [final_url],
                },
                # Optional fields.
                'status': 'ENABLED'
            }
        }
    ]

    ads = ad_group_ad_service.mutate(operations)

    # Display results.
    for ad in ads['value']:
        print('Ad of type "%s" with id "%d" was added.'
              '\n\theadlinePart1: %s\n\theadlinePart2: %s\n\theadlinePart3: %s'
              % (ad['ad']['Ad.Type'], ad['ad']['id'],
                 ad['ad']['headlinePart1'], ad['ad']['headlinePart2'],
                 ad['ad']['headlinePart3']))


if __name__ == '__main__':
    # Initialize client object.
    adwords_client = adwords.AdWordsClient.LoadFromStorage('/Users/keenan/dev/googleads/auth/googleads.yaml')

    main(adwords_client, AD_GROUP_ID, HEADLINE_1, HEADLINE_2, DESCRIPTION, DESCRIPTION_2, FINAL_URL)
