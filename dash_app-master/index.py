import dash
from flask import Flask
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from app import App, build_graph
from homepage import Homepage

server = Flask(__name__)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED], server=server,url_base_pathname='/app1/')
app2 = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED], server=server,url_base_pathname='/app2/')
app2.layout = html.H1('App 2')


app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),
    html.Div(id = 'page-content')
])

@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/time-series':
        return App()
    else:
        return Homepage()

@app.callback(
    Output('output', 'children'),
    [Input('pop_dropdown', 'value')]
)
def update_graph(city):
    graph = build_graph(city)
    return graph

server.run()


