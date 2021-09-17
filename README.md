# 7th-Semester-Project

## Details of the project:
This is the minor-project that is to be submitted to my University, during the 7th semester.We build a BiLSTM model and train the model on textual data - Twitter data.
This project includes developing in two stages.

## Stage 1:
In this stage we develop a `Deep Learning` model, to train it on the data for `sentiment classification`. This stage includes:
### 1. Preparing the data: 
The data is prepared from Twitter Scraping. The dataset includes thousands of tweets which are segregated into 3 domains, namely, positive, negative and neutral 
sentiments respecively.

### 2. Preprocessing the data:
-> We First tokenize the data, which consists of sentences or tweets. While tokenizing we also clean the data, cleaning the html codes, removing urls and hashtags, etc.
-> Next we lemmatize the data, to shrink down the vocabulary of the dataset and reduce complexity of the data.
-> Lastly we remove numbers or special characters from the data.

### 3. Preparing the Model:
Lastly, we intantiate the BilSTM model, using the sequential wrapper class. Once the model is trained, then we save the weights of the models to be used later onto the 2nd stage.

## Stage 2:
 In this stage we develop a web application on the `Django framework`. This stage includes:
 ### 1. Developing the Django Application:
 So first we developed the django application and tested it on the development server. The application has a `model-views-template` architectural system. For our project
 we only work upon the `template-views` sytem only as we are not storing data from the website itself.
 
 ### 2. Deploying on `Heroku`:
 Once developed, we deploy the web application on Heroku platform.
 
 
 
 **Link to site**: https://sentiment-analysis-bilstm.herokuapp.com/
  NOTE: The site takes time to load, this is due to the fact that BiLSTM is a heavy model for the free version of heroku hardware.
