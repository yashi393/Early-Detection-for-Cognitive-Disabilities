import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Early detection of cognitive disabilities",
                   layout="wide",
                   page_icon="🧠🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

ASD_child_model = pickle.load(open(f'{working_dir}/saved_models/ASD_child_model.sav', 'rb'))

ASD_todd_model = pickle.load(open(f'{working_dir}/saved_models/ASD_todd_model.sav', 'rb'))

ID_model = pickle.load(open(f'{working_dir}/saved_models/ID_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Autism Spectrum Disorder Prediction in Toddlers',
                            'Autism Spectrum Disorder Prediction in Children',
                            'Intellectual Disability Prediction'],
                           menu_icon='hospital-fill',
                           icons=['baby', 'child', 'brain'],
                           default_index=0)


# ASD toddler Prediction Page
if selected == 'Autism Spectrum Disorder Prediction in Toddlers':

    # page title
    st.title('Autism Spectrum Disorder Prediction in Toddlers using ML')

# Note with emoji
    st.markdown("ℹ️ **Note**: In this form, *Yes* corresponds to **1** and *No* corresponds to **0**.")

    # getting the input data from the user
    col1, col2 = st.columns(2)

    with col1:
        A1 = st.selectbox('Does your child look at you when you call his/her name?', options=[1, 0])

    with col2:
        A2 = st.selectbox('How easy is it for you to get eye contact with your child?', options=[1, 0])

    with col1:
        A3 = st.selectbox('Does your child point to indicate that s/he wants something? (e.g. a toy that is out of reach)', options=[1, 0])

    with col2:
        A4 = st.selectbox('Does your child point to share interest with you? (e.g. pointng at an interesing sight)', options=[1, 0])

    with col1:
        A5 = st.selectbox('Does your child pretend? (e.g. care for dolls, talk on a toy phone)', options=[1, 0])

    with col2:
        A6 = st.selectbox('Does your child follow where youre looking? ', options=[1, 0])

    with col1:
        A7 = st.selectbox('If you or someone else in the family is visibly upset, does your child show signs of wan9ng to comfort them? (e.g. stroking hair, hugging them)', options=[1, 0])

    with col2:
        A8 = st.selectbox('Would you describe your child’s first words as typical?', options=[1, 0])

    with col1:
        A9 = st.selectbox('Does your child use simple gestures? (e.g. wave goodbye)', options=[1, 0])

    with col2:
        A10 = st.selectbox('Does your child stare at nothing with no apparent purpose', options=[1, 0])

    with col1:
        Age = st.text_input('Age of the toddler(in months)')

    with col2:
        Qchat_10_Score = st.selectbox('Qchat-10-Score', options=[1, 0])

    with col1:
        Sex = st.selectbox('Sex (1 = Male, 0 = Female)', options=[1, 0])

    with col2:
        Jaundice = st.selectbox('Jaundice', options=[1, 0])


    with col1:
        Family_mem_with_ASD = st.selectbox('Family Member with ASD', options=[1, 0])

    with col2:
         test = st.selectbox('Who completed the test? (1 = Parent, 0 = Other)', options=[1, 0])

    # code for Prediction
    asdt_diagnosis = ''

    # creating a button for Prediction

    if st.button('ASD for toddler Test Result'):

        user_input = [ A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, Age,
       Qchat_10_Score, Sex, Jaundice, Family_mem_with_ASD, test]

        user_input = [float(x) for x in user_input]

        asdt_prediction = ASD_todd_model.predict([user_input])

        if asdt_prediction[0] == 1:
            asdt_diagnosis_diagnosis = 'The person is Autistic'
        else:
            asdt_diagnosis = 'The person is not Autistic'

    st.success(asdt_diagnosis)

# Autism Spectrum Disorder Prediction in Children
if selected == 'Autism Spectrum Disorder Prediction in Children':

    # page title
    st.title('Autism Spectrum Disorder Prediction in Children')
    # Note with emoji
    st.markdown("ℹ️ **Note**: In this form, *Yes* corresponds to **1** and *No* corresponds to **0**.")

    col1, col2 = st.columns(2)

    with col1:
        id = st.text_input('ID')

    with col1:
        A1_Score = st.selectbox('I often notice small sounds when others do not.', options=[1, 0])

    with col2:
        A2_Score = st.selectbox('I usually concentrate more on the whole picture, rather than the small details.', options=[1, 0])

    with col1:
        A3_Score = st.selectbox('I find it easy to do more than one thing at once', options=[1, 0])

    with col2:
        A4_Score = st.selectbox('If there is an interruption, I can switch back to what I was doing very quickly', options=[1, 0])

    with col1:
        A5_Score = st.selectbox('I find it easy to read between the lines when someone is talking to me', options=[1, 0])

    with col2:
        A6_Score = st.selectbox('I know how to tell if someone listening to me is getting bored', options=[1, 0])

    with col1:
        A7_Score = st.selectbox('When Im reading a story I find it difficult to work out the characters intentions', options=[1, 0])

    with col2:
        A8_Score = st.selectbox('I like to collect information about categories of things (e.g. types of car, bird, train, plant etc.)', options=[1, 0])

    with col1:
        A9_Score = st.selectbox('I find it easy to work out what someone is thinking or feeling just by looking at their face', options=[1, 0])

    with col2:
        A10_Score = st.selectbox('I find it didicult to work out peoples intentions', options=[1, 0])

    with col1:
        age = st.text_input('Age')

    with col2:
        gender = st.selectbox('Sex (1 = Male, 0 = Female)', options=[1, 0])
    
    with col1:
        jundice = st.selectbox('Jaundice', options=[1, 0])

    with col2:
        austim = st.selectbox('Autism', options=[1, 0])
    # code for Prediction
    asdc_diagnosis = ''

    # creating a button for Prediction

    if st.button('ASD children Test Result'):

        user_input = [id, A1_Score, A2_Score, A3_Score, A4_Score, A5_Score,
       A6_Score, A7_Score, A8_Score, A9_Score, A10_Score, age,
       gender, jundice, austim]

        user_input = [float(x) for x in user_input]

        asdc_prediction = ASD_child_model.predict([user_input])

        if asdc_prediction[0] == 1:
            asdc_diagnosis = 'The person has Autistic'
        else:
            asdc_diagnosis = 'The person is not Autistic'

    st.success(asdc_diagnosis)

# Parkinson's Prediction Page
if selected == "Intellectual Disability Prediction":

    # page title
    st.title("Intellectual Disability Prediction using ML")

    # Note with emoji
    st.markdown("ℹ️ **Note**: In this form, *Yes* corresponds to **1** and *No* corresponds to **0**.")

    col1, col2= st.columns(2)

    with col1:
        Communication_Score = st.slider('Communication_Score', min_value=0, max_value=100)

    with col2:
        Daily_Living_Score = st.slider('Daily_Living_Score', min_value=0, max_value=100)

    with col1:
        Socialization_Score = st.slider('Socialization_Score', min_value=0, max_value=100)

    with col2:
        Overall_Adaptive_Score = st.slider('Overall_Adaptive_Score', min_value=0, max_value=100)


    # code for Prediction
    id_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Intellectual disability Test Result"):

        user_input = [Communication_Score, Daily_Living_Score, Socialization_Score, Overall_Adaptive_Score]

        user_input = [float(x) for x in user_input]

        id_prediction = ID_model.predict([user_input])

        if id_prediction[0] == 1:
            id_diagnosis = "The person does not have Intellectual disability"
        else:
            id_diagnosis = "The person has Intellectual disability"

    st.success(id_diagnosis)