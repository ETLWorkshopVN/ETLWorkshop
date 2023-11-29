A.	Pentaho Installation Guidelines
Prerequisites
•	Java SE: Download  a 64-bit Java SE (JRE) from Adoptium and install in your laptop. video.
o	Add java bin path to environment variable in “path” variable.
•	Pentaho Data Integration: Download PDI from Hitachi and install it.
•	AWS CLI: Download and install AWS CLI. For exe file link 

B.	AWS services
We use a cloud guru sandbox for AWS services. For this you must follow below steps:
•	Open command prompt in your laptop
•	To configure AWS credentials type: aws configure.
•	Use provided Access key id and Secret access key.
•	Use default region and output format: Simple PRESS ENTER.
•	To test simply, type - aws s3 ls. This will list all available s3 buckets.

C.	ETL Pipeline
Source
For this ETL pipeline, there are multiple sources for file inputs. They are given below:
1.	CSV
2.	TSV
3.	Excel (xlsx)
4.	JSON
5.	Flat file (txt)
Various fields incorporated on these files are:
1.	Agency name: refers to the name of travel agency name.
2.	Agency type: refers to the travel agency.
3.	Address: refers to the address of agency.
4.	Contact: refers to the contact number of agency.
5.	Distribution channel: refers to the channel insurance plan sold to customer. Either Online or offline.
6.	Plan name: refers to various type of plans issued by insurance company. Option: Silver, Gold, and Premium.
7.	Premium amount: refers to the lump sum amount paid by customer to buy insurance plan. This varies upon the insurance plan and the agency.
8.	Customer name: refers to the name of buyer of travel insurance plan.
9.	Age: refers to the age of customer
10.	Gender: refers to the gender of customer
11.	Travel date: refers to the travel date.
12.	Travel destination: refers to the destination country.
13.	duration: number of travel days.
14.	Claim date: refers to date of claim issued by the customer to insurance agency.
15.	Claim amount: refers to the amount claimed by the customer to insurance agency to cover their losses.
Metrics calculation in ETL Process
We calculate various metrics which are given below:
1.	Commission amount: Commission is given by insurance company to travel company. This amount is calculated based on category of plan. 
a.	For Premium: 30% of premium amount.
b.	For Gold: 20% of premium amount.
c.	For Silver: 10% of premium amount.

2.	Claim after days: This refers to number of days that the customer applied for their claims. It is calculated as:
Claim_after_days = claim_date – travel_date

3.	Claim Validity: If customer claimed their losses within 30 days of their travel. They are the valid claims otherwise claims are invalid.

4.	Net sales (Profit): This is the net profit earned by the insurance company. This is calculated based on claims validity.
It is calculated as:
a.	For valid claims: 
Net sales = Premium amount – commission amount – claimed amount.
b.	For Invalid claims:
Net sales = Premium amount – commission amount.

Data Warehouse:
•	A centralized repository of data, used for reporting and analysis.
•	Stores large amounts of data over a long period.
•	Provide consolidated view of data for decision makers to gain insights and make informed business decision.
•	Data in DW is organized using a dimensional model, which include:
o	facts (numeric performance measures)
o	dimensions (contextual information)
•	Facilitate easy querying and reporting.
 


Facts Table:
•	Transaction Fact table: include columns as below:
o	tran_id: refers to unique transaction id.
o	Plan_id: refers to plan id and help to link with agency dimension table.
o	Agcy_Id: refers to agency id. This makes relation to agency dimension table.
o	Cust_id: refers to customer id. Link with customer dimension table.
o	Travel_destination: refers to name of destination country.
o	Duration: refers to number of travel days.
o	Claim_amount: refers to claim amount claimed by a customer.
o	Claim_valid: refers to a flag that denotes claim is valid or not.
o	Net_sales: refers to profit amount

Dimension Tables:
•	Agency Dimension:
o	Ag_key: primary key for agency dimension table.
o	Agency_name: name of travel agency name.
o	Address: refers to the address of agency
o	Contact: refers to the contact number of agency.
•	Plan Dimension:
o	Plan_key: primary key for plan dimension table.
o	Plan_name: refers to name of plan. Option: Silver, Gold, and Premium.
•	Customer Dimension:
o	Cust_key: primary key for customer dimension table.
o	Customer_name: refers to the name of buyer of travel insurance plan.
o	Age: refers to the age of customer.
o	Gender: refers to the gender of customer
