import streamlit
import streamlit as st
import numpy as np
import pickle
import logging
import random


class Main:

    def testing_model(self):
        logging.info("main_file.py: running test_model")
        try:
            trained_model = pickle.load(open('trained_model.pkl', 'rb'))

            list2 = list()
            for i in range(30):
                list2.append(random.randint(-1, 1))
            #print("testing_model function:", list2)
            #print("in test:", trained_model.predict([list2]))
            logging.info("main_file.py: successfully predicted in main file")

            list4 = list()
            st.title("Running streamlit app")
            list4.append(st.text_input("Enter value"))
            list4 = list4*30
            if st.button("Predict"):
                result = trained_model.predict([list4])
                st.success('The output is: {}'.format(result))

        except Exception as ex:

            logging.error("main_file.py: PROGRAMME FAILED, WITH :: %s" % ex)
