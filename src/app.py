#----------------------------------------------------------------------------#
#
#                                   Dash App
#
#----------------------------------------------------------------------------#

# Libraries

from dotenv import load_dotenv

import dash
from dash import Dash, html, dcc
import dash_mantine_components as dmc

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from .components import Header, Footer
from .theme.theme import theme
from .callbacks.initial_load import initial_load
from .callbacks.homepage import *

load_dotenv()

app = Dash(__name__, use_pages=True)

#----------------------------------------------------------------------------#
# main method

app.layout = dmc.MantineProvider(
    id="app-layout",
    theme=theme,
    children=[
        html.Div(
            children=[
                Header("My App"),
                dmc.Paper(
                    children=[
                        html.Div(id="page-content"),
                        dash.page_container,
                    ],
                    style={
                        'padding': '1rem',
                        'overflow': 'auto',
                    }
                ),
                Footer(),
                dcc.Store(id='cached-data'),
                # This is a dummy interval to trigger the initial load.
                dcc.Interval(id='interval', max_intervals=0),
            ],
            style={
                'display': 'grid',
                'grid-template-rows': 'auto 1fr auto',
                'height': '100vh',
                "margin": "0 auto",
            }
        )
    ],
)

#----------------------------------------------------------------------------#

if __name__ == '__main__':
    app.run(debug=True)