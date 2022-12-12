#Importing required libraries
import streamlit as st
import streamlit.components.v1 as components
import altair as alt
import pandas as pd

#Loading data into detail_df
detail_df = pd.DataFrame(pd.read_csv('Bali Popular Destination for Tourist 2022 - Sheet.csv'))
#taking the Place name and assigning it to name_of_the_city
name_of_the_city = list(detail_df['Place'].unique())
st.set_page_config(layout="wide")
#This is the Main Page or Information Page
def page1():
    #Setting Title
    st.title("Famous Bali Destination details")
    #Assiging all the values to the variables to use later
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
    #Dividing the page into two columns with 8 and 4 as width parameters
    col1,col2 = st.columns([8,4])
    #Column 1 starts here
    with col1:
        #Loading the image of the place in this area.
        st.image(mLocationImage,width=600)
    #Column 2 starts here
    with col2:
        #Loding the details like address and Maps Rating
        st.header(selected_city)
        st.text(" \n")
        st.text(" \n")
        st.subheader("Address")
        st.write(mLocation)
        st.text(" \n")
        st.text(" \n")
        st.subheader("Google Rating")
        st.subheader(mMapsRating)
    #Initializing another set of column to display it under the above columns
    col3, col4 = st.columns([8,4])
    #Column 3 starts here
    with col3:
        # Loding Google Maps Embedd info into this area
        st.header("Location on map")
        st.components.v1.iframe(mMapsEmbed, width=600, height=600, scrolling=False)
    #Column 4 starts here
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
#This is the Second Page or Visualization Page
def page2():
    #Comparison window to compare two places
    st.title("Famous Bali Destination Visualization")
    st.header("Select the dropdown to compare any two places")
    #Creating a column with 6,6 as width parameter
    col1,col2 = st.columns([6,6])
    #First column which loads first Selected City Details
    with col1:
        first_city = st.selectbox("Select the first city", detail_df["Place"])
        fPlace = detail_df[(detail_df['Place'] == first_city)]
        fDescription = fPlace['Description'].values[0]
        fTouristVisitFee = fPlace['Tourism/Visitor Fee (approx in USD)'].values[0]
        fMapsRating = fPlace['Google Maps Rating'].values[0]
        fMapsReviews = fPlace['Google Reviews (Count)'].values[0]
        st.caption("Description of the location")
        st.write(fDescription)
        st.text(" \n")
        st.caption("Fee and Payment Details")
        st.write(fTouristVisitFee)
        st.text(" \n")
        st.caption("Google Maps Review Count and Rating")
        st.write(fMapsRating, fMapsReviews)
    #Second Column which loads second selected city details
    with col2:
        second_city = st.selectbox("Select the second city", detail_df["Place"],index=2)
        sPlace = detail_df[(detail_df['Place'] == second_city)]
        sDescription = sPlace['Description'].values[0]
        sTouristVisitFee = sPlace['Tourism/Visitor Fee (approx in USD)'].values[0]
        sMapsRating = sPlace['Google Maps Rating'].values[0]
        sMapsReviews = sPlace['Google Reviews (Count)'].values[0]
        st.caption("Description of the location")
        st.write(sDescription)
        st.text(" \n")
        st.caption("Fee and Payment Details")
        st.write(sTouristVisitFee)
        st.text(" \n")
        st.caption("Google Maps Review Count and Rating")
        st.write(sMapsRating, sMapsReviews)
    st.markdown("""--------------------------------------------------------------------------------------""")
    #Crearting a tab to visualize line plot for the entire dataset.
    tab1, tab2,= st.tabs(["Google Ratings", "Google Reviews"])
    #Tab 1 shows line plot for Google Maps Rating
    with tab1:
        st.header("A Line plot for Places and Google Ratings")
        #Initializing space for the graph to display
        rating_chart_row = st.empty()
        #Creating line graph
        gReviewBarChrt = alt.Chart(detail_df).mark_line().encode (
            y='Google Maps Rating',
            x=alt.X('Place',sort=None)
        )
        #displaying line chart
        rating_chart_row.altair_chart(gReviewBarChrt, use_container_width = True)

    #Tab 2 shows line plot for Google Reviews Rating
    with tab2:
        st.header("A Line plot for Places and Google Reviews")
        #Initializing space for the graph to display
        review_chart_row = st.empty()
        #Creating line graph
        gReviewBarChrt = alt.Chart(detail_df).mark_line().encode (
            y='Google Reviews (Count)',
            x=alt.X('Place',sort=None)
        )
        #displaying line chart
        review_chart_row.altair_chart(gReviewBarChrt, use_container_width = True)
    # Below code shows the point plot for the entire dataset
    st.header("An Interactive Point plot against review and rating")
    #Initializing space for the graph to display
    point_chart_row = st.empty()
    #Creating point plot chart
    point_chart = alt.Chart(detail_df).mark_point().encode(
    x='Google Maps Rating:Q',
    y='Google Reviews (Count):Q',
    color='Place',
    tooltip='Place'
    ).interactive()
    #displaying Point Plot
    point_chart_row.altair_chart(point_chart, use_container_width = True)
#Page 3 or Recommendations page
def page3():
    #Getting the user input from a slider and showing top recommendations from their budget.
    st.title("Famous Bali Destination Recommendation")
    max_input = st.slider("Pick your Budget range", min_value=0.0, max_value=50.00, step=00.50)
    sec_df = pd.DataFrame(pd.read_csv('Bali Popular Destination for Tourist 2022 - Sheet.csv'))
    result_df = sec_df[sec_df['Fee Info']<=max_input]
    top_recom = result_df[['Place','Google Maps Rating','Google Reviews (Count)','Fee Info']].copy()
    #Sorting values based on Rating and Review
    top_recom.sort_values(["Google Maps Rating","Google Reviews (Count)"],axis=0,ascending=False,inplace=True,na_position="first")
    st.subheader("Here is the top 10 Recommendation based on your Budget.")
    st.dataframe(top_recom[:10], use_container_width=True)
    st.markdown("""--------------------------------------------------------------------------------------""")
    #Creating a tab to display bar plot for the recommended dataset
    rtab1, rtab2,= st.tabs(["Google Ratings", "Google Reviews"])
    # rtab1 shows the bar graph for Google Rating
    with rtab1:
        st.header("A Bar plot for Places and Google Reviews")
        #Initializing space for the graph to display
        rec_rev_chart_row = st.empty()
        #Creating the bar graph
        rReviewBarChrt = alt.Chart(top_recom).mark_bar().encode (
            y='Google Reviews (Count)',
            x=alt.X('Place',sort=None)
        )
        #Displaying the Bar graph
        rec_rev_chart_row.altair_chart(rReviewBarChrt, use_container_width = True)

    with rtab2:
        st.header("A Bar plot for Places and Google Ratings")
        #Initializing space for the graph to display
        rec_rating_chart_row = st.empty()
        #Creating the bar graph
        rRatingBarChrt = alt.Chart(top_recom).mark_bar().encode (
            y='Google Maps Rating',
            x=alt.X('Place',sort=None)
        )
        #Displaying the Bar graph
        rec_rating_chart_row.altair_chart(rRatingBarChrt, use_container_width = True)
        



##Sidebar info
st.sidebar.header("Select the checkbox to filter the location")
#Checkbox for user to filter the Places based on Rating and Review. this filter works on page 1 and 2 only.
sortvalue1 = st.sidebar.checkbox("Select to sort with respect to rating",value=False)
sortvalue2 = st.sidebar.checkbox("Select to sort with respect to number of reviews",value=False)
#Checking if the user has clicked both the checkbox and sort it based on review and rating
if sortvalue1 and sortvalue2:
    #Sorting on review and rating in descending order
    detail_df.sort_values(["Google Maps Rating","Google Reviews (Count)"],axis=0,ascending=False,inplace=True,na_position="first")
#Checking if the user has clicked only Review
elif sortvalue2:
    #Sorting based on review count in descending order
    detail_df.sort_values(["Google Reviews (Count)"],axis=0,ascending=[False],inplace=True)
else:
    #Sorting based on rating count in descending order
    detail_df.sort_values(["Google Maps Rating"],axis=0,ascending=[False],inplace=True)
#sidebar header for location
st.sidebar.header("Select a location")
#Select box to select the city to visualize it in the page 1
selected_city = st.sidebar.selectbox("Select The City", detail_df['Place'])
#Initializint the Three pages
page_names = {
    "Information": page1,
    "Visualization": page2,
    "Recommendation": page3
}
#Creating empty space
st.sidebar.text("\n")
st.sidebar.text("\n")
st.sidebar.text("\n")
st.sidebar.text("\n")
st.sidebar.text("\n")
st.sidebar.text("\n")
st.sidebar.text("\n")
st.sidebar.text("\n")
st.sidebar.text("\n")
st.sidebar.text("\n")
st.sidebar.text("\n")
st.sidebar.text("\n")
st.sidebar.text("\n")
st.sidebar.text("\n")
st.sidebar.text("\n")
#Page Selectio goes here
page_selected = st.sidebar.selectbox("Select the Page Here to display", page_names.keys())
#Calling the selected page to display in the main page area.
page_names[page_selected]()

