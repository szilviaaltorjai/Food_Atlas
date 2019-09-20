import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

########### Define your variables ######

tabtitle = 'Diabetes in US counties, 2013'
myheading = 'Scatterplot of diabetes prevalence among adults and poverty rate in US counties'
color1='blue'
sourceurl = 'https://www.ers.usda.gov'
githublink = 'https://github.com/szilviaaltorjai/Food_Atlas'

#### Prepare dataframe

df = pd.read_csv('Food_clean.csv')
df = df['POVRATE15']
df = df['PCT_DIABETES_ADULTS13']

#### Set up the chart
trace = go.Scatter(
    x=df['POVRATE15'],
    y=df['PCT_DIABETES_ADULTS13'],
    mode = 'markers',
    )

data=[trace]
layout = go.Layout(
    title=f'Scatterplot of poverty rates and proportion of adults with diabetes, US counties',
    xaxis=dict(title = 'Poverty rates'),
    yaxis=dict(title = 'Proportion of adults with diabetes'),
    hovermode = 'closest'
)

fig=go.Figure(data=data, layout=layout)

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
    app.run
