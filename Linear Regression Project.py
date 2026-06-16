import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

customers = pd.read_csv('Ecommerce Customers')

sns.jointplot(data=customers, x='Time on Website', y='Yearly Amount Spent')
plt.show()

sns.jointplot(data=customers, x='Time on App', y='Yearly Amount Spent')
plt.show()

sns.lmplot(data=customers, x='Length of Membership', y='Yearly Amount Spent')
plt.show()


X = customers[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
Y = customers['Yearly Amount Spent']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=101)


lm = LinearRegression()
lm.fit(X_train, Y_train)


predictions = lm.predict(X_test)


plt.scatter(Y_test, predictions)
plt.xlabel('Y Test (True Values)')
plt.ylabel('Predicted Y')
plt.title('Predicted vs. True Values')
plt.show()


print('MAE:', metrics.mean_absolute_error(Y_test, predictions))
print('MSE:', metrics.mean_squared_error(Y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(Y_test, predictions)))


sns.histplot((Y_test - predictions), bins=50, kde=True)
plt.title('Residuals Distribution')
plt.xlabel('Yearly Amount Spent Error')
plt.show()


coefficients = pd.DataFrame(lm.coef_, X.columns, columns=['Coefficient'])
print("\n--- Model Coefficients ---")
print(coefficients)


