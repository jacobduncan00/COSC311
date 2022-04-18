from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

def load_data():
    real_data = np.loadtxt("./clean_real.txt", dtype=str, delimiter="\n")
    fake_data = np.loadtxt("./clean_fake.txt", dtype=str, delimiter="\n")
    reals = np.ones(len(real_data))
    fakes = np.zeros(len(fake_data))
    data = np.concatenate((real_data, fake_data), axis=0)
    indicators = np.concatenate((reals, fakes), axis=0)
    count_vec = CountVectorizer()
    data_matrix = count_vec.fit_transform(data)
    x_train, x_temp, y_train, y_temp = train_test_split(data_matrix, indicators, test_size=0.3, random_state=123)
    x_valid, x_test, y_valid, y_test = train_test_split(x_temp, y_temp, test_size=0.5, random_state=123)
    return x_train, y_train, x_valid, y_valid, x_test, y_test, count_vec


load_data()

def select_knn_model(x_train, y_train, x_valid, y_valid, isCosine):
    max_acc = -1000
    best_knn = None
    valid_errs = []
    train_errs = []
    for i in range(1, 21):
        if isCosine:
            model = KNeighborsClassifier(n_neighbors=i, metric="cosine")
        else:
            model = KNeighborsClassifier(n_neighbors=i)
        model.fit(x_train, y_train)
        acc = model.score(x_valid, y_valid)
        valid_errs.append(1-acc)
        train_errs.append(1-model.score(x_train,y_train))

        if acc > max_acc:
            max_acc = acc
            best_knn = model

    return best_knn, valid_errs, train_errs


# ===================================================================================================================
# SELECT_KNN_MODEL
x_train, y_train, x_validation, y_validation, x_test, y_test, count_vec = load_data()
print("Output for Select KNN Model")
knn_model, validation_errors, training_errors = select_knn_model(x_train, y_train, x_validation, y_validation, False)
best_knn_accuracy = knn_model.score(x_test, y_test)
print("Accuracy of the best KNN model on the test dataset: ", best_knn_accuracy)
x = [i for i in range(1, 21)]
fig, ax = plt.subplots()
ax.set_xlim(21, 0)
ax.scatter(x, validation_errors, label='Validation')
ax.plot(x, validation_errors)
ax.scatter(x, training_errors, c='red', label='Train')
ax.plot(x, training_errors, c='red')
plt.xlabel('k - Number of Nearest Neighbors')
plt.ylabel('Test Error')
ax.legend()
ax.xaxis.set_ticks_position('top')
ax.xaxis.set_label_position('top')
plt.show()
# ===================================================================================================================
# SELECT_KNN_MODEL WITH COSINE
print("Output for Select KNN Model With Cosine")
knn_model, validation_errors, training_errors = select_knn_model(x_train, y_train, x_validation, y_validation, True)
best_knn_accuracy = knn_model.score(x_test, y_test)
print("Accuracy of the best KNN model on the test dataset: ", best_knn_accuracy)
x = [i for i in range(1, 21)]
fig, ax = plt.subplots()
ax.set_xlim(21, 0)
ax.scatter(x, validation_errors, label='Validation')
ax.plot(x, validation_errors)
ax.scatter(x, training_errors, c='red', label='Train')
ax.plot(x, training_errors, c='red')
plt.xlabel('k - Number of Nearest Neighbors')
plt.ylabel('Test Error')
ax.legend()
ax.xaxis.set_ticks_position('top')
ax.xaxis.set_label_position('top')
plt.show()
# ===================================================================================================================

"""
Question (c)
How  does  metric='cosine' compute the  distance  between  data  points,  and  why  might  this  perform  better 
than the Euclidean metric (default) here?

Cosine similarity looks at the angle between two vectors where as Euclidean similarity looks at only the raw distance
between two points. Let's assume OA, OB and OC are three vectors. The points A, B and C form an equilateral triangle.
This means that the Euclidean distance of these points are the same (AB=BC=CA). In this case, the Euclidean distance
will not be effective in deciding which of the three vectors are similar to each other. Although the magnitude (length)
of the vectors are different. Cosine similarity measure shows that OA is more similar to OB than to OC.
"""