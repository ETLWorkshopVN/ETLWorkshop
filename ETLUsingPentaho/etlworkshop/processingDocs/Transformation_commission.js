var comission = 0;

if (lower(trim(plan_name)) == "silver")
{
    comission = 10 * (premium_amount/100);
}
else if (lower(trim(plan_name)) == "gold")
{
    comission = 20 * (premium_amount/100);
}
else if(lower(trim(plan_name)) == "premium")
{
    comission = 30 * (premium_amount/100);
}    
else
    comission = 0;