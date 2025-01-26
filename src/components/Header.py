# Header component that persists across all pages

from dash import html
import dash_mantine_components as dmc

from theme.theme import theme

#----------------------------------------------------------------------------#
# Component

def Header(app_title: str) -> html.Div:
    """
    Header has a hamburger dropdown on the far left that expands to show the
    page navigation links. The app title is next to the hamburger menu.
    """

    hamburger_menu = dmc.Burger(
        id='hamburger-menu',
        color=theme['white'],
        style={
            'margin': '1rem',
        }
    )

    app_title = html.H1(
        app_title,
        id='app-title',
        style={
            'color': theme['white'],
            'margin': '1rem',
        }
        )

    header = html.Div(
        id='header',
        children=[hamburger_menu, app_title],
        style={
            'background-color': theme['colors']['primary'][0],
            'display': 'flex',
            'align-items': 'center',
            'justify-content': 'flex-start',
            'min-height': '64px',
        }

    )

    return header
#----------------------------------------------------------------------------#
# Callbacks