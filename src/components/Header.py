# Header component that persists across all pages

from dash import html
import dash_mantine_components as dmc


#----------------------------------------------------------------------------#
# Component

def Header(app_title: str) -> html.Div:
    """
    Header has a hamburger dropdown on the far left that expands to show the
    page navigation links. The app title is next to the hamburger menu.
    """

    hamburger_menu = dmc.Burger(id='hamburger-menu')

    app_title = html.H1(app_title, id='app-title')

    header = html.Div(
        id='header',
        children=[hamburger_menu, app_title]
    )

    return header
#----------------------------------------------------------------------------#
# Callbacks