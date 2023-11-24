import dash_bootstrap_components as dbc

pagina_layout = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("GRAFICA 1", href="/pagina1")),
        dbc.NavItem(dbc.NavLink("GRAFICA 2", href="/hola")),
        dbc.NavItem(dbc.NavLink("GRAFICA 3", href="/")),
    ],

    brand="pagina2",
    brand_href="#",
    color="#C8BBE4",
    dark=True,
)