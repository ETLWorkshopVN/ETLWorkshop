USE SNOWFLAKE_DEMO;


create or replace table plan_dimension(
plan_name varchar,
plan_key varchar PRIMARY KEY
);

create or replace table customer_dimension(
customer_name varchar,
age INT,
gender varchar,
cust_key varchar PRIMARY KEY
);


create or replace table agency_dimension(
agency_name varchar,
address varchar,
contact varchar,
ag_key varchar PRIMARY KEY
);

create or replace table transaction_fact(
tran_id varchar,
plan_id varchar REFERENCES plan_dimension(plan_key),
agcy_id varchar REFERENCES agency_dimension(ag_key),
cust_id varchar REFERENCES customer_dimension(cust_key),
travel_destination varchar,
duration INT,
claim_amount DECIMAL,
claim_valid CHAR,
net_sales DECIMAL
);

SELECT * FROM AGENCY_DIMENSION;
SELECT * FROM CUSTOMER_DIMENSION;
SELECT * FROM PLAN_DIMENSION;
SELECT * FROM TRANSACTION_FACT;
