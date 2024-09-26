from dash import Dash, dcc, html, Input, Output

# Create the Dash app
app = Dash(__name__)
server = app.server

# Layout of the app
app.layout = html.Div([html.H1("✌️يا هلا بالشباب✌️\n"),
                    #    html.Br(),
                        dcc.Input(id='input-text-1', value='ذكر ام انثي؟', type='text'),
                        dcc.Input(id='input-text-2', value='Your name', type='text'),
                        html.Br(), # line break
                        html.Br(),
                        html.Div(id='output-text')
])

# Define the callback function
@app.callback(
    Output('output-text', 'children'),  # What gets updated
    Input('input-text-1', 'value'),     # First input trigger
    Input('input-text-2', 'value')      # Second input trigger
)
def update_output(input1, input2):
    if input1.lower()=="m" or input1.lower()=="male":
        title="Mr"
    elif input1.lower()=="f" or input1.lower()=="female":
        title="Miss"
    else:
        title=" "
    return f'Hello to your 1st web app, {title} {input2} 😊😊😊'

# Run the app
if __name__ == '__main__': # the main() function will execute only if the script is run directly.
    app.run_server(debug=True)
