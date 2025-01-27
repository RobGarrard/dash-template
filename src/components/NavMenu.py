import dash
from dash import html, Input, Output, callback
import dash_mantine_components as dmc

from theme.theme import theme

import logging
logger = logging.getLogger(__name__)

#----------------------------------------------------------------------------#
# Component

def NavMenu() -> html.Div:
    """
    NavMenu has a hamburger dropdown on the far left that expands to show the
    page navigation links.
    """

    pages = [(i['name'], i['path']) for i in dash.page_registry.values()]
    logger.info(f"Creating navigation links for pages: {pages}")

    hamburger_menu = dmc.Burger(
            id='hamburger-menu',
            color=theme['white'],
        )
    
    nav_links = html.Div(children=[
        dmc.Menu(
            [
                dmc.MenuTarget(hamburger_menu),
                dmc.MenuDropdown(
                    [
                        dmc.MenuItem(
                            name,
                            href=path,
                            style={
                                'fontSize': '1.25rem',
                                'fontWeight': '600',
                            },
                        )
                        for name, path in pages
                        ]
                    ),
                ],
            ),
        ],
        style={"display": "flex", "align-items": "center"},
    )

    return nav_links

#----------------------------------------------------------------------------#
# Callbacks 

# When the hamburger menu gets clicked, by default it changes to an X. Then
# changes back to a hamburger. Prevent this from happening, always leave it as
# a hamburger.

@callback(
    Output('hamburger-menu', 'opened'),
    Input('hamburger-menu', 'opened'),
)
def keep_hamburger_menu_open(open):
    return False