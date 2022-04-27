from utils import sigmoid
import numpy as np

def logistic_predict(weights, data):
    """ Compute the probabilities predicted by the logistic classifier.

    Note: N is the number of examples
          M is the number of features per example

    :param weights: A vector of weights with dimension (M + 1) x 1, where
    the last element corresponds to the bias (intercept).
    :param data: A matrix with dimension N x M, where each row corresponds to
    one data point.
    :return: A vector of probabilities with dimension N x 1, which is the output
    to the classifier.
    """
    #####################################################################
    # TODO:                                                             #
    # Given the weights and bias, compute the probabilities predicted   #
    # by the logistic classifier.                                       #
    #####################################################################
    N, M = data.shape
    data_buff = np.concatenate((data, np.ones((N, 1))), axis=1)
    y = np.dot(data_buff, weights)
    y = sigmoid(y)
    #####################################################################
    #                       END OF YOUR CODE                            #
    #####################################################################
    return y
    
def evaluate(targets, y):
    """ Compute evaluation metrics.

    Note: N is the number of examples
          M is the number of features per example

    :param targets: A vector of targets with dimension N x 1.
    :param y: A vector of probabilities with dimension N x 1.
    :return: A tuple (ce, frac_correct)
        WHERE
        ce: (float) Averaged cross entropy
        frac_correct: (float) Fraction of inputs classified correctly
    """
    #####################################################################
    # TODO:                                                             #
    # Given targets and probabilities predicted by the classifier,      #
    # return cross entropy and the fraction of inputs classified        #
    # correctly.                                                        #
    #####################################################################
    counter = 0
    for i in range(targets.size):
        if (y[i]>=0.5 and targets[i]==1) or (y[i]<0.5 and targets[i]==0):
            counter += 1
    ce = (-np.dot(targets.T, np.log(y)) - (np.dot((1-targets).T, np.log(1-y)))) / float(targets.size)
    frac_correct = counter / float(len(targets))
    #####################################################################
    #                       END OF YOUR CODE                            #
    #####################################################################
    return ce[0], frac_correct


def logistic(weights, data, targets, hyperparameters):
    """ Calculate the cost and its derivatives with respect to weights.
    Also return the predictions.

    Note: N is the number of examples
          M is the number of features per example

    :param weights: A vector of weights with dimension (M + 1) x 1, where
    the last element corresponds to the bias (intercept).
    :param data: A matrix with dimension N x M, where each row corresponds to
    one data point.
    :param targets: A vector of targets with dimension N x 1.
    :param hyperparameters: The hyperparameter dictionary.
    :returns: A tuple (f, df, y)
        WHERE
        f: The average of the loss over all data points.
           This is the same as averaged cross entropy.
           This is the objective that we want to minimize.
        df: (M + 1) x 1 vector of derivative of f w.r.t. weights.
        y: N x 1 vector of probabilities.
    """
    y = logistic_predict(weights, data)
    #####################################################################
    # TODO:                                                             #
    # Given weights and data, return the averaged loss over all data    #
    # points, gradient of parameters, and the probabilities given by    #
    # logistic regression.                                              #
    #####################################################################
    # Hint: hyperparameters will not be used here.
    f, frac_correct = evaluate(targets, y)
    N, M = data.shape
    data_buff = np.concatenate((data, np.ones((N, 1))), axis=1)
    df = np.dot(data_buff.T, y - targets) / float(N)
    #####################################################################
    #                       END OF YOUR CODE                            #
    #####################################################################
    return f, df, y


def logistic_pen(weights, data, targets, hyperparameters):
    """ Calculate the cost of penalized logistic regression and its derivatives
    with respect to weights. Also return the predictions.

    Note: N is the number of examples
          M is the number of features per example

    :param weights: A vector of weights with dimension (M + 1) x 1, where
    the last element corresponds to the bias (intercept).
    :param data: A matrix with dimension N x M, where each row corresponds to
    one data point.
    :param targets: A vector of targets with dimension N x 1.
    :param hyperparameters: The hyperparameter dictionary.
    :returns: A tuple (f, df, y)
        WHERE
        f: The average of the loss over all data points, plus a penalty term.
           This is the objective that we want to minimize.
        df: (M+1) x 1 vector of derivative of f w.r.t. weights.
        y: N x 1 vector of probabilities.
    """
    y = logistic_predict(weights, data)
    #####################################################################
    # TODO:                                                             #
    # Given weights and data, return the averaged loss over all data    #
    # points (plus a penalty term), gradient of parameters, and the     #
    # probabilities given by penalized logistic regression.             #
    #####################################################################
    N, M = data.shape
    lambd = hyperparameters["weight_decay"]
    w = weights[:-1]
    y = logistic_predict(weights, data)
    ce, frac_correct = evaluate(targets, y)
    f = ce + (lambd/2) * np.sum(w * w)
    data_buff = np.concatenate((data, np.ones((N, 1))), axis=1)
    weight_buff = np.copy(weights)
    weight_buff[-1] = 0
    df = np.dot(data_buff.T,y - targets) / float(N) + lambd * weight_buff
    #####################################################################
    #                       END OF YOUR CODE                            #
    #####################################################################
    return f, df, y