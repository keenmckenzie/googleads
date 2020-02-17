from googleads import adwords


AD_GROUP_ID = 95008684935
KEYWORD_TEXT = 'Test Keyword 1'
MATCH_TYPE = 'PHRASE'
FINAL_URL = 'www.example.com/test/keyword1'


def main(client, ad_group_id, keyword_text, match_type, final_url):
  # Initialize appropriate service.
  ad_group_criterion_service = client.GetService(
      'AdGroupCriterionService', version='v201809')

  # Construct keyword ad group criterion object.
  keyword1 = {
      'xsi_type': 'BiddableAdGroupCriterion',
      'adGroupId': ad_group_id,
      'criterion': {
          'xsi_type': 'Keyword',
          'matchType': match_type,
          'text': keyword_text
      },
      # These fields are optional.
      'userStatus': 'ENABLED',
      'finalUrls': {
          'urls': ['https://' + final_url]
      }
  }

  # Construct operations and add ad group criteria.
  operations = [
      {
          'operator': 'ADD',
          'operand': keyword1
      },

  ]
  ad_group_criteria = ad_group_criterion_service.mutate(
      operations)['value']

  # Display results.
  for criterion in ad_group_criteria:
    print('Keyword ad group criterion with ad group id "%s", criterion id '
          '"%s", text "%s", and match type "%s" was added.'
          % (criterion['adGroupId'], criterion['criterion']['id'],
              criterion['criterion']['text'],
              criterion['criterion']['matchType']))


if __name__ == '__main__':
  # Initialize client object.
  adwords_client = adwords.AdWordsClient.LoadFromStorage('/Users/keenan/dev/ads/auth/googleads.yaml')

  main(adwords_client, AD_GROUP_ID, KEYWORD_TEXT, MATCH_TYPE, FINAL_URL)