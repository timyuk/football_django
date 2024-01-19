import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

app = dash.Dash(__name__)

# Sample data for demonstration
teams = ["Team 1", "Team 2", "Team 3", "Team 4", "Team 5", "Team 6", "Team 7", "Team 8"]

# Define the initial bracket structure
initial_bracket = {
    "round1": [(teams[0], teams[1]), (teams[2], teams[3]), (teams[4], teams[5]), (teams[6], teams[7])],
    "round2": [("", ""), ("", "")],
    "champion": ("", "")
}

# Create the initial figure with empty data
fig = go.Figure()

# Function to update the bracket based on user input
def update_bracket(selected_match, winner):
    # Update the winner in the bracket data
    round_name, match_index = selected_match.split("_")
    match_index = int(match_index)
    initial_bracket[round_name][match_index] = winner

    # Update the figure with the new bracket data
    fig.update_traces(text=sum(initial_bracket.values(), []))

# Layout of the app
app.layout = html.Div([
    dcc.Graph(
        id='tournament-bracket',
        figure=fig
    ),
    html.Label("Select a match winner:"),
    dcc.Dropdown(
        id='winner-dropdown',
        options=[
            {'label': team, 'value': team} for team in teams
        ],
        value=''
    ),
    html.Button('Submit Winner', id='submit-button')
])

# Callback to update the bracket when a winner is selected
@app.callback(
    Output('tournament-bracket', 'figure'),
    [Input('submit-button', 'n_clicks')],
    [Input('winner-dropdown', 'value')]
)
def update_graph(n_clicks, winner):
    if n_clicks is not None and winner:
        # Get the selected match from the button ID
        selected_match = dash.callback_context.triggered[0]['prop_id'].split('.')[0]
        update_bracket(selected_match, winner)

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
