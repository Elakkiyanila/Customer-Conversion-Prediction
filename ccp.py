import pandas as pd
import numpy as np
from datetime import datetime
import streamlit as st
import pickle as pkl
from streamlit_option_menu import option_menu
import warnings as warning

# Streamlit page configuration
st.set_page_config(page_title='Customer Conversion Prediction', page_icon='📈', layout='wide')

warning.filterwarnings('ignore')

model = pkl.load(open(r"xg_pickle.pkl", 'rb'))
scaler = pkl.load(open(r"sc_pickle.pkl", 'rb'))

df = pd.read_csv('./train.csv')

# Set the background image using custom CSS
background_image_style = """
    <style>
        body {
            background-image: url('CCP.jpg');  # Change 'CCP.jpg' to the actual image file path
            background-size: cover;
            background-attachment: fixed;
        }
    </style>
"""
st.markdown(background_image_style, unsafe_allow_html=True)

# =========hide the streamlit main and footer
hide_default_format = """
   <style>
   #MainMenu {visibility: hidden; }
   footer {visibility: hidden;}
   </style>
"""
st.markdown(hide_default_format, unsafe_allow_html=True)

# Full-page content
with st.container():
    st.image('CCP.jpg', use_column_width=True)
    st.markdown("<h1 style='text-align: center; color: white;'>CUSTOMER CONVERSION PREDICTION </h1>",
                unsafe_allow_html=True)

    selected = option_menu(None, ['HOME', "PREDICTION"],
                           icons=["house", 'torpy'], orientation='horizontal', default_index=0)

    if selected=='HOME':
       

        st.write('## **WELCOME TO CUSTOMER CONVERSION MODELLING**')
        st.markdown('##### ***This project focuses on modelling Customer Conversion Prediction project, where we leverage the power of Python and key libraries such as Pandas, NumPy, and Scikit-Learn. The primary goal of this initiative is to predict customer conversion – specifically, determining whether a customer is likely to subscribe to a service.***')
        left ,right=st.columns([2,2])
        with left:
            st.write('### TECHNOLOGY USED')
            st.write('- PYTHON   (PANDAS, NUMPY)')
            st.write('- SCIKIT-LEARN')
            st.write('- DATA PREPROCESSING')
            st.write('- EXPLORATORY DATA ANALYSIS')
            st.write('- STREAMLIT')

        with right:
            st.write("### MACHINE LEARNING MODEL")
            st.write('#### REGRESSION - ***:red[EXTRATREEREGRESSOR]***')
            st.write('- The ExtraTree Regressor is an ensemble learning method that belongs to the tree-based family of models.')
            st.write('#### CLASSIFICATION - ***:green[RANDOMFORESTCLASSIFIER]***')
            st.write('- The RandomForestClassifier is an ensemble learning method that combines multiple decision trees to create a robust and accurate classification model.')




    elif selected == 'PREDICTION':
        st.write("## Customer Conversion Prediction Section")

        # Add your prediction content here
        st.markdown('##### ***This section allows you to predict whether a customer is likely to subscribe to a service based on various features.***')
        st.write(' **- Select your information on the left panel.**')

        ages,jobs,maritals =  st.columns(3)
        with ages:
            age = st.slider('Enter Your Age:',18,95)
        with jobs:
            job = st.selectbox('Select Job Type:', sorted(df['job'].unique()))
        with maritals:
            marital = st.selectbox('Select Marital Type:', sorted(df['marital'].unique()))
        educations,calls,days =  st.columns(3)
        with educations:
            education = st.selectbox('Select Education Type:', sorted(df['education_qual'].unique()))
        with calls:
            call = st.selectbox('Select Calls Type:', sorted(df['call_type'].unique()))
        with days:
            day = st.slider('Select Day:', 1,31)
        months,durations =  st.columns(2)
        with months:
            month = st.selectbox('Select Months:', sorted(df['mon'].unique(), key=lambda m: datetime.strptime(m, "%b")))
        with durations:
            duration = st.slider('Select Duration:',0,5000)
        previous_outcomes,num_calls = st.columns(2)
        with num_calls:
            call = st.slider('Select No Of Calls:', 1,65)
        with previous_outcomes:
            prev_outcome = st.selectbox('Select Previous Income:', sorted(df['prev_outcome'].unique()))
        result = st.button('Submit')
        ad = 0
        bl = 0
        en = 0
        ho = 0
        ma = 0
        re = 0
        se = 0
        ser = 0
        stu = 0
        te = 0
        un = 0
        unk = 0


        if job == 'admin':
            ad = 1
        else:
            ad = 0

        if job == 'blue-collar':
            bl = 1
        else:
            bl = 0

        if job == 'entrepreneur':
            en = 1
        else:
            en = 0

        if job == 'housemaid':
            ho = 1
        else:
            ho = 0

        if job == 'management':
            ma = 1
        else:
            ma = 0

        if job == 'retired':
            re = 1
        else:
            re = 0

        if job == 'self-employed':
            se = 1
        else:
            se = 0

        if job == 'services':
            ser = 1
        else:
            ser = 0

        if job == 'student':
            stu = 1
        else:
            stu = 0
            
        if job == 'technician':
            te = 1
        else:
            te = 0

        if job == 'unemployed':
            un = 1
        else:
            un = 0

        if job == 'unknown':
            unk = 1
        else:
            unk = 0


        # MARITAL

        mar = 0
        if marital == 'married':
            mar = 0
        elif marital == 'singal':
            mar = 1
        else:
            mar = 2


        # EDUCATION

        edu = 0
        if education == 'secondary':
            edu = 0
        elif education == 'tertiary':
            edu = 1
        elif education == 'secondary':
            edu = 2
        else:
            edu = 3


        # CALL

        cal = 0
        if call == 'cellular':
            cal = 0
        elif call == 'unknown':
            cal = 1
        else:
            cal = 2

        # MONTH

        janu = 0
        febr = 0
        marc = 0
        apri = 0
        maye = 0
        june = 0
        july = 0
        augu = 0
        sept = 0
        octo = 0
        nove = 0
        dece = 0


        if month == 'jan':
            janu = 1
        else:
            janu = 0

        if month == 'feb':
            febr = 1
        else:
            febr = 0

        if month == 'mar':
            marc = 1
        else:
            marc = 0

        if month == 'apr':
            apri = 1
        else:
            apri = 0

        if month == 'may':
            maye = 1
        else:
            maye = 0

        if month == 'jun':
            june = 1
        else:
            june = 0

        if month == 'jul':
            july = 1
        else:
            july = 0

        if month == 'aug':
            augu = 1
        else:
            augu = 0

        if month == 'sep':
            sept = 1
        else:
            sept = 0
            
        if month == 'oct':
            octo = 1
        else:
            octo = 0

        if month == 'nov':
            nove = 1
        else:
            nove = 0

        if month == 'dec':
            dece = 1
        else:
            dece = 0

        # PREVIOUS OUTCOME

        fal = 0
        oth = 0
        suc = 0
        unn = 0


        if prev_outcome == 'failure':
            fal = 1
        else:
            fal = 0

        if prev_outcome == 'other':
            oth = 1
        else:
            oth = 0

        if prev_outcome == 'success':
            suc = 1
        else:
            suc = 0

        if prev_outcome == 'unknown':
            unn = 1
        else:
            unn = 0


        st.write(' **-Click the "Submit" button to get the prediction.**')

        if result:
            data = np.array([[age,mar,edu,cal,day,duration,call,bl,en,ho,ma,re,se,ser,stu,te,un,unk,augu,dece,febr,janu,july,june,marc,maye,nove,octo,sept,oth,suc,unn]])
            scale_data = scaler.transform(data)
            res = model.predict(scale_data)
            st.markdown('<p class="header">Prediction</p>', unsafe_allow_html=True)

                # Display the prediction
            if res == 0:
                    st.markdown('<p class="prediction" style="color: red;">No, The customer is highly unlikely to subscribe to the insurance.</p>', unsafe_allow_html=True)
            else:
                    st.markdown('<p class="prediction" style="color: green;">Yes, The customer is highly likely to subscribe to the insurance.</p>', unsafe_allow_html=True)

                    


