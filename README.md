# Airplane Speed Predictor
Author: Justin Short
Course: CECS 457
### Description
This is a simple python program that uses a linear regression model to predict the speed of an airplane at a given altitude. The model is trained from the dataset available at https://www.kaggle.com/datasets/brianwarner/aircraft-data-from-nov-2022-through-dec-31-2022.  

Testing.ipynb is a jupyter notebook I used to explore the data and test different models. Results.ipynb is a jupyter notebook that I used to document the results of the models and step through how I chose which model to use in the final CLI app. Presentation.ipynb is a jupyter notebook that I used to generate plots for my presentation, which can be found in the presentation folder (in both .pptx and .pdf formats).

### Usage
- from within directory of main.py file run "python3 main.py <altitude>
    - altitude is in feet
    - altitude must be a numeric value between 0 and 50000
    - output is in miles per hour
- example: "python3 main.py 35000"
    - output: "Predicted speed at 35000.0 ft: 515.80 mph"

### Dependencies
- for main executable
    - pandas
    - scikit-learn
- for notebooks
    - pandas
    - scikit-learn
    - matplotlib
    - seaborn
    - numpy