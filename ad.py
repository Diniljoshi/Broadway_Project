import streamlit as st

#Interface
import pickle
import streamlit as st

with open('ad_sales.pickle','rb') as file:
    model = pickle.load(file)


st.title('Ad Sales Prediction')
tv = st.number_input('Input tv ad')
radio = st.number_input('Input Radio ad')
newspaper = st.number_input('Input Newspaper ad')

#Predict button
if st.button('Submit'):
    y_pred = model.predict([[tv, radio, newspaper]])
    st.write('The predicted Ad Sales is', round(y_pred[0],2))