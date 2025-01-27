# Footer component that persists across all pages

from dash import html
import dash_mantine_components as dmc

from theme.theme import theme

#----------------------------------------------------------------------------#
# Component

def Footer() -> html.Div:
    """
    Grey background. Has company logo in bottom left.
    """

    company_logo = html.Img(
        src='assets/company_logo.svg',
        alt='Company Logo',
        style={
            'max-height': '3rem',
            'display': 'block',
            'margin': 'auto 0',
            'padding': '4px',
        }
    )

    footer = html.Div(
        id='footer',
        children=[company_logo],
        style={
            'background-color': theme['colors']['gray'][0],
            'display': 'flex',
            'align-items': 'center',
            'justify-content': 'flex-start',
            'padding': '0 1rem',
        }

    )

    return footer
#----------------------------------------------------------------------------#
# Callbacks