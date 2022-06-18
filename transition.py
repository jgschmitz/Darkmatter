from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
X, y = load_wine(return_X_y=True)
y = y == 2
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
svc = SVC(random_state=42)
svc.fit(X_train, y_train)
print 1,2,3,4,



