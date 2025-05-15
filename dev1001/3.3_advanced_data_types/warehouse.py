'''_summary_'''
def update_warehouse_product_database():
    '''_summary_

    :return: _description_
    :rtype: _type_
    '''
    warehouse_product_database = {
        "Xbox": 77,
        "PS5": 912,
        "Switch": 311,
        "Steam Deck": 51,
        "Valve Index": 102
    }
    todays_orders = {
        "Xbox": 12,
        "PS5": 112,
        "Switch": 310,
        "Steam Deck": 51,
        "Valve Index": 62
    }
    after_today= {
        'Xbox': warehouse_product_database["Xbox"] - todays_orders["Xbox"],
        'PS5': warehouse_product_database["PS5"] - todays_orders["PS5"],
        'Switch': warehouse_product_database["Switch"] - todays_orders["Switch"],
        'Steam Deck': warehouse_product_database["Steam Deck"] - todays_orders["Steam Deck"],
        'Valve Index': warehouse_product_database["Valve Index"] - todays_orders["Valve Index"]
    }
    warehouse_product_database.update(after_today)
        # Your challenge is to update the dictionary containing the products contained within the warehouse,
        
        # (warehouse_product_database), using today's orders, (todays_orders),
        
        # so that the warehouse product database dictionary will be updated to reflect the products available in the warehouse after today's orders.
        
    return warehouse_product_database

update_warehouse_product_database()
print(update_warehouse_product_database())
