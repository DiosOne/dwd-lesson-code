'''module to calculate the total cost of visiting a cinema

    :return: total cost of visiting a cinema
    :rtype: int
    '''
# age : integer
# has_membership : boolean
# transport_type : string
def calculate_total_cost_of_visiting_cinema(age, has_membership, transport_type):
    '''function to calculate the total cost of visiting a cinema

    :param age: int
    :type age: int
    :param has_membership: bool
    :type has_membership: bool
    :param transport_type: str
    :type transport_type: str
    :return: total cost of visiting a cinema
    :rtype: int
    '''
    entry_ticket_cost = 10 if age >= 60 else 15
    candy_cost = 5 if has_membership else 10
    parking_cost = 0 if transport_type == 'Bus' else 3


    return entry_ticket_cost + candy_cost + parking_cost

calculate_total_cost_of_visiting_cinema(20, True, 'Car')
