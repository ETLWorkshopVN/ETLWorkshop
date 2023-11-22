import boto3
import os


def download_files_from_s3(bucket_name, s3_key, local_path):
    s3 = boto3.client('s3', verify=False)
    filename = s3_key.split("/")[-1]
    print(f'Downloading file from s3://{bucket_name}/{s3_key}')
    s3.download_file(bucket_name, s3_key, f'{local_path}/{filename}')
    print("File Download Success")
    return f'{local_path}/{filename}'


def read_file(file_path):
    with open(file_path) as file:
        data = []
        fields = tuple(field.strip() for field in file.readline().split(","))
        for line in file:
            line = tuple(field_value.strip() for field_value in line.split(','))
            data.append(line)
    return fields, data


def generate_rows_from_file(filepath):
    rows = {}
    fields, data = read_file(filepath)
    table = os.path.splitext(os.path.basename(filepath))[0]

    rows[table] = {"fields": fields, "data": data}
    print(f"Processed {table} file")

    return rows
