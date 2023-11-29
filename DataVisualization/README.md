---------------------Measures---------------------------------
 
 
1) Age Group:
 
agegroup = 
VAR AgeNumber = VALUE([AGE])
RETURN
SWITCH(
    TRUE(),
    AgeNumber <= 18, "0-18",
    AgeNumber <= 35, "19-35",
    AgeNumber <= 50, "36-50",
    TRUE(), "51+"
)
 
2) gender group
gendergroup = 
SWITCH(
    TRUE(),
    [GENDER] = "u", "u",
    [GENDER] = "f", "f",
    [GENDER] = "m", "m"
)
 
 
2) AVG_SALES = AVERAGE(TRANSACTION_FACT[NET_SALES])
3) COUNT_PLAIN_ID = COUNT(TRANSACTION_FACT[PLAN_ID])
4) Count_PlainId = Count(TRANSACTION_FACT[PLAN_ID] )
5) InValidClaims = COUNTROWS(FILTER(TRANSACTION_FACT, TRANSACTION_FACT[CLAIM_VALID] = "N"))
6) ValidClaims = COUNTROWS(FILTER(TRANSACTION_FACT, TRANSACTION_FACT[CLAIM_VALID] = "Y"))
