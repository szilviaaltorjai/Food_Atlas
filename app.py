import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

########### Define your variables ######

tabtitle = 'Diabetes in US counties, 2013'
myheading = 'Scatterplot of diabetes prevalence among adults and pverty rate in US counties'
color1='#04F9E6'
color2='#1B03B1'
sourceurl = 'https://www.kaggle.com/christophercorrea/dc-residential-properties/'
githublink = 'https://github.com/szilviaaltorjai/Food_Atlas'

#### Prepare dataframe

df = pd.read_csv('Food_clean.csv')

#### Set up the chart
trace = go.Scatter(
    x=df['POVRATE15'],
    y=df['PCT_DIABETES_ADULTS13'],
    mode = 'markers',
    marker=dict(
        size=8,
        color=df['FOOD_TAX14'],
        colorscale=[color1, color2],
        colorbar=dict(title='Food tax'),
        showcase=True
    )
)

data=[trace]
layout = go.Layout(
    title=f'Poor areas have both higher diabetes prevalence and higher food taxes.',
    xaxis=dict(title = 'Poverty rate'),
    yaxis=dict(title = 'Proportion of adults with diabetes'),
    hovermode = 'closest'
)

fig=go.Figure(data=data, layout=layout)

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='FoodAtlas'

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
