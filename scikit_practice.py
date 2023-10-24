from sklearn.linear_model import LinearRegression
import pandas as pd

data = pd.read_csv("/Users/louishagenbucher/Downloads/ML_Houses_dataset.csv")

data.head()

livecode_data = data[['GrLivArea','SalePrice']]

livecode_data.head()
