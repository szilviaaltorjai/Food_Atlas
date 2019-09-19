import dash
import dash_core_components as dcc
import dash_html_components as html
import os

########### Define your variables ######

list_of_choices=['Distribution of adults with diabetes', 'Daibetes and poverty in US counties', 'Diabetes, poverty and food tax']
githublink = 'https://github.com/szilviaaltorjai/Food_Atlas'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='FoodAtlas'

########### Set up the layout
app.layout = html.Div([
    html.H2('Food Atlas in the US'),
    html.Img(src=app.get_asset_url(image1), style={'width': 'auto', 'heights': '10%'}),
    dcc.Dropdown(id='your-input-here',
                options=[{'label': i, 'value': i} for i in list_of_choices],
                value='Diabetes, poverty and food tax',
                style={'width': '500px'}),
    html.Br(),
    html.Div(id='your-output-here', children=''),
    html.Br(),
    html.A('Code on Github'', href=githublink),

])

############### Interactive callback comes here
@app.callback(dash.dependencies.Output('your-output-here', 'children'),
                [dash.dependencies.Input('your-input-here', 'value')])
def display_value(whatever_you_chose):
    return f'Food Atlas shows {whatever_you_chose}.'

############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)
