from FoodClass import Customer, Transaction

def main():
    customers = [
        {"customerid": 570, "name": "Danni Sellyar", "address": "97 Mitchell Way, Hewitt, Texas 76712",
         "email": "dsellyar@gmpg.org", "phone": "254-555-9362", "member_status": False},
        {"customerid": 569, "name": "Aubree Himsworth", "address": "1172 Moulton Hill, Waco, Texas 76710",
         "email": "ahimsworthfs@list-manage.com", "phone": "254-555-2273", "member_status": True}
    ]

    transactions = [
        {"date": "2024-09-01", "item_name": "Apple", "cost": 1.0, "customerid": 570},
        {"date": "2024-09-02", "item_name": "Banana", "cost": 0.5, "customerid": 570},
        {"date": "2024-09-03", "item_name": "Cherry", "cost": 2.0, "customerid": 569}
    ]

    for customer_info in customers:
        customer = Customer(**customer_info)
        print_customer_report(customer, transactions)

def print_customer_report(customer, transactions):
    print("Customer Report")
    print("=================")
    print(f"Customer ID: {customer.get_customerid()}")
    print(f"Name: {customer.get_name()}")
    print(f"Address: {customer.get_address()}")
    print(f"Email: {customer.get_email()}")
    print(f"Phone: {customer.get_phone()}")
    print(f"Member Status: {'Yes' if customer.get_member_status() else 'No'}")
    print("\nTransactions:")
    print("-------------")

    total_cost = 0
    for transaction_info in transactions:
        if transaction_info['customerid'] == customer.get_customerid():
            transaction = Transaction(**transaction_info)
            print(f"Date: {transaction.get_date()}")
            print(f"Item: {transaction.get_item_name()}")
            print(f"Cost: ${transaction.get_cost()}")
            total_cost += transaction.get_cost()

    if customer.get_member_status():
        discount = total_cost * 0.20
        total_cost -= discount
        print(f"Discount: -${discount:.2f}")

    print(f"Total Cost: ${total_cost:.2f}")
    print("=================\n")

if __name__ == "__main__":
    main()
