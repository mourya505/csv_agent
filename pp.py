from tools import *

def execute(intent, df, quarter):

    if intent == "total_sales":
        return total_sales(df, quarter)

    elif intent == "average_sales":
        return average_sales(df, quarter)

    elif intent == "highest_sales_region":
        return highest_sales_region(df, quarter)

    elif intent == "highest_sales_product":
        return highest_sales_product(df, quarter)

    else:
        return "I don't understand the question."