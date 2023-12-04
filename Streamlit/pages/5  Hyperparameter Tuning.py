import streamlit as st
import pandas as pd
from sklearn import svm, datasets
from sklearn.model_selection import GridSearchCV
option = ''
option = st.session_state['option']
if option is not None:
    if option == 'SVC':

        number1 = st.number_input('Insert first parameter', step=1, value=0, min_value=0)

        number2 = st.number_input('Insert second parameter', step=1, value=0, min_value=0)

        number3 = st.number_input('Insert third parameter', step=1, value=0, min_value=0)

        # count2 = 0
        # increment2 = st.button('Increment second value', count2)
        # if increment2:
        #     count2 += 1
        #
        # count3 = 0
        # increment3 = st.button('Increment third value', count3)
        # if increment3:
        #     count3 += 1

        if st.button('Calculate best parameter'):
            clf = GridSearchCV(svm.SVC(gamma='auto'), {  #Hyperparameter tuning part
                'C': [number1, number2, number3],
                'kernel': ['rbf', 'linear']
            }, cv=5, return_train_score=False)
            x = st.session_state['x']
            y = st.session_state['y']
            clf.fit(x, y)
            df = pd.DataFrame(clf.cv_results_)
            st.info(clf.best_params_)
            st.info(clf.best_score_)

    else:
        st.error('First upload the data')

else:
    st.error('Test the model first')
