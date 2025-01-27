from dash import Output, Input, callback

import pandas as pd

import logging
logger = logging.getLogger(__name__)


@callback(
    Output('cached-data', 'data'),
    Input('interval', 'n_intervals')
)
def initial_load(_):
    logger.info("Initial load")

    # Read data from our assets location

    df = pd.read_csv("src/assets/ComputerSales.csv")

    logger.info(f"Loaded data: \n {df.head().to_string()}")

    return df.to_dict('records')