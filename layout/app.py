import dash
from dash import html, dcc
from login import login_layout
from callbacks import register_callbacks
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', children=[
        login_layout,
    ])
])

register_callbacks(app)


if __name__ == "__main__":
    app.run_server(debug=True)
