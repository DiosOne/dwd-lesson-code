# Task: Read updated_config.json. Change the theme to "light" and add a new
#       key-value pair "font_size": 12. Write this modified data to a new
#       file user_prefs.json.

import json

with open("updated_config.json", 'r') as f:
    config_data = json.load(f)
    print (config_data)