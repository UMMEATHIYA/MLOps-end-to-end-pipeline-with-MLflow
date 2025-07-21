import pandas as pd
import os
import numpy as np
from mlProject import logger
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import mlflow
import mlflow.sklearn
from mlProject.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        # Load data
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]

        # Set MLflow tracking
        mlflow.set_tracking_uri("http://127.0.0.1:5000")
        mlflow.set_experiment("ElasticNet-Regression")

        with mlflow.start_run():
            # Model training
            lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
            lr.fit(train_x, train_y)

            # Predictions and metrics
            preds = lr.predict(test_x)
            rmse = np.sqrt(mean_squared_error(test_y, preds))

            r2 = r2_score(test_y, preds)

            # Log parameters, metrics, and model
            mlflow.log_param("alpha", self.config.alpha)
            mlflow.log_param("l1_ratio", self.config.l1_ratio)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2_score", r2)
            mlflow.sklearn.log_model(lr, artifact_path="model")

            # Save model locally
            joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))

            logger.info(f"Model trained and logged to MLflow. RMSE: {rmse:.4f}, R2: {r2:.4f}")
