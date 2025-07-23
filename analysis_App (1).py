import streamlit as st

st.header("Sentiment_Analysis")

st.title("Using NLP via predicting analysis")
st.write("Hello","This is my nlp prediction app")

st.button("Prediction")

import streamlit as st

st.markdown("This is the markdown")
st.subheader("This is the subheader")
st.caption("This is the caption")
st.code("x = 2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

st.image(r"C:\Users\Datamites\Downloads\car.webp",caption = "Sedan Car")

st.checkbox('Yes')
st.radio('Pick your gender', ['Male', 'Female'])
st.selectbox('Pick a fruit', ['Apple', 'Banana', 'Orange'])
st.multiselect('Choose a planet', ['Jupiter', 'Mars', 'Neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0, 50)


st.number_input('Pick a number', 0, 10)
st.text_input('Email address')
st.date_input('Traveling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

st.balloons()  # Celebration balloonsst.progress(10)  # Progress barwith 
st.spinner('Wait for it...')#:    time.sleep(10)  # Simulating a process delay

st.success("You did it!")
st.error("Error occurred")
st.warning("This is a warning")
st.info("It's easy to build a Streamlit app")
st.exception(RuntimeError("RuntimeError exception"))



st.sidebar.title("Sidebar Title")
st.sidebar.markdown("This is the sidebar content")

with st.container():    
    st.write("This is inside the container")



import matplotlib.pyplot as plt
import numpy as np
rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)



import pandas as pd
df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.line_chart(df)



df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.bar_chart(df)


df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.area_chart(df)


import altair as alt
df = pd.DataFrame(np.random.randn(500, 3), columns=['x', 'y', 'z'])
chart = alt.Chart(df).mark_circle().encode(x='x', y='y', size='z', color='z', tooltip=['x', 'y', 'z'])
st.altair_chart(chart, use_container_width=True)


# import graphviz
# st.graphviz_chart('''    digraph {        Big_shark -> Tuna        Tuna -> Mackerel        Mackerel -> Small_fishes        Small_fishes -> Shrimp    }''')



@st.cache
def get_fvalue(val): 
    feature_dict = {"No": 1, "Yes": 2}    
    return feature_dict[val]
def get_value(val, my_dict):
     return my_dict[val]


app_mode = st.sidebar.selectbox("Select page",["Home","Prediction"])
if app_mode == 'Home':
    st.title('Loan Prediction')   
    st.image('loan_image.jpg')   
    st.markdown('Dataset:')    
    data = pd.read_csv('loan_dataset.csv')   
    st.write(data.head())   
    st.bar_chart(data[['ApplicantIncome', 'LoanAmount']].head(20))