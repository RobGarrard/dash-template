from dash import Output, Input, callback, dcc
import plotly.express as px

import pandas as pd

import logging
logger = logging.getLogger(__name__)

import datetime

@callback(
    Output('chart-1', 'children'),
    Input('cached-data', 'data'),
)
def update_chart_1(data):
    """
    Time series chart of profit vs year-month
    """

    df = pd.DataFrame(data)


    # This you'd put in some utilities logic
    # Drop duplicates on Year and Month
    df = df.drop_duplicates(subset=['Year', 'Month'])

    # Concat the strings of Year and Month
    def month_str_to_num(month_str):
        datetime_object = datetime.datetime.strptime(month_str, "%B")
        return datetime_object.month
    
    df['Month'] = df['Month'].apply(lambda x: f"{month_str_to_num(x):02d}")
    df['Year-Month'] = df['Year'].astype(str) + '-' + df['Month']

    # Create the chart
    chart = px.line(df, x='Year-Month', y='Profit', title='Profit vs Month')

    return dcc.Graph(figure=chart)

@callback(
    Output('chart-2', 'children'),
    Input('cached-data', 'data'),
)
def update_chart_2(data):
    logger.info(f"Updating chart 2.")
    
    df = pd.DataFrame(data)

    chart = px.histogram(df, x='Age', title='Distribution of Age')

    return dcc.Graph(figure=chart)

@callback(
    Output('chart-3', 'children'),
    Input('cached-data', 'data'),
)
def update_chart_4(data):
    logger.info(f"Updating chart 4.")
    
    df = pd.DataFrame(data)

    chart = px.histogram(df, x='Sale Price', title='Distribution of Sale Price')

    return dcc.Graph(figure=chart)
