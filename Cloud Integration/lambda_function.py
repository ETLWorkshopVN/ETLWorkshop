from file_utility import download_files_from_s3, generate_rows_from_file
from snowflake_utility import load_tables


def lambda_handler(event, context):
    records = event["Records"][0]
    bucket_name = records["s3"]["bucket"]["name"]
    file_key = records["s3"]["object"]["key"]
    localpath = '/tmp/'
    print(f'##### Bucket - {bucket_name} S3Key - {file_key} #####')
    filepath = download_files_from_s3(bucket_name, file_key, localpath)
    rows = generate_rows_from_file(filepath)
    load_tables(rows)

