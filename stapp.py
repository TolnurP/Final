import streamlit as st
import streamlit.components.v1 as components
import altair as alt
import pandas as pd

st.set_page_config(layout="wide")
detail_df = pd.DataFrame(pd.read_csv('Bali Popular Destination for Tourist 2022 - Sheet.csv'))

name_of_the_city = list(detail_df['Place'].unique())
##header info
st.title("Famous Bali Destination details")

##Sidebar info
st.sidebar.header("Select a location")
selected_city = st.sidebar.selectbox("Select The City", detail_df['Place'])

##mainpage

mPlace = detail_df[(detail_df['Place'] == selected_city)]
mLocation = mPlace['Location'].values[0]
mCoordinates = mPlace['Coordinate'].values[0]
mMapsRating = mPlace['Google Maps Rating'].values[0]
mMapsReviews = mPlace['Google Reviews (Count)'].values[0]
mSource = mPlace['Source'].values[0]
mDescription = mPlace['Description'].values[0]
mTouristVisitFee = mPlace['Tourism/Visitor Fee (approx in USD)'].values[0]
mMapsEmbed = mPlace['MapsEmbed'].values[0]
mLocationImage = mPlace['LocationImage'].values[0]

col1,col2 = st.columns([8,4])
with col1:
    st.image(mLocationImage,width=600)
with col2:
    st.header(selected_city)
    st.text(" \n")
    st.text(" \n")
    st.subheader("Address")
    st.write(mLocation)
    st.text(" \n")
    st.text(" \n")
    st.subheader("Google Rating")
    st.write(mMapsRating)
col3, col4 = st.columns([8,4])
with col3:

    st.header("Location on map")
    st.components.v1.iframe(mMapsEmbed, width=600, height=600, scrolling=False)
with col4:
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")
    st.text(" \n") 
    st.header("Short Description of the location")
    st.text(" \n")
    st.write(mDescription)
    st.header("Fee and Payment Info")
    st.text(" \n")
    st.write(mTouristVisitFee)
# st.write(mPlace)
# st.write(mLocation)
# st.write(mCoordinates)
# st.write(mMapsRating)
# st.write(mMapsReviews)
# st.write(mSource)
# st.write(mDescription)
# st.write(mTouristVisitFee)

# st.image(mLocationImage,width=800)
# st.write(selected_city)
# st.title("Welcome to the app")
# option = st.selectbox("Select The City", detail_df['Place'])

# st.write(option)