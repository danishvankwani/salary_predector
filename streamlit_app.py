import streamlit_app as st
import pickle 
import numpy as np 

st.set_page_config(page_title="Salary predictor", page_icon="📕")
    
st.title("SALARY PREDICTOR")

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

yoe = st.number_input("Experience year" , min_value=0.0 ,max_value=10.0)

if st.button("predict"):
    predictions = model.predict([[yoe]])
    st.success(np.round(predictions[0]))

