# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_daq as daq

# Imports from this application
from app import app


row = html.Div(
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
        # 3rd Row. Includes Accomadates, Number of bathrooms
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown("##### Accomadates", className='mb-1'),
                        daq.NumericInput(
                            id='my-daq-accomadates',
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
                            id='my-daq-bedrooms',
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
                            id='my-daq-beds',
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
    ]
)

layout = row

# # 2 column layout. 1st column width = 4/12
# # https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
# column1 = dbc.Col(
#     [
#         dcc.Markdown(
#             """
        
#             ## Predictions

#             Your instructions: How to use your app to get new predictions.

#             """
#         ),
#     ],
#     md=4,
# )

# column2 = dbc.Col(
#     [

#     ]
# )

# layout = dbc.Row([column1, column2])