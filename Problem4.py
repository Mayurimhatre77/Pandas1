import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    filter_customers = customers[~customers['id'].isin(orders['customerId'])]
    result = filter_customers[['name']].rename(columns = {'name' : 'Customers'})
    return result