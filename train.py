from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import logging

class Train:
    def __init__(self, df):
        self.df = df

    def training(self):
        try:
            logging.info("train.py: training started")
            df = self.df

            #train_test_split
            logging.info("train.py: splitting data")
            y = df['Result']
            x = df.drop(['Result'], axis=1)
            xtrain, xtest, ytrain, ytest = train_test_split(x, y)
            logging.info("train.py: data is successfully split")

            logging.info("train.py: starting model training")

            #model-tree
            logging.info("train.py: model_tree running")
            model_tree = DecisionTreeClassifier()
            model_tree.fit(xtrain, ytrain)
            tr = model_tree.score(xtest, ytest)
            logging.info("train.py: model_tree id successfully finished")
            #print("tree score", tr)

            #model-rf
            logging.info("train.py: starting random forest model")
            model_rf = RandomForestClassifier()
            model_rf.fit(xtrain, ytrain)
            rf = model_rf.score(xtest, ytest)
            logging.info("train.py: rf model run successfully")
            #print("random forest score:", rf)

            #model-lr
            logging.info("train.py: starting logistic reg model")
            model_lr = LogisticRegression()
            model_lr.fit(xtrain, ytrain)
            lr = model_lr.score(xtest, ytest)
            logging.info("train.py: lr model run successfully")

            #print("lr score:", lr)

            max_score = 0
            model = "none"

            if tr>max_score:
                model = "tr"
                max_score = tr
            if rf>max_score:
                model = "rf"
                max_score = rf
            if lr>max_score:
                model = "lr"
                max_score = lr

            logging.info("train.py: best model selected")
            #print(model, max_score)
            logging.info("train.py: successfully run training")
            if max_score == tr:
                return model_tree
            elif max_score == rf:
                return model_rf
            return model_lr
        except Exception as ex:
            logging.error("train.py: PROGRAMME FAILED, WITH :: %s" % ex)
