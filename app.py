from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("formatted_output.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

app = Dash(__name__)

app.layout = html.Div(

    style={
        "backgroundColor": "#F5F7FA",
        "padding": "30px",
        "fontFamily": "Arial"
    },

    children=[

        html.H1(
            "Pink Morsel Sales Dashboard",
            style={
                "textAlign": "center",
                "color": "#2C3E50"
            }
        ),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "South", "value": "south"},
                {"label": "East", "value": "east"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True,
            style={
                "marginBottom": "20px",
                "textAlign": "center"
            }
        ),

        dcc.Graph(id="sales-chart")

    ]
)


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)

def update_graph(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"] == selected_region]

    fig = px.line(
        filtered_df,
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
        y=filtered_df["Sales"].max(),
        text="Price Increase",
        showarrow=True
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)