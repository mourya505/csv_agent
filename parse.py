def parse_question(question):
    question=question.lower()
    if "highest" in question and "region" in  question:
        intent="highest_sales_region"
    elif "highest" in question and "product" in question:
        intent="highest_sales_product"
    elif "total" in question:
        intent="total_sales"
    elif "average" in question:
        intent="average_sales"
    else:
        intent="uknown"
    quarter=None
    if "q1" in question:
        quarter = "Q1_Sales"

    elif "q2" in question:
        quarter = "Q2_Sales"

    elif "q3" in question:
        quarter = "Q3_Sales"

    elif "q4" in question:
        quarter = "Q4_Sales"

    return intent, quarter