from random import random
import time
from dcd.entities.thing import Thing
from dcd.entities.property import PropertyType

from dotenv import load_dotenv
import os
# The thing ID and access token
load_dotenv()
THING_ID = os.environ['THING_ID']
THING_TOKEN = os.environ['THING_TOKEN']

# Instantiate a thing with its credential
my_thing = Thing(thing_id=THING_ID, token=THING_TOKEN)

# We can fetch the details of our thing
my_thing.read()

#print(my_thing.to_json())

# If we have no properties, let's create a random one
my_property = my_thing.find_or_create_property("My Random Property",
                                               PropertyType.THREE_DIMENSIONS)

#print(my_property.to_json())

# Let's create a function that generate random values
def generate_dum_property_values(the_property):
    # Define a tuple with the current time, and 3 random values
    values = (random(), random(), random())
    # Update the values of the property
    the_property.update_values(values)

while True:
    generate_dum_property_values(my_property)
    # Have a 2-second break
    time.sleep(2)
