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

LD_model = pickle.load(open(f'{working_dir}/saved_models/Dyslexia_Detection_Model.sav', 'rb'))
# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Autism Spectrum Disorder Prediction in Toddlers',
                            'Autism Spectrum Disorder Prediction in Children',
                            'Intellectual Disability Prediction',
                            'Dyslexia Detection'],
                           menu_icon='hospital-fill',
                           icons=['baby', 'child', 'brain'],
                           default_index=0)
    # Define Likert-scale mapping
option_map = {
    "Never ": 0.0,
    "Rarely ": 0.25,
    "Sometimes ": 0.5,
    "Often ": 0.75,
    "Always ": 1.0
}
binary_map = {
    "Yes": 1,
    "No": 0
}
sex_map = {
    "Female": 0,
    "Male": 1
}


# ASD toddler Prediction Page
if selected == 'Autism Spectrum Disorder Prediction in Toddlers':

    st.title('Autism Spectrum Disorder Prediction in Toddlers using ML')
    st.markdown("ℹ️ **Note**: Please answer each question based on a likelihood scale from Never to Always.")

    col1, col2 = st.columns(2)

    with col1:
        A1 = option_map[st.selectbox('Does your child look at you when you call his/her name?', options=list(option_map.keys()))]
    with col2:
        A2 = option_map[st.selectbox('How easy is it for you to get eye contact with your child?', options=list(option_map.keys()))]
    with col1:
        A3 = option_map[st.selectbox('Does your child point to indicate that s/he wants something?', options=list(option_map.keys()))]
    with col2:
        A4 = option_map[st.selectbox('Does your child point to share interest with you?', options=list(option_map.keys()))]
    with col1:
        A5 = option_map[st.selectbox('Does your child pretend?', options=list(option_map.keys()))]
    with col2:
        A6 = option_map[st.selectbox('Does your child follow where youre looking?', options=list(option_map.keys()))]
    with col1:
        A7 = option_map[st.selectbox('If someone is visibly upset, does your child comfort them?', options=list(option_map.keys()))]
    with col2:
        A8 = option_map[st.selectbox('Would you describe your child’s first words as typical?', options=list(option_map.keys()))]
    with col1:
        A9 = option_map[st.selectbox('Does your child use simple gestures (e.g. wave goodbye)?', options=list(option_map.keys()))]
    with col2:
        A10 = option_map[st.selectbox('Does your child stare at nothing with no apparent purpose?', options=list(option_map.keys()))]

    with col1:
        Age = st.text_input('Age of the toddler (in months)')
    with col2:
        Qchat_10_Score = option_map[st.selectbox('Qchat-10-Score', options=list(option_map.keys()))]
    with col1:
        Sex = sex_map[st.selectbox('Sex of the child:', options=list(sex_map.keys()))]
    with col2:
        Jaundice = binary_map[st.selectbox('Was the child diagnosed with jaundice?', options=list(binary_map.keys()))]
    with col1:
        Family_mem_with_ASD = binary_map[st.selectbox('Has the child already been diagnosed with autism?', options=list(binary_map.keys()))]
    with col2:
        test = binary_map[st.selectbox('Who completed the test? (1 = Parent, 0 = Other)', options=list(binary_map.keys()))]


    asdt_diagnosis = ''

    if st.button('ASD for toddler Test Result'):
        user_input = [A1, A2, A3, A4, A5, A6, A7, A8, A9, A10,
                      Age, Qchat_10_Score, Sex, Jaundice, Family_mem_with_ASD, test]
        user_input = [float(x) for x in user_input]
        asdt_prediction = ASD_todd_model.predict([user_input])

        if asdt_prediction[0] == 1:
            asdt_diagnosis = 'The person is Autistic'
        else:
            asdt_diagnosis = 'The person is not Autistic'

    st.success(asdt_diagnosis)


# ASD Children Prediction Page
if selected == 'Autism Spectrum Disorder Prediction in Children':

    st.title('Autism Spectrum Disorder Prediction in Children')
    st.markdown("ℹ️ **Note**: Please answer each question based on a likelihood scale from Never to Always.")

    col1, col2 = st.columns(2)

    with col1:
        id = st.text_input('ID')
    with col1:
        A1_Score = option_map[st.selectbox('I often notice small sounds when others do not.', options=list(option_map.keys()))]
    with col2:
        A2_Score = option_map[st.selectbox('I usually concentrate more on the whole picture than small details.', options=list(option_map.keys()))]
    with col1:
        A3_Score = option_map[st.selectbox('I find it easy to do more than one thing at once.', options=list(option_map.keys()))]
    with col2:
        A4_Score = option_map[st.selectbox('If interrupted, I can quickly switch back to my task.', options=list(option_map.keys()))]
    with col1:
        A5_Score = option_map[st.selectbox('I find it easy to read between the lines.', options=list(option_map.keys()))]
    with col2:
        A6_Score = option_map[st.selectbox('I know if someone listening to me is getting bored.', options=list(option_map.keys()))]
    with col1:
        A7_Score = option_map[st.selectbox('While reading, I struggle with characters’ intentions.', options=list(option_map.keys()))]
    with col2:
        A8_Score = option_map[st.selectbox('I like collecting info about categories (cars, birds, etc.).', options=list(option_map.keys()))]
    with col1:
        A9_Score = option_map[st.selectbox('I can tell what someone is feeling by their face.', options=list(option_map.keys()))]
    with col2:
        A10_Score = option_map[st.selectbox('I find it hard to understand others’ intentions.', options=list(option_map.keys()))]

    with col1:
        age = st.text_input('Age')
    with col2:
        gender = sex_map[st.selectbox('Sex of the child:', options=list(sex_map.keys()))]
    with col1:
        jundice = binary_map[st.selectbox('Was the child diagnosed with jaundice?', options=list(binary_map.keys()))]
    with col2:
        austim = binary_map[st.selectbox('was the child diagnosed with jaundice?', options=list(binary_map.keys()))]

    asdc_diagnosis = ''

    if st.button('ASD children Test Result'):
        user_input = [id, A1_Score, A2_Score, A3_Score, A4_Score, A5_Score,
                      A6_Score, A7_Score, A8_Score, A9_Score, A10_Score,
                      age, gender, jundice, austim]
        user_input = [float(x) for x in user_input]
        asdc_prediction = ASD_child_model.predict([user_input])

        if asdc_prediction[0] == 1:
            asdc_diagnosis = 'The person is Autistic'
        else:
            asdc_diagnosis = 'The person is not Autistic'

    st.success(asdc_diagnosis)

#Intellectual Disability Prediction
if selected == 'Intellectual Disability Prediction':

    st.title('Intellectual Disability Prediction using ML')
    st.markdown("ℹ️ **Note**: Please answer the following questions based on the individual’s typical abilities or behaviors.")

    option_map = {
        "Never": 0.0,
        "Rarely": 0.25,
        "Sometimes": 0.5,
        "Often": 0.75,
        "Always": 1.0
    }

    binary_map = {
        "Yes": 1,
        "No": 0
    }

    col1, col2 = st.columns(2)
    with col1:
        comm1 = option_map[st.selectbox("Does the person express basic needs using words or gestures?", list(option_map.keys()), key="comm1")]
    with col2:
        comm2 = option_map[st.selectbox("Does the person understand simple spoken instructions?", list(option_map.keys()), key="comm2")]
    with col1:
        comm3 = option_map[st.selectbox("Can the person engage in back-and-forth conversation?", list(option_map.keys()), key="comm3")]

    Communication_Score = ((comm1 + comm2 + comm3) / 3) * 100

    with col2:
        daily1 = option_map[st.selectbox("Can the person perform basic self-care (e.g., brushing teeth)?", list(option_map.keys()), key="daily1")]
    with col1:
        daily2 = option_map[st.selectbox("Does the person manage simple household tasks?", list(option_map.keys()), key="daily2")]
    with col2:
        daily3 = option_map[st.selectbox("Can the person follow a routine or daily schedule?", list(option_map.keys()), key="daily3")]

    Daily_Living_Score = ((daily1 + daily2 + daily3) / 3) * 100

    with col1:
        soc1 = option_map[st.selectbox("Does the person engage in play or recreational activities with others?", list(option_map.keys()), key="soc1")]
    with col2:
        soc2 = option_map[st.selectbox("Can the person form and maintain relationships?", list(option_map.keys()), key="soc2")]
    with col1:
        soc3 = option_map[st.selectbox("Does the person respond appropriately in social situations?", list(option_map.keys()), key="soc3")]

    Socialization_Score = ((soc1 + soc2 + soc3) / 3) * 100

    Overall_Adaptive_Score = (Communication_Score + Daily_Living_Score + Socialization_Score) / 3

    with col2:
        Q4 = binary_map[st.selectbox("Does the person have a history of any medical conditions?", list(binary_map.keys()), key="id_q4")]
    with col1:
        Q5 = binary_map[st.selectbox("Has the person achieved developmental milestones on time?", list(binary_map.keys()), key="id_q5")]
    with col2:
        Q6 = binary_map[st.selectbox("Is there a family history of intellectual disability?", list(binary_map.keys()), key="id_q6")]

    id_diagnosis = ''

    if st.button("Intellectual Disability Test Result"):
        user_input = [Communication_Score, Daily_Living_Score, Socialization_Score, Overall_Adaptive_Score]

        id_prediction = ID_model.predict([user_input])

        if id_prediction[0] == 1:
            id_diagnosis = "The person does not have Intellectual Disability"
        else:
            id_diagnosis = "The person has Intellectual Disability"

    st.success(id_diagnosis)

# Dyslexia Detection Page
import os
import numpy as np  # Ensure numpy is imported
import pickle
import streamlit as st
from PIL import Image

if selected == 'Dyslexia Detection':
    st.title("Learning Disability Prediction using ML")
    st.markdown("🧠 Upload an image related to learning disabilities (e.g., brain scan, behavioral cues)")
    st.markdown("📁 Drag and drop a JPG, JPEG, or PNG file (Max 200MB).")

    uploaded_file = st.file_uploader("Choose an image file", type=['jpg', 'jpeg', 'png'])

    ld_diagnosis = ''

    if uploaded_file is not None:
        # Display the image
        image = Image.open(uploaded_file)

        st.image(image, caption="Uploaded Image", use_container_width=True)  # Changed use_column_width to use_container_width

        # Preprocess image — adjust as needed for your model
        try:
            # Resize image to 128x128 and convert to RGB
            img = image.resize((128, 128))  # Resize to expected input size
            img = img.convert('RGB')  # Ensure image has 3 channels (RGB)

            # Convert image to numpy array and normalize
            img_array = np.array(img).astype('float32') / 255.0  # Normalize the image
            img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension (1, 128, 128, 3)

            if st.button("Predict Learning Disability"):
                # Run the model prediction
                prediction = LD_model.predict(img_array)

                if prediction[0] == 1:
                    ld_diagnosis = "⚠️ The person is not likely to have a learning disability (e.g., dyslexia)."
                else:
                    ld_diagnosis = "✅ The person is likely to have a learning disability."
                
                st.success(ld_diagnosis)

        except Exception as e:
            st.error(f"Error in processing the image: {e}")
    else:
        st.info("Please upload an image to proceed.")
