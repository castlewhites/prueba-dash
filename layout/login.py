import dash
from dash import html
import dash_bootstrap_components as dbc

login_layout = html.Div([
    dbc.Container(
        dbc.Row(
            dbc.Col(
                html.Div(
                    [
                        
                        html.H2("LOGIN", style={"textAlign": "center", "color": "#fff", "fontWeight": "bold"} ),
                        html.Br(),
                        dbc.Input(type="text", id="username", placeholder="Username"),
                        html.Br(),
                        dbc.Input(type="password", id="password", placeholder="Password"),
                        html.Div(id="login-output"),
                        html.Br(),
                        dbc.Button("Sign In", id="login-button", n_clicks=0, style={"background": "#959095", "border": "none", "color": "black", "borderRadius": "20px"}),
                    ],
                    className="d-grid gap-2 col-6 mx-auto",
                    style={'max-width': '400px', 'margin': 'auto', "background": "#C8BBE4", "padding": "30px 40px", "borderRadius": "7%"}
                ),
                width={"size": 6, "offset": 3},
                className="mt-5",
            ),
        )
    )
])
