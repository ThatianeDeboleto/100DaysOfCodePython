import pandas as pd
import sklearn.model_selection as ms
import sklearn.linear_model as lm
import matplotlib.pyplot as plt
import numpy as np




dataset = pd.read_csv("")
dataset = dataset.dropna()
X = dataset.iloc[:, :-2]
y = dataset.iloc[:, -1].values

######################################
# Codificando variaveis Dummy
######################################
X_dummies = pd.get_dummies(X)

######################################
# Separar dados em Treino e Teste
######################################

X_train, X_test, y_train, y_test = ms.train_test_split(X_dummies, y, test_size = 1/5, random_state = 0)


######################################
# Treinando o modelo
######################################

regressor = lm.LinearRegression()
regressor.fit(X_train, y_train)

######################################
# Previsao
######################################

y_pred = regressor.predict(X_test)

np.set_printoptions(precision=2)
result = np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1)

def undummify(df, prefix_sep="_"):
    cols2collapse = {
        item.split(prefix_sep)[0]: (prefix_sep in item) for item in df.columns
    }
    series_list = []
    for col, needs_to_collapse in cols2collapse.items():
        if needs_to_collapse:
            undummified = (
                df.filter(like=col)
                .idxmax(axis=1)
                .apply(lambda x: x.split(prefix_sep, maxsplit=1)[1])
                .rename(col)
            )
            series_list.append(undummified)
        else:
            series_list.append(df[col])
    undummified_df = pd.concat(series_list, axis=1)
    return undummified_df

X_reverse = undummify(X_test)

X_reverse = X_reverse.reset_index(drop=True)

y_compare = pd.DataFrame(result)
y_compare = y_compare.rename(index=str, columns={0:'y_pred', 1:'y_test'})
y_compare = y_compare.reset_index(drop=True)

resultado_final = pd.concat([y_compare, X_reverse], axis=1)

######################################
# Valor Especifico
######################################

print(regressor.predict([[10]]))




'''Adicional
Não consegui encontrar os dados solicitados na tarefa, adaptei outro csv DataSet para concluir o projeto chegando a um 
projeto semelhante!
Use a famosa Pesquisa Longitudinal Nacional da Juventude 1997-2011 para executar uma Regressão Multivariável para prever
 salários. Como os ganhos são determinados e o que isso implica na política governamental?'''