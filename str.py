# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 19:38:03 2023

@author: Amma
"""


import numpy as np
import pickle
import streamlit as st

filename = 'C:/Users/vaish/OneDrive/Documents/MiniProject/trained_model.sav'

# loading the saved model
with open(filename, 'rb') as file:
    loaded_model = pickle.load(file)

#loaded_model = pickle.load(open('D:/Work/Machine Learning/Deploying Machine Learning model/trained_model.sav', 'rb'))
#loaded_model = pickle.load(open('C:/Users/Amma/Downloads/vaishu_stramlit_project/trained_model.sav', 'rb'))


# creating a function for Prediction

def kidney_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not affected by kidney disease'
    else:
      return 'The person is effected by kidney dise'
  
    
  
def main():
    
    
    # giving a title
    st.title('Kidney Prediction Web App')
    
    
    # getting the input data from the user
    #id,age,bp,sg,al,su,rbc,pc,pcc,ba,bgr,bu,sc,sod,pot,hemo,pcv,wc,rc,htn,dm,cad,appet,pe,ane,classification
    
    id = st.text_input('age')
    age = st.text_input('bacteria')
    bp = st.text_input('Blood Pressure value')
    sg= st.text_input('Specific gravity of urine')
    al = st.text_input('Albumin')
    su = st.text_input('Sugar')
    rbc = st.text_input('Red blood cells')
    pc = st.text_input('Pus cell')
    pcc = st.text_input('Pus cell clumps')
    ba = st.text_input('Bacteria') 
    bgr = st.text_input('Blood glucose random')
    bu = st.text_input('Blood urea')
    sc = st.text_input('Serum creatinine')
    sod = st.text_input('Sodiumsod')
    pot = st.text_input(' Potassium')
    hemo = st.text_input('Hemoglobin')
    pcv = st.text_input('Packed cell volume')
    wc = st.text_input('White blood cell count')
    rc = st.text_input('Red blood cell count')
    htn = st.text_input('Hypertension')
    dm = st.text_input('Diabetes mellitus')
    cad = st.text_input('Coronary artery disease')
    appet = st.text_input('Appetite')
    pe= st.text_input('Pedal edema')
    ane= st.text_input('Anemia')
    classification = st.text_input('packed cells')
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('kidney Test Result'):
        diagnosis = kidney_prediction([id,age,bp,sg,al,su,rbc,pc,pcc,ba,bgr,bu,sc,sod,pot,hemo,pcv,wc,rc,htn,dm,cad,appet,pe,ane,classification])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
    

