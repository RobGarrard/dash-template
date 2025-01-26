# ----------------------------------------------------------------------------#
#
#                                  Homepage
#
# ----------------------------------------------------------------------------#

# Libraries

import dash
from dash import html

# ----------------------------------------------------------------------------#
# Register page

dash.register_page(__name__, path='/')

# ----------------------------------------------------------------------------#
# Components

page_title = html.H1("Homepage")

full_width_chart = html.Div(
    id="homepage-full-width-chart",
    children=[html.H2("Full Width Chart")],
    style={
        "width": "100%",
        "height": "500px",
        "background-color": "lightgrey",
    },
)

# ----------------------------------------------------------------------------#
# Layout

layout = html.Div(
    id="homepage-layout", children=[page_title, full_width_chart]
)
