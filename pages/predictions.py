# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app


row = html.Div(
    [
        dbc.Row(dbc.Col(html.Div('''Welcome to our predictions page! Fill out the form as accurately as possible,
                                 and we will compare similar properties (bases on amenities and location) and 
                                 provide you with the best estimate for your daily rental price on AirBnB.''', className='mb-4'))),
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
                            value='Apartment'
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
                            value='Entire home/apt'
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