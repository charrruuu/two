import pickle
import sys
import numpy as np
from sklearn.linear_model import LinearRegression
print("====ML CI Pipeline====")
x=np.array([[1],[2],[3]])
y=np.array([2,4,6])
model=LinearRegression()
model.fit(x,y)
print('Model Trained')
with open('model.pkl','wb') as f:
    pickle.dump(model,f)
print('Model saved')
prediction=model.predict([[4]])[0]
print(f"Prediction : {prediction:.1f}(Expected: 8.0)")
if abs(prediction - 8.0) < 0.1:
    print('Validation passed')
    sys.exit(0)
else:
    print('validation failed')
    sys.exit(1)
    