class Metrics:
    def __init__(self):
        pass

#comment
    def accuracy(self,y_true,y_pred):
        '''
        Function to calculate accuracy
        :param y_true: list of true values
        :param y_pred: list of predicted values
        :return: accuracy score
        '''
        correct_counter = 0
        for yt,yp in zip(y_true,y_pred):
            if yt == yp:
                correct_counter += 1
        return  correct_counter/len(y_true)

    def true_positive(self,y_true,y_pred):
        '''
        Function to calculate accuracy
        :param y_true: list of true values
        :param y_pred: list of predicted values
        :return: accuracy score
        '''
        tp_counter = 0
        for yt,yp in zip(y_true,y_pred):
            if yt == 1 and yp == 1:
                tp_counter += 1
        return  tp_counter

    def true_negative(self,y_true,y_pred):
        '''Function to calculate accuracy
        :param y_true: list of true values
        :param y_pred: list of predicted values
        :return: accuracy score

        '''
        tn_counter = 0
        for yt,yp in zip(y_true,y_pred):
            if yt == 0 and yp == 0:
                tn_counter += 1
        return  tn_counter

    def false_positive(self,y_true,y_pred):
        '''
        Function to calculate accuracy
        :param y_true: list of true values
        :param y_pred: list of predicted values
        :return: accuracy score
        '''
        fp_counter = 0
        for yt,yp in zip(y_true,y_pred):
            if yt == 0 and yp == 1:
                fp_counter += 1
        return  fp_counter

    def false_negative(self,y_true,y_pred):
        '''
        Function to calculate accuracy
        :param y_true: list of true values
        :param y_pred: list of predicted values
        :return: accuracy score
        '''
        fn_counter = 0
        for yt,yp in zip(y_true,y_pred):
            if yt == 1 and yp == 0:
                fn_counter += 1
        return  fn_counter

    def accuracy_v2(self,y_true, y_pred):

        """
        Function to calculate accuracy using tp/tn/fp/fn
        :param y_true: list of true values
        :param y_pred: list of predicted values
        :return: accuracy score
        """
        tp = true_positive(y_true, y_pred)
        fp = false_positive(y_true, y_pred)
        fn = false_negative(y_true, y_pred)
        tn = true_negative(y_true, y_pred)
        accuracy_score = (tp + tn) / (tp + tn + fp + fn)
        return accuracy_score

    def precision(self,y_true,y_pred):
        '''
        out of all predicted values how many are actual true
        tp/tp+fp
        '''
        tp = true_positive(y_true,y_pred)
        fp = false_positive(y_true,y_pred)

        return tp/(tp+fp)

    def recall(self,y_true,y_pred):
        '''
        out of all true value, how many were predicted correct
        tp/tp+fn
        '''
        tp = true_positive(y_true,y_pred)
        fn = false_negative(y_true,y_pred)

        return tp/(tp+fn)


