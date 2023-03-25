import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import logging


class Describe:
    def __init__(self, df):
        self.df = df

    def propertiesofdf(self):
        try:
            logging.info("see_df.py: running see_df")
            #print(self.df.head(5))
            #pd.set_option('display.max_rows', 500, 'display.max_columns', 500)
            #print(self.df.describe())
            #print(self.df.info())
            #print(self.df.columns)
            logging.info("see_df.py: data is read in see_df")
            #sns.heatmap(self.df.corr(), cmap="BuPu")
            #plt.show()
            #plt.plot(sorted(self.df.corr()['Result'].abs(), reverse=True))
            #plt.show()
            #plt.plot(self.df.apply(pd.value_counts))
            #plt.show()
            logging.info("see_df.py: data is visualised in see_df")
        except Exception as ex:
            logging.error("see_df.py: PROGRAMME FAILED, WITH :: %s" % ex)