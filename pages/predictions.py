# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_daq as daq
import pandas as pd
from datetime import date
from tensorflow import keras

# Imports from this application
from app import app
from pred_lists import zip_code, neighborhood
from airbnb_model import *


# load model trained on airbnb data
model = keras.models.load_model('airbnb_model')
print('Model loaded successfully')

# create input form for User
row1 = html.Div(
    [
        # 1st Row. Introductory Marks
        dbc.Row(dbc.Col(html.Div('''Welcome to our predictions page! Fill out the form as accurately as possible,
                                 and we will compare similar properties (bases on amenities and location) and 
                                 provide you with the best estimate for your daily rental price on AirBnB.''', className='mb-4'))),
        # 2nd Row. Includes Property Type, Room Type
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown("##### Property Type", className='mb-1'),
                        dcc.Dropdown(
                            id='property',
                            options=[
                                {'label': 'Apartment', 'value': 'Apartment'},
                                {'label': 'House', 'value': 'House'},
                                {'label': 'Condominium', 'value': 'Condominium'},
                                {'label': 'Townhouse', 'value': 'Townhouse'},
                                {'label': 'Loft', 'value': 'Loft'},
                                {'label': 'Other', 'value': 'Other'},
                                {'label': 'Guesthouse', 'value': 'Guesthouse'},
                                {'label': 'Bed & Breakfast', 'value': 'Bed & Breakfast'},
                                {'label': 'Bungalow', 'value': 'Bungalow'},
                                {'label': 'Dorm', 'value': 'Dorm'},
                                {'label': 'Guest suite', 'value': 'Guest suite'},
                                {'label': 'Villa', 'value': 'Villa'},
                                {'label': 'Timeshare', 'value': 'Timeshare'},
                                {'label': 'In-law', 'value': 'In-law'},
                                {'label': 'Boutique hotel', 'value': 'Boutique hotel'},
                                {'label': 'Hostel', 'value': 'Hostel'},
                                {'label': 'Camper/RV', 'value': 'Camper/RV'},
                                {'label': 'Cabin', 'value': 'Cabin'},
                                {'label': 'Boat', 'value': 'Boat'},
                                {'label': 'Serviced apartment', 'value': 'Serviced apartment'},
                                {'label': 'Castle', 'value': 'Castle'},
                                {'label': 'Tent', 'value': 'Tent'},
                                {'label': 'Vacation home', 'value': 'Vacation home'},
                                {'label': 'Yurt', 'value': 'Yurt'},
                                {'label': 'Treehouse', 'value': 'Treehouse'},
                                {'label': 'Chalet', 'value': 'Chalet'},
                                {'label': 'Hut', 'value': 'Hut'},
                                {'label': 'Tipi', 'value': 'Tipi'},
                                {'label': 'Earth House', 'value': 'Earth House'},
                                {'label': 'Cave', 'value': 'Cave'},
                                {'label': 'Casa particular', 'value': 'Casa particular'},
                                {'label': 'Train', 'value': 'Train'}
                            ],
                            # value='Apartment',
                            className='mb-4',
                        ),
                    ],
                ),
                dbc.Col(
                    [
                        dcc.Markdown("##### Room Type", className='mb-1'),
                        dcc.Dropdown(
                            id='room',
                            options=[
                                {'label': 'Entire Home/Apartment', 'value': 'Entire home/apt'},
                                {'label': 'Private Room', 'value': 'Private room'},
                                {'label': 'Shared room', 'value': 'Shared room'}
                            ],
                            # value='Entire home/apt',
                            className='mb-4',
                        ),
                    ],
                ),
            ]
        ),
        # 3rd Row. Includes Accomadates, number of bathrooms
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown("##### Accomadates", className='mb-1'),
                        daq.NumericInput(
                            id='accomadates',
                            min=1,
                            max=16,
                            value=1,
                            className='mb-4',
                        ),
                    ],
                ),
                dbc.Col(
                    [
                        dcc.Markdown("##### Number of Bathrooms", className='mb-1'),
                        dcc.Slider(
                            id='bathrooms',
                            min=0,
                            max=8,
                            step=0.5,
                            marks={
                                0: '0',
                                0.5: '0.5',
                                1: '1',
                                1.5: '1.5',
                                2: '2',
                                2.5: '2.5',
                                3: '3',
                                3.5: '3.5',
                                4: '4',
                                4.5: '4.5',
                                5: '5',
                                5.5: '5.5',
                                6: '6',
                                6.5: '6.5',
                                7: '7',
                                7.5: '7.5',
                                8: '8'
                            },    
                            value=1,
                            className='mb-4',
                        ),
                    ],
                ),
            ]
        ),
        # 4th Row. Includes Bedrooms, Beds
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown("##### Number of Bedrooms", className='mb-1'),
                        daq.NumericInput(
                            id='bedrooms',
                            min=0,
                            max=10,
                            value=1,
                            className='mb-4',
                        ),  
                    ],
                ),
                dbc.Col(
                    [
                        dcc.Markdown("##### Number of Beds", className='mb-1'),
                        daq.NumericInput(
                            id='beds',
                            min=0,
                            max=18,
                            value=1,
                            className='mb-4',
                        ),
                    ],
                ),
            ]
        ),
        # 5th Row. Includes bed_type, cancellation_policy
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown("##### Bed Type", className='mb-1'),
                        dcc.Dropdown(
                            id='bedtype',
                            options=[
                                {'label': 'Real Bed', 'value': 'Real Bed'},
                                {'label': 'Futon', 'value': 'Futon'},
                                {'label': 'Pull-out Sofa', 'value': 'Pull-out Sofa'},
                                {'label': 'Airbed', 'value': 'Airbed'},
                                {'label': 'Couch', 'value': 'Couch'},
                            ],
                            className='mb-4',
                        ),
                    ],
                ),
                dbc.Col(
                    [
                        dcc.Markdown("##### Cancellation Policy", className='mb-1'),
                        dcc.Dropdown(
                            id='cancellation',
                            options=[
                                {'label': 'Strict', 'value': 'strict'},
                                {'label': 'Flexible', 'value': 'flexible'},
                                {'label': 'Moderate', 'value': 'moderate'},
                                {'label': 'Super Strict 30', 'value': 'super_strict_30'},
                                {'label': 'Super Strict 60', 'value': 'super_strict_60'},
                            ],
                            className='mb-4',
                        ),
                    ],
                ),
            ]
        ),
        # 6th Row. Includes cleaning_fee, city
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown("##### Includes Cleaning Fee", className='mb-1'),
                        daq.BooleanSwitch(
                            id='cleaning',
                            on=True,
                            label='Blue = True',
                            className='mb-4',
                        ),
                    ],
                ),
                dbc.Col(
                    [
                        dcc.Markdown("##### City", className='mb-1'),
                        dcc.Dropdown(
                            id='city',
                            options=[
                                {'label': 'New York City', 'value': 'NYC'},
                                {'label': 'Los Angeles', 'value': 'LA'},
                                {'label': 'San Francisco', 'value': 'SF'},
                                {'label': 'Washington DC', 'value': 'DC'},
                                {'label': 'Boston', 'value': 'Boston'},
                                {'label': 'Chicago', 'value': 'Chicago'},
                            ],
                            className='mb-4',
                        ),
                    ],
                ),
            ]
        ),
        # 7th Row. Includes host_identity_verified, instant_bookable, host_since_days
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown("##### You Are a Verified Host", className='mb-1'),
                        daq.BooleanSwitch(
                            id='verified_host',
                            on=True,
                            label='Blue = True',
                            className='mb-4',
                        ),
                    ],
                ),
                dbc.Col(
                    [
                        dcc.Markdown("##### Is Instantly Bookable", className='mb-1'),
                        daq.BooleanSwitch(
                            id='bookable',
                            on=True,
                            label='Blue = True',
                            className='mb-4',
                        ),
                    ],
                ),
                dbc.Col(
                    [
                        dcc.Markdown("##### Host Start Date", className='mb-1'),
                        dcc.DatePickerSingle(
                            id='days_host',
                            date=date(2010, 1, 1)
                        )
                    ],
                ),
            ]
        ),
        # 8th Row. Includes neighbourhood, zipcode
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown("##### Neighborhood", className='mb-1'),
                        dcc.Dropdown(
                            id='neighborhood',
                            options=neighborhood.neighborhoods,
                            className='mb-4',
                        ),
                    ],
                ),
                dbc.Col(
                    [
                        dcc.Markdown("##### Zipcode", className='mb-1'),
                        dcc.Dropdown(
                            id='zipcode',
                            options=zip_code.total_zip,
                            className='mb-4',
                        ),
                    ],
                ),
            ]
        ),
        # 9th Row. Includes amenities
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown("##### Amenities", className='mb-1'),
                        dcc.Checklist(
                            id='amenities',
                            options=[
                                {'label': 'TV', 'value': 'TV'},
                                {'label': 'Cable TV', 'value': 'Cable TV'},
                                {'label': 'Kitchen', 'value': 'Kitchen'},
                                {'label': 'Free parking on premises ', 'value': 'Free parking on premises'},
                                {'label': 'Breakfast ', 'value': 'Breakfast'},
                                {'label': 'Elevator in building ', 'value': 'Elevator in building'},
                                {'label': 'Heating ', 'value': 'Heating'},
                                {'label': 'Washer ', 'value': 'Washer'},
                                {'label': 'Dryer ', 'value': 'Dryer'},
                                {'label': 'Smoke detector ', 'value': 'Smoke detector'},
                                {'label': 'First aid kit ', 'value': 'First aid kit'},
                                {'label': 'Safety card ', 'value': 'Safety card'},
                                {'label': 'Fire extinguisher ', 'value': 'Fire extinguisher'},
                                {'label': 'Hair dryer ', 'value': 'Hair dryer'},
                                {'label': 'Laptop friendly workspace ', 'value': 'Laptop friendly workspace'},
                                {'label': 'Wireless Internet ', 'value': 'Wireless Internet'},
                                {'label': 'Air conditioning ', 'value': 'Air conditioning'},
                                {'label': 'Gym ', 'value': 'Gym'},
                                {'label': 'Carbon monoxide detector ', 'value': 'Carbon monoxide detector'},
                                {'label': 'First aid kit ', 'value': 'First aid kit'},
                                {'label': 'Wheelchair accessible ', 'value': 'Wheelchair accessible'},
                                {'label': 'Family/kid friendly ', 'value': 'Family/kid friendly'},
                            ],
                            inputStyle={"margin-right": '8px'},
                            labelStyle = {'margin-right':'15px'}
                        )
                    ],
                ),
            ]
        ),
    ]
)


# output section that returns estimated price based off inputs
row2 = html.Div(
    dbc.Col(
        [
            html.H2('Price Estimation', className='mb-5'), 
            html.Div(id='prediction-content', className='lead')
        ]
    )
)



@app.callback(
    Output('prediction-content', 'children'),
    [
        Input('property', 'value'), Input('room', 'value'), Input('accomadates', 'value'),
        Input('bathrooms', 'value'), Input('bedrooms', 'value'), Input('beds', 'value'),
        Input('bedtype', 'value'), Input('cancellation', 'value'), Input('cleaning', 'value'),
        Input('city', 'value'), Input('verified_host', 'value'), Input('bookable', 'value'), Input('days_host', 'value'),
        Input('neighborhood', 'value'), Input('zipcode', 'value'), Input('amenities', 'value')
    ],
)
def predict(
    property, room, accomadates, bathrooms,
    bedrooms, beds, bedtype, cancellation,
    cleaning, city, verified_host, bookable,
    days_host, neighborhood, zipcode, amenities):
    df = pd.DataFrame(
        columns=[
            'property', 'room', 'accomadates', 'bathrooms,',
            'bedrooms', 'beds', 'bedtype', 'cancellation',
            'cleaning', 'city', 'verified_host', 'bookable',
            'days_host', 'neighborhood', 'zipcode', 'amenities'
        ], 
        data=[
            [
                property, room, accomadates, bathrooms,
                bedrooms, beds, bedtype, cancellation,
                cleaning, city, verified_host, bookable,
                days_host, neighborhood, zipcode, amenities
            ]
        ]
    )
    y_pred = model.predict(df)[0]
    return f'{y_pred:.0f} dollars per day'


# layout of the page
layout = dbc.Row([row1, row2])