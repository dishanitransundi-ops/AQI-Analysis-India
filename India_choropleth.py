
import pandas as pd
import plotly.express as px

# 1. Load the dataset
file_path = r"C:\Users\disha\Desktop\AQI_Analysis_India\Dataset\city_day.csv"

df = pd.read_csv(file_path)

# 2. Map cities to their respective states
city_state = {
    "Ahmedabad": "Gujarat",
    "Aizawl": "Mizoram",
    "Amaravati": "Andhra Pradesh",
    "Amritsar": "Punjab",
    "Bengaluru": "Karnataka",
    "Bhopal": "Madhya Pradesh",
    "Brajrajnagar": "Odisha",
    "Chandigarh": "Chandigarh",
    "Chennai": "Tamil Nadu",
    "Coimbatore": "Tamil Nadu",
    "Delhi": "Delhi",
    "Ernakulam": "Kerala",
    "Gurugram": "Haryana",
    "Guwahati": "Assam",
    "Hyderabad": "Telangana",
    "Jaipur": "Rajasthan",
    "Jorapokhar": "Jharkhand",
    "Kochi": "Kerala",
    "Kolkata": "West Bengal",
    "Lucknow": "Uttar Pradesh",
    "Mumbai": "Maharashtra",
    "Patna": "Bihar",
    "Shillong": "Meghalaya",
    "Talcher": "Odisha",
    "Thiruvananthapuram": "Kerala",
    "Visakhapatnam": "Andhra Pradesh"
}

# 3. Add State column using city mapping
df["State"] = df["City"].map(city_state)

# 4. Remove rows with missing AQI or State
df = df.dropna(subset=["AQI", "State"])

# 5. Calculate average AQI for each state
state_aqi = (
    df.groupby("State", as_index=False)["AQI"]
    .mean()
    .round(2)
)

print("State-wise AQI data:")
print(state_aqi)

# 6. Load India state boundary map
geojson_url = (
    "https://raw.githubusercontent.com/"
    "geohacker/india/master/state/india_state.geojson"
)

# 7. Create Choropleth Map
fig = px.choropleth(
    state_aqi,
    geojson=geojson_url,
    featureidkey="properties.NAME_1",
    locations="State",
    color="AQI",
    color_continuous_scale="RdYlGn_r",
    hover_name="State",
    hover_data={"AQI": ":.2f"},
    title="State-wise Average AQI in India"
)

# 8. Improve map appearance
fig.update_geos(
    fitbounds="locations",
    visible=False
)

fig.update_layout(
    title_x=0.5,
    template="plotly_dark",
    height=700,
    coloraxis_colorbar_title="Average AQI"
)

# 9. Display map
fig.show()

# 10. Save map as HTML
fig.write_html("India_AQI_Choropleth_Map.html")

print("Choropleth map created successfully!")
