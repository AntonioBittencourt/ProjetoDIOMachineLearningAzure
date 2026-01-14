from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
from azure.ai.ml import MLClient

try:
    credential = DefaultAzureCredential()
    #checar se credencial captura o token corretamente
    credential.get_tojen("https://management.azure.com/.default")
except Exception as ex:
    # volta ao InteractiveBrowserCredential caso DefaultAzrueCredential não funcione
    credential = InteractiveBrowserCredential()
#Espaço de trabalho
ml_client = MLCLient.from_config(credential=credential)
#import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve

#carrega o dataset Sorvetes
print("Carregando Data...")
sorvetes =pd.read_csv("sorvetes.csv")

#Separa recursos e classificações
x,y = sorcetes[['Temperatura']].values, sorvetes['Vendas'].values

#Separa dados em treinamento e teste
X_train, X_teste, y_train, y_teste = train_test_split(x,y, test_size= 0.2, random_state=0)

#hiperparâmetro de regularização
reg = 0.01

#treina um modelo de regressão logístico
print('Treinando um modelo de regressão logístico com uma taxa de ', reg)
model= LogisticRegression(C=1/reg, solver="liblinear").fit(X_train,y_train)

#Calcula Acurácia
y_hat = model.predict(X_test)
acc = np.average(y_hat == y_test)
print('Acuracia: ', acc)


#Calcula AUC
Y_scores = model.predict_proba(X_test)
auc = roc_auc_score(y_test, y_scores[:1])
print('AUX: ' , str(auc))

from azure.ai.ml import command

#continua o trabalho(job)
job = command(
    code="./src",
    command= "python sorvetes-trainning.py",
    environment = "AzureML=sklearn-0.24-ubuntu18.04-py-37-cpu@latest",
    compute "aml-cluster",
    display_name "sorvetes-python2-train",
    experinment_name= "Sorvetes-training"
)


#enviar o trabalho(job)
returned_job = ml_client.create_cf_update(job)
uml_url = returned_job.studio_url
print("Monitore o seu trabalho(job) em ", aml_url)
