# Iris Flower Classification with Logistic Regression

Hey there! 👋 Welcome to my project where I use Logistic Regression to classify Iris flowers based on their petal and sepal measurements. This is a simple yet classic example to get started with machine learning using the famous **Iris dataset**.

## What’s This About?

In this project, I’m working with the **Iris dataset**, which includes data on three types of Iris flowers: *Setosa*, *Versicolor*, and *Virginica*. Each flower is described by four features:
- Sepal length
- Sepal width
- Petal length
- Petal width

I’m using **Logistic Regression** to classify which species a flower belongs to, based on those features. After training the model, I save it so it can be reused without retraining it every time.

## How It Works

### Step-by-Step

1. **Load the Dataset**: Using `scikit-learn`'s handy `load_iris()` function to get the data.
2. **Train-Test Split**: I split the data into training and testing sets to evaluate how well the model performs on unseen data.
3. **Train the Model**: I apply Logistic Regression and fit it to the training data.
4. **Make Predictions**: The model predicts the species for the test set.
5. **Save the Model**: Using `pickle`, I save the trained model to a file for later use.
6. **Compare Results**: Finally, I compare the predicted species with the actual species in the test data.

## Files in This Repo

- `iris_classification.py`: The main script that does all the work—loading the data, training the model, and saving it.
- `model.pkl`: The trained Logistic Regression model, saved so you can use it later without needing to retrain.

## How to Run This

First, make sure you’ve got Python 3 and the required libraries installed. If you don’t have them yet, you can install `scikit-learn` with:

```bash
pip install scikit-learn
```

Then, just run the script:

```bash
python iris_classification.py
```

The script will:
- Train the model on 80% of the data.
- Test it on the remaining 20%.
- Print out the predicted and actual species for the test set.

## What You'll See

You’ll get an output showing the shape of the training and testing data, along with the predicted and actual species for the test samples.

Example:

```
Predicted values: [1 0 2 1 1 0 2 ...]
Actual values: [1 0 2 1 1 0 2 ...]
```
It’s a simple project, but it’s a great way to see how a basic machine learning pipeline works. Plus, the Iris dataset is small and easy to understand, making it perfect for beginners. 🌱
Let me know if you have any feedback or suggestions!
