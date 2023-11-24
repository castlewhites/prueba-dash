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
        [State("username", "value"), State("password", "value"),
         State('url', 'pathname')] 
    )
    def display_content(n_clicks, username, password, pathname):
        if dash.callback_context.triggered_id is None:
            # La callback se llama por primera vez
            return login_layout, None, '/'
        
        # La callback fue desencadenada por algún evento
        triggered_component = dash.callback_context.triggered_id.split('.')[0]

        if triggered_component == 'url':
            # La callback fue desencadenada por el cambio de la URL
            if pathname == '/dashboard':
                return dashboard_layout, None, '/dashboard'
            elif pathname == '/page1':
                return pagina_layout, None, '/pagina1'
            elif pathname == '/page2':
                return html.Div("Contenido de la Página 2"), None, '/page2'
            else:
                return login_layout, None, '/'
        elif triggered_component == 'login-button':

            if username == "usuario" and password == "123":
                return dashboard_layout, html.Div("Login exitoso", style={'color': 'green'}), '/dashboard'
            else:
                return login_layout, html.Div("Credenciales incorrectas", style={'color': 'red'}), '/'
        else:
    
            return login_layout, None, '/'
