import requests
import json

# Creation of our variables
bridge_ip = "BRIDGE_IP"
username = "API_TOKEN"
light_number = "LIGHT_ID"

# URLs' structure
lights_url = "http://{}/api/{}/lights".format(bridge_ip, username)

light_state_url = "{}/{}/state".format(lights_url, light_number)

# Retrieving the lights' data
r = requests.get(lights_url)

# Exploring the data
for light in r.json():
    light_current_status = "{} - {} : {}".format(light,
                                                 r.json()[light]["name"].encode(
                                                     "utf-8"),
                                                 r.json()[light]["state"]["on"])

    # Printing the data for good measure
    print(light_current_status)

# Changing the light's state depending on its current state
new_state = not r.json()[light_number]["state"]["on"]
message = json.dumps({"on": new_state})
action = requests.put(light_state_url, data=message)
print(action.content)
