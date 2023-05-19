import streamlit as st
import pickle

model = pickle.load(open('model.pkl','rb'))

st.title('CAR PRICE PREDICTION')


Fuel_Type_Diesel = 0
Year = st.number_input('Enter year Bought',step= 1)
Present_Price = st.number_input('Enter Present price')
Kms_Driven = st.number_input('Enter Kms_Driven',step=1)
Age = 2023 - Year
Owner = st.selectbox("Choose Owner",(0,1,3))

Fuel_Type_Petrol = st.selectbox("Choose Fuel_Type",('Petrol', 'Diesel', 'CNG'))
if(Fuel_Type_Petrol=='Petrol'):
    Fuel_Type_Petrol=1
    Fuel_Type_Diesel= 0
else:
    Fuel_Type_Petrol=0
    Fuel_Type_Diesel=1


Seller_Type_Individual = st.selectbox('Choose Seller type',('Dealer','Individual'))
if (Seller_Type_Individual == 'Individual'):
    Seller_Type_Individual = 1
else:
    Seller_Type_Individual = 0


Transmission_Manual = st.selectbox('Choose Seller type',('Manual','Automatic'))
if (Seller_Type_Individual == 'Manual'):
    Transmission_Manual = 1
else:
    Transmission_Manual = 0


if st.button('Predict'):
   result = model.predict([[Present_Price, Kms_Driven, Owner, Age, Fuel_Type_Diesel,
      Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Manual]])
   output = round(result[0], 2)
   if output < 0:
       st.header("Sorry you cannot sell this car")
   else:
       st.header("The Car can be sold for {} dollars".format(output))




