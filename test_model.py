import random
import logging

class Testing:
    def __init__(self, model):
        self.model = model

    def test(self, model):
        try:
            model = self.model
            #print("In test function:", model)
            logging.info("test_model.py running")

            list2 = list()
            for i in range(30):
                list2.append(random.randint(-1, 1))
            #print("test function:", list2)
            #print("in test:", model.predict([list2]))
            logging.info("test_model.py successfully predicted in test file")
            logging.info("test_model.py starting main file")
        except Exception as ex:
            logging.error("test_model.py: PROGRAMME FAILED, WITH :: %s" % ex)