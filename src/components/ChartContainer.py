from dash import html, dcc


def ChartContainer(id: str) -> html.Div:
    """
    Return a div that is a grid container for a chart.
    """
    return html.Div(
        id=id,
        style={
            "display": "grid",
            "width": "100%",
            "height": "100%",
            "padding": ".25rem",
        },
    )
