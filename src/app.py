#----------------------------------------------------------------------------#
#
#                                   Dash App
#
#----------------------------------------------------------------------------#

# Libraries
import dash
from dash import Dash, html

app = Dash(__name__, use_pages=True)

#----------------------------------------------------------------------------#
# main method

app.layout = html.Div(
    id="app-layout",
    children=[
        html.H1("Dash App"),
        html.A("Homepage", href="/"),
        html.A("Other Page", href="/other_page"),
        html.Div(id="page-content"),
        dash.page_container,
    ],
)

#----------------------------------------------------------------------------#

if __name__ == '__main__':
    app.run(debug=True)