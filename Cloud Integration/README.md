1. IAM Policy:
a. S3FullAccessPolicy
b. CLoudWatchLogsPolicy
 
2. IAM Role:
a. Attach Policies to the IAM Role
 
3. Setup Lambda:
a. Create a function
b. Choose Python as a programming language
c. Find the roles
d. Add code and deploy
 
4. Setup s3 event trigger
a. All object create event
b. Folder to add event: bucket_name/output/
 
5. Snowflake
a. Create trial account
b. Create the necessary table
Link: https://github.com/ETLWorkshopVN/ETLWorkshop/blob/main/Cloud%20Integration/snowflake_tables_ddl.sql
 
6. Retouch the files in s3 bucket