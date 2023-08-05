import dash
from dash import dcc
from dash import html
import pickle


# Load the saved model from a file
with open('tree_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define your Dash app
app = dash.Dash(__name__)

# Define your input and output components
app.layout = html.Div([
    dcc.Input(id='GrAppv', type='number', placeholder='Enter GrAppv'),
    dcc.Input(id='Term', type='number', placeholder='Enter Term'),
    dcc.Input(id='NoEmp', type='number', placeholder='Enter NoEmp'),
    dcc.Input(id='NewExist', type='number', placeholder='Enter NewExist'),
    dcc.Input(id='UrbanRural', type='text', placeholder='Enter UrbanRural'),
    dcc.Input(id='Industry', type='text', placeholder='Enter Industry'),
    dcc.Graph(id='output')
])

# Define your callback function
@app.callback(
    dash.dependencies.Output('output', 'figure'),
    [dash.dependencies.Input('GrAppv', 'value'),
     dash.dependencies.Input('Term', 'value'),
     dash.dependencies.Input('NoEmp', 'value'),
     dash.dependencies.Input('NewExist', 'value'),
     dash.dependencies.Input('UrbanRural', 'value'),
     dash.dependencies.Input('Industry', 'value')]
)
def update_output(GrAppv, Term, NoEmp, NewExist, UrbanRural, Industry):
    
    # Pass the input data through the loaded model
    input_data = [[GrAppv, Term, NoEmp, NewExist, UrbanRural, Industry]]
    prediction = model.predict(input_data)
    # Allow user input for loan application
    dcc.subheader("Classify your Loan Application in Seconds")
    GrAppv = dcc.number_input("Loan Amount")
    Term = dcc.number_input("Loan Term")
    NewExist = dcc.text_input("How long has the business been in operation?")
    Location = dcc.selectbox("Where is the business located?", ["Urban", "Rural"])
    if Location == 'Urban':
        UrbanRural = 1
    else:
        UrbanRural = 2
    NoEmp = dcc.selectbox("Number of employees?", [1, 5, 10, 20, 50, 100])
    

    
    
    # Update the graph output component with the prediction results
    return fig

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)