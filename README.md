# Data Science Project - G31

Data Science project for the course Introduction to Data Science (CS244) during the fourth semester.

## Topic:
Gearbox Fault Analysis using Machine Learning and Data Science.\
Presentation - 
- [Part-1](https://docs.google.com/presentation/d/14HmFRW4bMTIqvRdnrHYgkMq0jVh-rpTuiP8LIkTGbCs/edit?usp=sharing)
- [Part-2](https://docs.google.com/presentation/d/1bciRV9ST2Md8pk72wz22ykiqegdcmwve6ywB_lV3pIE/edit?usp=sharing)

Project Explanation - 
- [Part-1](https://youtu.be/o3-bFDOQUy0)
- [Part-2](https://youtu.be/Szh2v4yI4jY)

### Team:
- Siddharth Gupta
- Yash Ajitsaria
- Pratyush Kumar
- Shivam Singhal 
- Ashfaq Ahmed
- Aarav Arya

## Introduction:
Our project deals with the application of Machine Learning in industrial environemnt in the field of Mechanical Engineering. Given vibrational data collected using 4 vibration sensors placed in four different corners of a gearbox, our model will analyse the data and predict if the gearbox has a broken tooth and hence, if the gearbox is healthy or not. 

## Data Collection:
Dataset used: [Gearbox Fault Analysis - Kaggle](https://www.kaggle.com/brjapon/gearbox-fault-diagnosis) \
Gearbox Fault Diagnosis Data set include the vibration dataset recorded by using SpectraQuest’s Gearbox Fault Diagnostics Simulator.
Dataset has been recorded using 4 vibration sensors placed in four different direction, and under variation of load from '0' to '90' percent. Two different scenario are included: \
[1] Healthy condition and \
[2] Broken Tooth Condition

## Summary:
The problem statement mainly focuses on detection of broken tooth in a gearbox. We aim to design an ML model in order to replace the laborious task of manually checking the gearbox for faults with a prediction-based approach. The data required to detect the fault is gathered using four accelerometers (a1, a2, a3 and a4). [0] and [1] have been used to describe the broken and healthy conditions respectively. While preparing the above-described model, we identified some basic steps. At first the raw data obtained from Kaggle.com has been converted into a readable and easily understandable format which comes under the category of data pre-processing. Pre-processing was followed by data cleaning and visualization wherein we ensured that there were no missing data points and various patterns and anomalies were observed on the basis of which we formed our hypothesis. \
In our hypothesis we aim to prove/disprove that a1 is the dominant factor in determining the fault in a gearbox. Following slides include 3 different types of graphs which have been used to deduce our hypothesis, more commonly included in exploratory data analysis (EDA). The first graph is a KDE plot where we observe a more significant variation in the frequency distribution of broken and healthy data sets of the accelerometer a1 as compared to the other three which can be mathematically represented by the difference in standard deviations of broken and healthy data. Another plot focuses on the mean of distribution of standard deviations of small samples (100) for broken and healthy conditions. The final plot is a time-series graph which represents the actual difference in readings of the four sensors. The key observation in all the three plots indicated that a1 indeed is the most dominant factor. \
However, we have not completely neglected the effects of sensors a2, a3 and a4. The ML-model will be further used to test our hypothesis and hence predict the condition of the gearbox i.e., healthy or broken. \
Right after we formulated our hypothesis from our inferences, we proceeded to implement an ML classification model to prove our hypothesis. We ran three models, namely KNN, Decision tree and Random Forest Classification models. In order to run our models, we’ve compiled our dataset and split it into three parts - testing, evaluation and testing data. We used a 60-20-20 ratio for the training,evaluation and test datasets respectively. Once we implemented these models using sklearn library in Python, we retrieved results for confusion matrix as well as four performance metrics - accuracy, precision, recall and F-score. \
Observing the values of the four metrics, we found that the value for the precision metric was high in all the 3 models. This indicates that the number of false positives are the lowest. This means we are more likely to correctly identify a broken tooth gearbox as broken and less likely to falsely classify a broken tooth gearbox as healthy, which is a favourable outcome for our model.
Hence, we used precision as our favorable metric to test our hypothesis. \
Taking an average value of the metrics for the three models, we found that the precision value for a1 sensor data was 0.6433. This value was significantly higher than that of the datasets of the a2, a3 and a4 sensors. Hence, this proves our alternate hypothesis which states that a1 is the most dominant factor for the detection of fault in the gearbox as compared to a2, a3, a4. \
Although we were able to prove our hypothesis, you may observe that all the performance metric scores were low in all the three models we ran. From this, we may conclude that ML classification models are not the most suitable approach for gearbox fault detection, instead a better approach would be to use a Deep Learning model on the provided dataset.




