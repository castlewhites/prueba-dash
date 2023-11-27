import dash
from dash.dependencies import Input, Output, State
from dash import html
from login import login_layout
from dashboard import dashboard_layout
from pagina import pagina_layout

def register_callbacks(app):
    @app.callback(
        [Output('page-content', 'children'),
         Output("login-output", "children"),
         Output('url', 'pathname')],
        [Input("login-button", "n_clicks")],
        [State("username", "value"), State("password", "value"), State('url', 'pathname')]
    )
    def display_dashboard(n_clicks, username, password, pathname):
        accessed_user = False
        print(f"pathname: {pathname}") 

        if n_clicks > 0:
            if username == "usuario" and password == "123":
                accessed_user = True
                pathname = "/dashboard"
            else:
                return login_layout, html.Div("Credenciales incorrectas", style={'color': 'red'}), '/'
            
        if accessed_user:
            if pathname == "/dashboard":
                return dashboard_layout, None, '/dashboard'
            elif pathname == "/pagina":
                print(f"pathname2: {pathname}") 
                return pagina_layout, None, "/pagina"  
        else:
            return login_layout, None, '/'
