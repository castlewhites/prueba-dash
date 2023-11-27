import dash_bootstrap_components as dbc

navbar_layout = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("GRAFICA 1", href="/pagina")),
        dbc.NavItem(dbc.NavLink("GRAFICA 2", href="/hola")),
        dbc.NavItem(dbc.NavLink("GRAFICA 3", href="/")),
    ],

    brand="PRUEBA",
    brand_href="#",
    color="#C8BBE4",
    dark=True,
)