import dash_bootstrap_components as dbc

pagina_layout = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("GRAFICA 1", href="/pagina")),
      
    ],

    brand="pagina2",
    brand_href="#",
    color="#C8BBE4",
    dark=True,
)