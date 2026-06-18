import streamlit as st
import pandas as pd

st.title("Heritage Map Dashboard")

df = pd.read_csv("data/sites1.csv")
df = df.rename(columns={'Latitude': 'lat', 'Longitude': 'lon'})

# --- Sidebar Interaction ---
st.sidebar.header("Filter Options")
selected_state = st.sidebar.selectbox("Select State:", df['State'].unique())

# Filter the data
filtered_df = df[df['State'] == selected_state]

st.write(f"Showing sites in: {selected_state}")
import pydeck as pdk

# Configure the map to show markers with names
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=20.5937,
        longitude=78.9629,
        zoom=4,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=filtered_df,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=20000,
            pickable=True,
        ),
    ],
    tooltip={"text": "{Name}"} # This makes the site name appear when you hover!
))