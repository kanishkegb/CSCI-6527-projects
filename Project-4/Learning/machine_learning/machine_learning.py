from sklearn.tree import DecisionTreeRegressor

import pandas as pd
import pdb


melbourne_file_path = 'melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)
# print(melbourne_data.describe())
melbourne_data = melbourne_data.dropna(axis=0)

y = melbourne_data.Price
melbourne_predictors = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea',
                        'YearBuilt', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_predictors]

melbourne_model = DecisionTreeRegressor()
print(y.describe())
print(X.describe())

# pdb.set_trace()
melbourne_model.fit(X, y)

print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))
