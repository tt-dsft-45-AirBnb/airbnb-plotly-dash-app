# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predict your AirBnB Listing Price

            ##### Attention property owners! Are you looking to earn some extra money off the property you own? 
            ##### Do you feel AirBnB is the most convenient site to help rent out your property? 
            ##### But you aren't sure what price to exactly list your property?
            ##### Then you in luck. Our site will help you predict exactly what price you should list your property ny comparing similar
            ##### properties in your neighborhoor. Click the button below and see how valuable your house is today.
            
            """
        ),
        dcc.Link(dbc.Button('Predict Your Price', color='primary'), href='/predictions')
    ],
    md=4,
)


column2 = dbc.Col(
    [
        html.Img(src='assets/treehouse.jpg', width='700px', height='470px'),
    ]
)

layout = dbc.Row([column1, column2])