import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output

# Load dataset
data_path = r"C:\Users\disha\Desktop\AQI_Analysis_India\Dataset\city_day.csv"

df = pd.read_csv(data_path)
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df = df.dropna(subset=["AQI", "City", "Date"]).copy()
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.to_period("M").astype(str)

cities = sorted(df["City"].unique())

# Dashboard colors
BG = "#0B1220"
CARD = "#151F32"
TEXT = "#F1F5F9"
MUTED = "#94A3B8"
ACCENT = "#38BDF8"

app = Dash(__name__)
app.title = "India AQI Analytics"

def make_card(title, component_id):
    return html.Div([
        html.P(title, style={"color": MUTED, "margin": "0"}),
        html.H2(id=component_id, style={"color": TEXT, "margin": "10px 0"})
    ], style={
        "backgroundColor": CARD,
        "padding": "20px",
        "borderRadius": "14px",
        "flex": "1",
        "minWidth": "150px"
    })

def graph_card(component_id):
    return dcc.Graph(
        id=component_id,
        config={"displayModeBar": False},
        style={"height": "350px"}
    )

app.layout = html.Div([
    html.Div([
        html.H1("INDIA AQI ANALYTICS", style={
            "color": TEXT, "marginBottom": "5px"
        }),
        html.P("Air Quality Monitoring & Pollution Insights",
               style={"color": MUTED, "marginTop": "0"})
    ]),

    html.Div([
        html.Label("Select City", style={"color": TEXT}),
        dcc.Dropdown(
            id="city-dropdown",
            options=[{"label": "All Cities", "value": "All"}] +
                    [{"label": c, "value": c} for c in cities],
            value="All",
            clearable=False,
            style={"color": "#111827", "marginTop": "8px"}
        ),
        html.Br(),
        html.Label("Select Year", style={"color": TEXT}),
        dcc.Dropdown(
            id="year-dropdown",
            options=[{"label": "All Years", "value": "All"}] +
                    [{"label": str(y), "value": y}
                     for y in sorted(df["Year"].unique())],
            value="All",
            clearable=False,
            style={"color": "#111827", "marginTop": "8px"}
        )
    ], style={
        "backgroundColor": CARD,
        "padding": "20px",
        "borderRadius": "14px",
        "marginBottom": "20px"
    }),

    html.Div([
        make_card("Average AQI", "avg-aqi"),
        make_card("Maximum AQI", "max-aqi"),
        make_card("Cities Covered", "city-count"),
        make_card("Total Records", "record-count")
    ], style={
        "display": "flex",
        "gap": "15px",
        "flexWrap": "wrap",
        "marginBottom": "20px"
    }),

    html.Div([
        html.Div(graph_card("aqi-trend"), style={
            "backgroundColor": CARD, "borderRadius": "14px", "padding": "10px"
        }),
        html.Div(graph_card("city-chart"), style={
            "backgroundColor": CARD, "borderRadius": "14px", "padding": "10px"
        }),
        html.Div(graph_card("category-chart"), style={
            "backgroundColor": CARD, "borderRadius": "14px", "padding": "10px"
        }),
        html.Div(graph_card("pollutant-chart"), style={
            "backgroundColor": CARD, "borderRadius": "14px", "padding": "10px"
        }),
        html.Div(graph_card("monthly-chart"), style={
            "backgroundColor": CARD, "borderRadius": "14px", "padding": "10px"
        }),
        html.Div(graph_card("scatter-chart"), style={
            "backgroundColor": CARD, "borderRadius": "14px", "padding": "10px"
        })
    ], style={
        "display": "grid",
        "gridTemplateColumns": "repeat(auto-fit, minmax(320px, 1fr))",
        "gap": "18px"
    }),

    html.P(
        "Project: AQI Analysis of India | Python, Pandas, Plotly & Dash",
        style={"color": MUTED, "textAlign": "center", "marginTop": "25px"}
    )
], style={
    "backgroundColor": BG,
    "minHeight": "100vh",
    "padding": "28px",
    "fontFamily": "Arial, sans-serif"
})


@app.callback(
    [
        Output("avg-aqi", "children"),
        Output("max-aqi", "children"),
        Output("city-count", "children"),
        Output("record-count", "children"),
        Output("aqi-trend", "figure"),
        Output("city-chart", "figure"),
        Output("category-chart", "figure"),
        Output("pollutant-chart", "figure"),
        Output("monthly-chart", "figure"),
        Output("scatter-chart", "figure")
    ],
    [
        Input("city-dropdown", "value"),
        Input("year-dropdown", "value")
    ]
)
def update_dashboard(selected_city, selected_year):

    filtered = df.copy()

    if selected_city != "All":
        filtered = filtered[filtered["City"] == selected_city]

    if selected_year != "All":
        filtered = filtered[filtered["Year"] == selected_year]

    if filtered.empty:
        empty_fig = go.Figure()
        empty_fig.update_layout(
            title="No data available",
            paper_bgcolor=CARD,
            plot_bgcolor=CARD,
            font_color=TEXT
        )
        return ("N/A", "N/A", "0", "0",
                empty_fig, empty_fig, empty_fig,
                empty_fig, empty_fig, empty_fig)

    avg_aqi = f"{filtered['AQI'].mean():.1f}"
    max_aqi = f"{filtered['AQI'].max():.0f}"
    city_count = str(filtered["City"].nunique())
    record_count = f"{len(filtered):,}"

    # 1. Yearly AQI trend
    yearly = filtered.groupby("Year", as_index=False)["AQI"].mean()
    fig1 = px.line(
        yearly, x="Year", y="AQI", markers=True,
        title="Yearly Average AQI Trend"
    )

    # 2. Top 10 cities
    city_data = filtered.groupby("City", as_index=False)["AQI"].mean()
    city_data = city_data.nlargest(10, "AQI").sort_values("AQI")
    fig2 = px.bar(
        city_data, x="AQI", y="City", orientation="h",
        title="Top 10 Cities by Average AQI"
    )

    # 3. AQI category distribution
    if "AQI_Bucket" in filtered.columns:
        category_data = filtered["AQI_Bucket"].value_counts().reset_index()
        category_data.columns = ["Category", "Records"]
        fig3 = px.pie(
            category_data, names="Category", values="Records",
            hole=0.55, title="AQI Category Distribution"
        )
    else:
        fig3 = go.Figure()

    # 4. Average pollutant levels
    pollutants = [
        p for p in ["PM2.5", "PM10", "NO2", "SO2", "CO", "O3"]
        if p in filtered.columns
    ]
    pollutant_data = filtered[pollutants].mean().reset_index()
    pollutant_data.columns = ["Pollutant", "Average Level"]
    fig4 = px.bar(
        pollutant_data, x="Pollutant", y="Average Level",
        title="Average Pollutant Levels"
    )

    # 5. Monthly AQI trend
    monthly = filtered.groupby("Month", as_index=False)["AQI"].mean()
    fig5 = px.area(
        monthly, x="Month", y="AQI",
        title="Monthly Average AQI Trend"
    )

    # 6. PM2.5 vs AQI scatter plot
    if "PM2.5" in filtered.columns:
        scatter_data = filtered.dropna(subset=["PM2.5"])
        fig6 = px.scatter(
            scatter_data, x="PM2.5", y="AQI",
            opacity=0.45, title="PM2.5 vs AQI"
        )
    else:
        fig6 = go.Figure()

    # Consistent dashboard styling
    for fig in [fig1, fig2, fig3, fig4, fig5, fig6]:
        fig.update_layout(
            paper_bgcolor=CARD,
            plot_bgcolor=CARD,
            font_color=TEXT,
            title_font_size=17,
            margin=dict(l=20, r=20, t=55, b=25)
        )

    return (
        avg_aqi, max_aqi, city_count, record_count,
        fig1, fig2, fig3, fig4, fig5, fig6
    )


if __name__ == "__main__":
    app.run(debug=True)