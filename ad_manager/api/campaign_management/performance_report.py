import sys
from googleads import adwords


def main(client):
    # Initialize appropriate service.
    report_downloader = client.GetReportDownloader(version='v201809')

    # Create report query.
    report_query = (adwords.ReportQueryBuilder()
                    .Select('CampaignId', 'CampaignName', 'Impressions', 'Clicks',
                            'Cost')
                    .From('CAMPAIGN_PERFORMANCE_REPORT')
                    .Where('CampaignName').Contains('tROAS')
                    .Where('CampaignStatus').EqualTo('ENABLED')
                    .Where('Impressions').GreaterThan('0')
                    .During('LAST_7_DAYS')
                    .Build())

    # You can provide a file object to write the output to. For this
    # demonstration we use sys.stdout to write the report to the screen.
    report_downloader.DownloadReportWithAwql(
        report_query, 'CSV', sys.stdout, skip_report_header=False,
        skip_column_header=False, skip_report_summary=False,
        include_zero_impressions=True)


if __name__ == '__main__':
    # Initialize client object.
    adwords_client = adwords.AdWordsClient.LoadFromStorage('/Users/keenan/dev/googleads/auth/googleads.yaml')

    main(adwords_client)
