import pytest
import pandas as pd
import numpy as np
from prediction_demo import data_preparation,data_split,train_model,eval_model

@pytest.fixture
def housing_data_sample():
    return pd.DataFrame(
      data ={
      'price':[13300000,12250000],
      'area':[7420,8960],
    	'bedrooms':[4,4],	
      'bathrooms':[2,4],	
      'stories':[3,4],	
      'mainroad':["yes","yes"],	
      'guestroom':["no","no"],	
      'basement':["no","no"],	
      'hotwaterheating':["no","no"],	
      'airconditioning':["yes","yes"],	
      'parking':[2,3],
      'prefarea':["yes","no"],	
      'furnishingstatus':["furnished","unfurnished"]}
    )

def test_data_preparation(housing_data_sample):
    feature_df, target_series = data_preparation(housing_data_sample)
    # Target and datapoints has same length
    assert feature_df.shape[0]==len(target_series)

    #Feature only has numerical values
    assert feature_df.shape[1] == feature_df.select_dtypes(include=(np.number,np.bool_)).shape[1]

@pytest.fixture
def feature_target_sample(housing_data_sample):
    feature_df, target_series = data_preparation(housing_data_sample)
    return (feature_df, target_series)

def test_data_split(feature_target_sample):
    # Call the data_split function
    X_train, X_test, y_train, y_test = data_split(*feature_target_sample)

    # Verify the function returns exactly 4 items
    assert len((X_train, X_test, y_train, y_test)) == 4, "data_split should return (X_train, X_test, y_train, y_test)"

    # Verify data is split correctly
    assert X_train.shape[0] > 0, "X_train should not be empty"
    assert X_test.shape[0] > 0, "X_test should not be empty"
    assert y_train.shape[0] > 0, "y_train should not be empty"
    assert y_test.shape[0] > 0, "y_test should not be empty"

    # Ensure feature columns match between train and test sets
    assert set(X_train.columns) == set(X_test.columns), "Mismatch in feature columns between X_train and X_test"

    # Verify target variable is properly separated
    assert 'price' not in X_train.columns, "Target variable should not be in X_train"
    assert 'price' not in X_test.columns, "Target variable should not be in X_test"
    assert y_train.name == 'price', "y_train should contain the target variable 'price'"
    assert y_test.name == 'price', "y_test should contain the target variable 'price'"