import mlflow
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import os
from dotenv import load_dotenv

load_dotenv()
tracking_uri = os.getenv("DAGSHUB_TRACKING_URI")
token = os.getenv("DAGSHUB_TOKEN")


# Load data
cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, test_size=0.2, random_state=42
)

mlflow.set_tracking_uri(tracking_uri)
mlflow.set_experiment("Tesing2")

# Enable autologging
mlflow.sklearn.autolog()

with mlflow.start_run():
    model = GradientBoostingClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Model scoring is automatically captured
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)
