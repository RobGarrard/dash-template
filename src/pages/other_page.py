# ----------------------------------------------------------------------------#
#
#                                 Other Page
#
# ----------------------------------------------------------------------------#

# Libraries

import dash
from dash import html

# ----------------------------------------------------------------------------#
# Register page

dash.register_page(__name__, path="/other_page")

# ----------------------------------------------------------------------------#
# Components

page_title = html.H1("Other Page")

full_width_chart = html.Div(
    id="other-page-full-width-chart",
    children=[html.H2("Yet Another Chart")],
    style={
        "width": "100%",
        "height": "500px",
        "background-color": "lightgrey",
    },
)

# ----------------------------------------------------------------------------#
# Layout

layout = html.Div(
    id="other-page-layout", children=[page_title, full_width_chart]
)
