from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

# Read the processed data
df = pd.read_csv("formatted_output.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Sort data by date
df = df.sort_values("Date")

# Create line chart
fig = px.line(
    df,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time",
    labels={
        "Date": "Date",
        "Sales": "Sales"
    }
)

fig.add_vline(
    x="2021-01-15",
    line_dash="dash",
    line_color="red"
)

fig.add_annotation(
    x="2021-01-15",
    y=df["Sales"].max(),
    text="Price Increase",
    showarrow=True,
    arrowhead=2
)

# Create Dash app
app = Dash(__name__)

# Dashboard layout
app.layout = html.Div([
    html.H1("Pink Morsel Sales Dashboard"),

    dcc.Graph(
        figure=fig
    )
])

# Run the application
if __name__ == "__main__":
    app.run(debug=True)