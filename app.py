import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

########### Define your variables ######

tabtitle = 'Diabetes and poverty'
myheading='Scatter of diabetes and poverty in US counties'
color1='#04F9E6'
color2='#1B03B1'
sourceurl = 'https://www.kaggle.com/christophercorrea/dc-residential-properties/'
githublink = 'https://github.com/szilviaaltorjai/Food_Atlas'

########### Prepare the dataframe
df = pd.read_csv('Food_clean.csv')

########### Set up the chart
trace = go.Scatter(
    x = df['POVRATE15'],
    y = df['PCT_DIABETES_ADULTS13'],
    mode = 'markers',
    marker=dict(
        size=8,
        color = df['FOOD_TAX14'], # set color equal to a third variable
        colorscale=[color1, color2],
        colorbar=dict(title='Food tax'),
        showscale=True
    )
)

data = [trace]
layout = go.Layout(
    title = 'Scatterplot of poverty rates and proportion of adults with diabetes, US counties', # Graph title
    xaxis = dict(title = 'Poverty rates'), # x-axis label
    yaxis = dict(title = 'Proportion of adults with diabetes'), # y-axis label
    hovermode ='closest' # handles multiple points landing on the same vertical
)
fig = go.Figure(data=data, layout=layout)

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

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
