#----------------------------------------------------------------------------#
#
#                                   Dash App
#
#----------------------------------------------------------------------------#

# Libraries

from dotenv import load_dotenv

import dash
from dash import Dash, html
import dash_mantine_components as dmc

from .components import Header, Footer
from .theme.theme import theme

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