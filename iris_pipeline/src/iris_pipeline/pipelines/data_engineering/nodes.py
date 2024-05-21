import pandas as pd
from sklearn.model_selection import train_test_split

class DataProcessor:
    def __init__(self, url):
        self.url = url
        self.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
    
    def load_data(self) -> pd.DataFrame:
        df = pd.read_csv(self.url, header=None, names=self.columns)
        return df
    
    def preprocess_data(self, df: pd.DataFrame) -> pd.DataFrame:
        df['species'] = df['species'].map({
            'Iris-setosa': 0,
            'Iris-versicolor': 1,
            'Iris-virginica': 2
        })
        return df
    
    def split_data(self, df: pd.DataFrame):
        X = df.drop('species', axis=1)
        y = df['species']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test
