import datetime
import streamlit as st

import numpy as np
import pandas as pd
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- Number of good
- year
- Number of rooms
- Surface
- ZIP Code
'''

#['Nombre de lots','year','Nombre pieces principales','Surface reelle bati','Code postal']





#Number of good
nb_good = st.number_input('Insert a number of good',0)

st.write('The current pickup longitude is ', nb_good)


#year
year = st.number_input('Insert a year',2011)

st.write('The current year is ', year)


#Number of rooms
Number_of_rooms = st.number_input('Insert a Number_of_rooms',1)

st.write('The current dropoff longitude is ', Number_of_rooms)


#Surface
Surface = st.number_input('Insert a Surface',100)

st.write('The current dropoff latitude is ', Surface)


#ZIP code
zipcode = st.number_input('Insert a zipcode',76600)

st.write('The current number of passenger is ', zipcode)




'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

#url = 'https://taxifare.lewagon.ai/predict'
url = 'https://prod-api2-xkl6u47rlq-ew.a.run.app/predict'
if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...'''

params={
            'nb_lot':int,
            'year':int,
            'nb_rooms':int,
            'surface':float,
            'zip':int}



'''3. Let's call our API using the `requests` package...'''


#r = requests.get(f'https://taxifare.lewagon.ai/predict?pickup_datetime={d} {time}&pickup_longitude={pickup_longitude}&pickup_latitude={pickup_latitude}&dropoff_longitude={dropoff_longitude}&dropoff_latitude={dropoff_latitude}&passenger_count={number_of_passenger}').json()

r=requests.get(url,params=params).json()



'''4. Let's retrieve the prediction from the **JSON** returned by the API...'''

fare = r['fare']

fare


'''## Finally, we can display the prediction to the user
'''





st.map()
