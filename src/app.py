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

from .components import Header

load_dotenv()

app = Dash(__name__, use_pages=True)

#----------------------------------------------------------------------------#
# main method

app.layout = dmc.MantineProvider(
    id="app-layout",
    children=[
        Header("My App"),
        html.A("Homepage", href="/"),
        html.A("Other Page", href="/other_page"),
        html.Div(id="page-content"),
        dash.page_container,
    ],
)

#----------------------------------------------------------------------------#

if __name__ == '__main__':
    app.run(debug=True)