# Header component that persists across all pages

from dash import html
import dash_mantine_components as dmc

from theme.theme import theme

from .NavMenu import NavMenu

#----------------------------------------------------------------------------#
# Component

def Header(app_title: str) -> html.Div:
    """
    Header has a hamburger dropdown on the far left that expands to show the
    page navigation links. The app title is next to the hamburger menu.
    """

    app_title = html.H1(
        app_title,
        id='app-title',
        style={
            'color': theme['white'],
        }
        )

    header = html.Div(
        id='header',
        children=[NavMenu(), app_title],
        style={
            'background-color': theme['colors']['primary'][0],
            'display': 'flex',
            'align-items': 'center',
            'justify-content': 'flex-start',
            'min-height': '32px',
            'gap': '1rem',
            'padding': '0 1rem',
        }

    )

    return header
#----------------------------------------------------------------------------#
# Callbacks