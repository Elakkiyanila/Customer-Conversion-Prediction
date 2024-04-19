import datetime
import pandas as pd

def calculate_bill(units):
    if 0 < units <= 100:
        unit_price = units * 2.25
        fixedcharge = 35
    elif 100 < units <= 200:
        unit_price = (100 * 2.25) + (units - 100) * 4.5
        fixedcharge = 45
    elif 200 < units <= 300:
        unit_price = (100 * 2.25) + ((200 - 100) * 4.5) + (units - 200) * 7.5
        fixedcharge = 75
    elif 300 < units <= 500:
        unit_price = (100 * 2.25) + ((200 - 100) * 4.5) + ((300 - 200) * 7.5) + (units - 300) * 9.5
        fixedcharge = 95
    else:
        unit_price = 0
        fixedcharge = 5000
    # Calculate the total bill
    total_bill = unit_price + fixedcharge
    return total_bill, unit_price, fixedcharge
def electricity_bills(num_bills):
    bills = []  # List to store bill data
    for _ in range(num_bills):
        # Getting user details
        name = input("Enter your name (or type 'exit' to quit): ")
        if name.lower() == 'exit':
            break
        address = input("Enter your address: ")
        consumer_id = input("Enter your consumer ID: ")
        units_consumed = int(input("Enter the units consumed: "))
        bill_amount, unit_price, fixedcharge = calculate_bill(units_consumed)
        # Get the current date
        current_date = datetime.date.today()
        due_date = current_date + datetime.timedelta(days=15)
        # Creating a dictionary for the current bill
        bill_data = {
            "Name": name,
            "Address": address,
            "Consumer ID": consumer_id,
            "Units Consumed": units_consumed,
            "Unit Price": unit_price,
            "Fixedcharge": fixedcharge,
            "Total Amount": bill_amount,
            "Bill Date": current_date,
            "Due Date": due_date,
        }
        bills.append(bill_data)
    if not bills:
        print("No bills generated.")
        return None
    df = pd.DataFrame(bills)
    print("\nElectricity Bills")
    return df
num_bills = int(input("Enter the number of bills to generate: "))
df1 = electricity_bills(num_bills)
print(df1)
