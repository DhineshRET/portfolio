import streamlit as st
import pandas as pd
from io import StringIO

st.title('Check')

uploaded_files = st.file_uploader(
    "Choose a CSV file"
)
df= pd.read_csv(uploaded_files)
st.write(df)
# uploaded_files = st.file_uploader(
#     "Choose a CSV file", accept_multiple_files=True
# )
# for uploaded_file in uploaded_files:
#     bytes_data = uploaded_file.()
#     temp=pd.read_csv(uploaded_file)read
#     st.write("filename:", uploaded_file.name,"column:",uploaded_file.read)
    # st.write(bytes_data)

# DATE_COLUMN = 'date/time'
# DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
#             'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# @st.cache_data
# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     return data

# data_load_state = st.text('Loading data...')
# data = load_data(10000)
# data_load_state.text("Done! (using st.cache_data)")

# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(data)

# st.subheader('Number of pickups by hour')
# hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
# st.bar_chart(hist_values)

# # Some number in the range 0-23
# hour_to_filter = st.slider('hour', 0, 23, 17)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

# st.subheader('Map of all pickups at %s:00' % hour_to_filter)
# st.map(filtered_data)
