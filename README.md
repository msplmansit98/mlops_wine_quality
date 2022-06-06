mlflow server command -

mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts 

Current problems 
- dvc pipeline not running 
- MLflow service connection it is unable to make to run the code for logging the files


** Things to keep in mind
- uncomment the mlflow code in train and evaluate file.
- Always gitignore the files present in data folder
- To see the data files run the dvc pipeline after you clone the repository