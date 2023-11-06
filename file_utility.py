import boto3


def download_files_from_s3(bucket_name, s3_keys, local_path):
    s3 = boto3.client('s3', verify=False)
    for key in s3_keys:
        filename = key.split("/")[-1]
        print(f'Downloading file from s3://{bucket_name}/{key}')
        s3.download_file(bucket_name, key, f'{local_path}/{filename}')

    print("File Download Success")


def read_file(file_path):
    with open(file_path) as file:
        data = []
        fields = tuple(field.strip() for field in file.readline().split(","))
        for line in file:
            line = tuple(field_value.strip() for field_value in line.split(','))
            data.append(line)
    return fields, data


def generate_rows_from_file(**kwargs):
    rows = {}
    file_paths = [
        kwargs.get('plan_file_path'),
        kwargs.get('agency_file_path'),
        kwargs.get('customer_file_path'),
        kwargs.get('transaction_file_path')
    ]
    tables = ['plan_dimension', 'agency_dimension', 'customer_dimension', 'transaction_fact']

    for table, path in zip(tables, file_paths):
        fields, data = read_file(path)
        rows[table] = {"fields": fields, "data": data}
        print(f"Processed {table} file")

    return rows
