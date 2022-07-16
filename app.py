#%%
import pandas as pd
import dash
from dash import html, dcc, Input, Output
import dash_trich_components as dtc
import dash_bootstrap_components as dbc
from builders import kpi_sidebar, kpi_layout, usertype_kpi_layout, main_layout

# %%
app = dash.Dash(__name__, external_stylesheets=[
                                                dbc.themes.SOLAR,
                                                dbc.icons.BOOTSTRAP,
                                                dbc.icons.FONT_AWESOME
                                            ],
                suppress_callback_exceptions=True,
                )

app.layout = main_layout


app.validation_layout = [kpi_sidebar, kpi_layout, usertype_kpi_layout]

if __name__ == '__main__':
    app.run_server(port=8040, debug=False)
