import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import logging
import pickle
from see_df import Describe
from train import Train
from test_model import Testing
from main_file import Main
import logging
import sys

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)

file_handler = logging.FileHandler('logs.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)


logger.addHandler(file_handler)
logger.addHandler(stdout_handler)
logging.basicConfig(filename='logs.log', level=logging.DEBUG, format='%(asctime)s %(message)s')


def model():
    try:
        df = pd.read_csv(r'C:\Users\PavanAray\Desktop\stuff\TO_DELETE\New folder\test\phish.csv')
        logging.info("model.py: df is read in main")

        # SEE DATA
        describe = Describe(df)
        describe.propertiesofdf() #read the properties of df
        logging.info("model.py: see_df is run successfully")
        logging.info("model.py: main running")

        # TRAIN DATA
        logging.info("model.py: starting training function")
        train1 = Train(df)
        trained_model = train1.training()
        #print("final model:", trained_model)
        logging.info("model.py: training is finished")
        logging.info("model.py: main file running")
    
    
        # TEST model
        logging.info("model.py: model testing started")
        test_model = Testing(trained_model)
        test = test_model.test(trained_model)
        logging.info("model.py: program run successfully!")

        # SAVE model
        logging.info("model.py: pickling model")
        pickle.dump(trained_model, open('trained_model.pkl', 'wb'))
        logging.info("model.py: pickling completed")

        # DEPLOY model
        logging.info("model.py: now running main file")
        main_instance = Main()
        main_instance.testing_model()
        logging.info("model.py: program finished")


    except Exception as ex:
        logging.error("model.py: PROGRAMME FAILED, WITH :: %s" % ex)


model()