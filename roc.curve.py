#roc curve demo - move this to tensorboard
python3
import sklearn
import tensorflow as TF
import numpy
c = RandomForestClassifier(n_estimators=10, random_state=42)
d = RandomForestClassifier(n_estimators=10, random_state=42)
e = RandomForestClassifier(n_estimators=10, random_state=42)
rfc.fit(X_train, y_train)
ax = plt.gca()
rfc_disp = plot_roc_curve(rfc, X_test, y_test, ax=ax, alpha=0.8)
svc_disp.plot(ax=ax, alpha=0.8)
plt.show()
#can commit 
