import dash
from dash.dependencies import Input, Output, State
from dash import html
from login import login_layout
from dashboard import dashboard_layout

def register_callbacks(app):
    @app.callback(
        [Output('page-content', 'children'),
         Output("login-output", "children"),
         Output('url', 'pathname')],
        [Input("login-button", "n_clicks")],
        [State("username", "value"), State("password", "value")]
    )
    def display_dashboard(n_clicks, username, password):
        if n_clicks > 0:
            if username == "usuario" and password == "123":
                return dashboard_layout, html.Div("Login exitoso", style={'color': 'green'}), '/dashboard'
            else:
                return login_layout, html.Div("Credenciales incorrectas", style={'color': 'red'}), '/'
        else:
            return login_layout, None, '/'


    def display_page(pathname):
        if pathname == '/dashboard':
            return dashboard_layout
        elif pathname == '/page1':
            return html.Div("Contenido de la Página 1")
        elif pathname == '/page2':
            return html.Div("Contenido de la Página 2")
        else:
            return login_layout
