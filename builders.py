#%%
import dash_bootstrap_components as dbc
from dash import html, dcc
import numpy as np
from style import homepage_icon_style, page_style, cardstyling, button_style, input_style
import dash_trich_components as dtc
from helper_components import (output_card, 
                               
                               )
import pandas as pd
from PIL import Image
#%%
img_kpi = Image.open('img/kpi.png')
img_scq = Image.open('img/SCQ.png')
#%%
data=pd.read_csv(r"Data/new_data.csv")

main_layout = html.Div(
    [
        dbc.NavbarSimple(
            brand="Dental21",
            brand_href="/",
            light=True,
            brand_style={"color": "#FFFFFF", "backgroundColor": "#FF8B00"},
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Location(id="location"),
                        html.Div(id="main_content"),
                        dcc.Loading(
                            id="loading_cach_data_stored",
                            type="cube",
                            fullscreen=True,
                            children=[dcc.Store(id="cach_data_stored")
                                      ],
                        ),
                    ]
                )
            ]
        ),
    ],
    style=page_style,
)


app_description = dbc.Container(
    style=page_style,
    children=[
        dbc.Row(html.H2("KPI Dashboard", style=input_style)),
        
        dbc.Row(
            children=[
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardImg(
                                    src=img_kpi,
                                    top=True,
                                    style=homepage_icon_style,
                                ),
                                dbc.CardLink(
                                    children=[
                                        dbc.CardImgOverlay(
                                            [
                                                dbc.CardBody(
                                                    html.H1(
                                                        "Key Performance Indicator",
                                                        style={"margin": "5%", 'color': '#FF8B00'},
                                                    )
                                                )
                                            ]
                                        )
                                    ],
                                    href="explore",
                                ),
                            ],
                            style={"width": "18rem", "height": "18rem"},
                        )
                    ]
                ),
                dbc.Col(
                    [
                        
                    ]
                ),
            ]
        ),
        
        html.Br(),
        
        dbc.Row(
            [
              
              dbc.Col(lg=1),
              dbc.Col(lg=6,
                    children=[
                        dbc.Label('Business Problem Design'), html.Br(),
                        dbc.Card(
                            [
                                dbc.CardImg(
                                    src=img_scq,
                                    top=True,
                                    style=homepage_icon_style,
                                ),
                            ],
                        )
                    ]
                ),
              dbc.Col(lg=5)
              
                 
            ]
        )
    ]
)


kpi_sidebar = html.Div(
    [
        dtc.SideBar(
            [
                dtc.SideBarItem(id="id_kpi", label="KPI", 
                                icon="fas fa-chart-bar" 
                                ),
                dtc.SideBarItem(id="id_user_kpi", label="User based KPI", 
                                icon="fas fa-chart-line"
                                )
            ],
            bg_color="#0088BC",
        ),
        html.Div([], id="page_content"),
    ]
)

kpi_layout = html.Div(
    [
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            id="date_dropdown", lg=3, style={"paddingLeft": "0%"},
                            children=[dcc.Dropdown(id='id_year_dropdown',
                                                   options=[{"label": year, "value": year}
                                                            for year in data['Year']]
                                                   ),
                                      
                                      dcc.Dropdown(id='id_month_dropdown',
                                                   options=[{'label': month, 'value': month}
                                                            for month in data['Month']
                                                            ]
                                                   )
                                    ]
                        ),
                        dbc.Col(
                            id="building_gateway",
                            lg=9,
                            children=[
                                dbc.Row(
                                    [
                                        output_card(id="id_conversion", 
                                                    card_label="Conversion rate",
                                                    icon="bi bi-grid-3x3-gap",
                                                    style=cardstyling
                                                    ),
                                        output_card(id="id_bounce", 
                                                    card_label="Bounce rate",
                                                    icon="bi bi-building",
                                                    style=cardstyling
                                                    )
                                    ]
                                ),
                                html.Br(),
                                dbc.Row(
                                    [
                                        dbc.Col([dcc.Graph(id='conversion_graph')]),
                                        dbc.Col([dcc.Graph(id='bounce_graph')])
                                    ]
                                ),
                            ],
                        ),
                    ]
                )
            ]
        ),
    ]
)





usertype_kpi_layout = html.Div(
    [
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            id="user_date_dropdown", lg=3, style={"paddingLeft": "0%"},
                            children=[dcc.Dropdown(id='id_user_year_dropdown',
                                                   options=[{"label": year, "value": year}
                                                            for year in data['Year']]
                                                   ),
                                      
                                      dcc.Dropdown(id='id_user_month_dropdown',
                                                   options=[{'label': month, 'value': month}
                                                            for month in data['Month']
                                                            ]
                                                   )
                                    ]
                        ),
                        dbc.Col(
                            id="building_gateway",
                            lg=9,
                            children=[
                                dbc.Row(
                                    [
                                        output_card(id="id_user_conversion", 
                                                    card_label="New User Conversion rate",
                                                    icon="bi bi-grid-3x3-gap",
                                                    style=cardstyling
                                                    ),
                                        output_card(id="id_user_bounce", 
                                                    card_label="Returning Bounce rate",
                                                    icon="bi bi-building",
                                                    style=cardstyling
                                                    )
                                    ]
                                ),
                                html.Br(),
                                dbc.Row(
                                    [
                                        output_card(id="id_total_new_user", 
                                                    card_label="Number of New Users",
                                                    icon="bi bi-grid-3x3-gap",
                                                    style=cardstyling
                                                    ),
                                        output_card(id="id_total_return_use", 
                                                    card_label="Number of Returning Users",
                                                    icon="bi bi-building",
                                                    style=cardstyling
                                                    )
                                    ]
                                ),
                                
                                
                                dbc.Row(
                                    [
                                        dbc.Col([dcc.Graph(id='new_user_graph')]),
                                        dbc.Col([dcc.Graph(id='return_user_graph')])
                                    ]
                                ),
                            ],
                        ),
                    ]
                )
            ]
        ),
    ]
)


