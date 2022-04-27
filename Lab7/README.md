# For each dataset, report which hyperparameter settings you found worked the best and the final cross entropy and classification error on the training, validation, and test sets.

My model got very small cross entropy and high accuracy in the mnist_train set when my learning rate was set to 0.008 and iterations set to 2000. Graphs can be seen in plots directory. When these hyperparamters were set I got train cross entropy of 0.09859, validation cross entropy of 0.22127, and test cross entropy of 0.21343, train classification err 0.00000, and validation classification error of 0.08000, and test classification error of 0.08000.

My model got very small cross entropy and high accuracy in the mnist_train_small set when my learning rate was set to 0.004 and iterations set to 500. Graphs can be seen in plots directory. When these hyperparamters were set I got train cross entropy of 0.11595, validation cross entropy of 0.67714, and test cross entropy of 0.54535, train classification err 0.00000, and validation classification error of 0.38000, and test classification error of 0.24000.

# In each plot, you need show two curves: one for the training set and one for the validation set. Run your code several times and observe if the results change. If they do, how would you choose the best parameter settings?

The plots are plotted after the program starts running, you want your train line and your validation line to be as close as possible as that shows that your model is trained well and is being validated against the validation data.
If the line deviates from the validation line you need to tweak your hyperparamters to get them aligned. Run program to see plots.

# For each dataset, report which hyperparameter settings you found worked the best and the final cross entropy and classification error on the training, validation, and test sets.

My model got very small cross entropy and high accuracy in the mnist_train set when my learning rate was set to 0.008 and iterations set to 2000. Graphs can be seen in plots directory. My model got small cross entropy and high accuracy in the mnist_train_small set when my learning rate was set to 0.004 and iterations set to 500. Graphs can be seen in plots directory.

mnist_train_set:
λ = 0, AVG_CE: Train 0.19340, Validation 0.30552, AVG_ERR: Train 0.02076, Validation 0.12610
λ = 0.001, AVG_CE: Train 0.19355, Validation 0.30526, AVG_ERR: Train 0.02086, Validation 0.12752
λ = 0.01, AVG_CE: Train 0.19820, Validation 0.30720, AVG_ERR: Train 0.02039, Validation 0.12503
λ = 0.1, AVG_CE: Train 0.24943, Validation 0.34385, AVG_ERR: Train 0.02589, Validation 0.11812
λ = 1, AVG_CE: Train 0.45728, Validation 0.50975, AVG_ERR: Train 0.06004, Validation 0.16590

mnist_train_small_set:
λ = 0, AVG_CE: Train 0.44554, Validation 0.50673, AVG_ERR: Train 0.08954, Validation 0.20342
λ = 0.001, AVG_CE: Train 0.44201, Validation 0.50312, AVG_ERR: Train 0.08196, Validation 0.18938
λ = 0.01, AVG_CE: Train 0.44539, Validation 0.50756, AVG_ERR: Train 0.08659, Validation 0.20391
λ = 0.1, AVG_CE: Train 0.45131, Validation 0.51078, AVG_ERR: Train 0.08669, Validation 0.20962
λ = 1, AVG_CE: Train 0.51341, Validation 0.55554, AVG_ERR: Train 0.08876, Validation 0.21402

# For each dataset, how does the cross entropy change when you increase λ? Do they go up, down, first up and then down, or down and then up? Explain why you think they behave this way. Which is the best value of λ, based on your experiments? Report the test cross entropy and classification rate for the best value of λ.

They seem to just go down as the lambda value increases. The graph seems to reach the coverage faster when the lambda is greater. The higher lambda I use, the model will converge faster since for each time we reduce more, making the coverage faster. The best lambda to choose here would be λ = 0.001 based on my tests. When λ = 0.001, CE: Test 0.21977, ERR: Test 0.08000, CR: Test 0.92000
