# ----------------------------------------------------------------------------#
#
#                                  Homepage
#
# ----------------------------------------------------------------------------#

# Libraries

import dash
from dash import html
import dash_mantine_components as dmc

from theme.theme import theme

from components import ChartContainer

# ----------------------------------------------------------------------------#
# Register page

dash.register_page(__name__, path='/', order=0)

# ----------------------------------------------------------------------------#
# Components

page_title = html.H1(
    "Homepage",
    style={
        'color': theme['colors']['primary'][0],
    }
)

text_block = dmc.Paper(
    children=[
        html.P("This is a text block. You can describe stuff here."),
    ],
)

full_width_chart = html.Div(
    id="homepage-full-width-chart",
    children=[
        ChartContainer(id='chart-1'),
    ],
    style={
        "width": "100%",
        "height": "500px",
        "background-color": "lightgrey",
        "display": "grid",
        "place-items": "center",
    },
)

# Grid of 2
two_charts = html.Div(
    id="homepage-two-charts",
    children=[
        html.Div(
            children=[
                ChartContainer(id='chart-2'),
            ],
            style={
                "width": "100%",
                "min-height": "500px",
                "background-color": "lightgrey",
                "display": "grid",
                "place-items": "center",
            },
        ),
        html.Div(
            children=[
                ChartContainer(id='chart-3'),
            ],
            style={
                "width": "100%",
                "min-height": "500px",
                "background-color": "lightgrey",
                "display": "grid",
                "place-items": "center",
            },
        ),
    ],
    style={
        "display": "grid",
        "grid-template-columns": "1fr 1fr",
        "gap": "1rem",
    },
)

three_charts = html.Div(
    id="homepage-two-charts",
    children=[
        html.Div(
            children=[ChartContainer(id='chart-4')],
            style={
                "width": "100%",
                "min-height": "500px",
                "background-color": "lightgrey",
                "display": "grid",
                "place-items": "center",
            },
        ),
        html.Div(
            children=[ChartContainer(id='chart-5')],
            style={
                "width": "100%",
                "min-height": "500px",
                "background-color": "lightgrey",
                "display": "grid",
                "place-items": "center",
            },
        ),
        html.Div(
            children=[ChartContainer(id='chart-6')],
            style={
                "width": "100%",
                "min-height": "500px",
                "background-color": "lightgrey",
                "display": "grid",
                "place-items": "center",
            },
        ),
    ],
    style={
        "display": "grid",
        "grid-template-columns": "1fr 1fr 1fr",
        "gap": "1rem",
    },
)

# ----------------------------------------------------------------------------#
# Layout

layout = html.Div(
    id="homepage-layout",
    children=[
        page_title,
        text_block,
        full_width_chart,
        two_charts,
        three_charts,
    ],
    style={
        # Place content in one column with a vertical gap of 1rem between each
        # element
        "display": "grid",
        "gap": "1rem", 
    }
)
