'''
This module contains a function to check if a mission is ready to
embark based on the availability of supplies,
the distance to the mission site, and the amount of fuel in the vehicle.
'''
def ready_to_embark_on_mission(have_supplies, distance_to_mission_site, fuel_in_vehicle):
    '''
    Determine if a mission is ready to embark based on supplies, distance, and fuel.

    Parameters:
        have_supplies (bool): Whether the mission has the necessary supplies.
        distance_to_mission_site (int): The distance to the mission site.
        fuel_in_vehicle (int): The amount of fuel in the vehicle.

    Returns:
        bool: True if the mission is ready to embark, False otherwise.
    '''
    if have_supplies and (distance_to_mission_site <= 10 or (distance_to_mission_site > 10 and
     fuel_in_vehicle >= distance_to_mission_site * 2)):
        print('Mission ready to embark.')
        return True
    else:
        print('Mission not ready to embark.')
        return False

ready_to_embark_on_mission(True, 20, 30)
