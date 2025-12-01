# Import necessary libraries
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import joblib

if __name__ == '__main__':
    # Load the digits dataset
    digits = load_digits()
    X, y = digits.data, digits.target

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a Random Forest classifier
    model = SVC(kernel='rbf')
    model.fit(X_train, y_train)

    # Save the model to a file
    joblib.dump(model, 'digits_model.pkl')

    print("Accuracy:", model.score(X_test, y_test))
    print("The model training was successful")
