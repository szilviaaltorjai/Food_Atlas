import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

########### Define your variables ######

tabtitle = 'the district'
myheading1 = 'Food Atlas'
myheading2 = 'Diabetes in US counties'
image1 = 'Hist_diabetes.jpg'
image2 = 'Pov_diabetes.jpg'
image3 = 'Diabetes_Pov_Foodtax.jpg'
sourceurl = 'https://www.ers.usda.gov'
githublink = 'https://github.com/szilviaaltorjai/Food_Atlas'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading1),
    html.H2(myheading2),
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url(image1), style={'width': '75%', 'height': 'auto'})
        ],className='four columns'),
        html.Div([
            html.Img(src=app.get_asset_url(image2), style={'width': '75%', 'height': 'auto'}),
        ],className='four columns'),
        html.Div([
            html.Img(src=app.get_asset_url(image3), style={'width': '75%', 'height': 'auto'})
        ],className='four columns'),
    ],className='twelve columns'),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
