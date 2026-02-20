from flask import Flask , jsonify , render_template , request
import requests
import pandas as pd
import pickle

app = Flask(__name__)

# @app.route('/create_user',methods = ['POST'])
# def create_user():
#     return jsonify({'msg' : 'POST_METHOD'})


# @app.route('/get_user',methods = ['GET'])
# def get_user():
#     return jsonify({'msg' : 'GET_METHOD'})


# @app.route('/update_user',methods = ['PUT'])
# def update_user():
#     return jsonify({'msg' : 'PUT_METHOD'})


# @app.route('/delete_user',methods = ['DELETE'])
# def delete_user():
#     return jsonify({'msg' : 'DELETE_METHOD'})






# API_KEY = "cc7b7d8dfe924791ae2663cf2d89389c"
# url = "https://newsapi.org/v2/everything?q=tesla&from=2026-01-17&sortBy=publishedAt&apiKey=cc7b7d8dfe924791ae2663cf2d89389c"

# @app.route('/api/news' , methods = ['GET'])
# def api_news():
    
#     response = requests.get(url)
#     if response.status_code == 200:
#         news_data = response.json()
#         # news_data['articles'][0].keys()
#         first_data = news_data['articles'][0]
#         total_articles = len(news_data['articles'])
#         author = first_data['author']
#         title = first_data['title']
#         published_date = first_data['publishedAt']


#         output_data = {
#             'Total_No_Articles' : total_articles,
#             'author': author,
#             'title' : title,
#             'published_date': published_date
#         }
#         return jsonify(output_data)
    
#     else:
#         return jsonify({'msg': 'Invalid Api Key'})





# @app.route('/' , methods = ['GET'])
# def file():
#     return render_template('form.html')


# @app.route('/upload' , methods = ['POST'])
# def upload_file():
#     file = request.files['file']
#     if file.filename.endswith(".csv"):
#         path = 'userfile/' + file.filename
#         file.save(path)
#         return " we have recieved the data ...... thanks to visiting us "
#     else:
#         return "upload only csv file...."
    

# @app.route('/' , methods = ['GET'])
# def render():
#     return render_template('form.html')


# @app.route('/upload' , methods = ['POST'])
# def uppload_files():
#     file = request.files['file']
#     if file.filename.endswith('.csv'):
#         path = 'userfile/' + file.filename
#         file.save(path)
#         df = pd.read_csv('userfile/Travel.csv')
#         print(df.head())
#         min_pop = float(df['MonthlyIncome'].min())
#         max_pop = float(df['MonthlyIncome'].max())
#         count_pop = float(df['MonthlyIncome'].count())
#         avgerage_pop = float(df['MonthlyIncome'].mean())

#         response = {"minimum_salary": min_pop,
#                     'maximum_salary' : max_pop,
#                     'count_salary' : count_pop,
#                     'avaerage_salary': avgerage_pop}
#         return jsonify(response)
#     else:
#         return "Error hai bhai theek karle"














def get_cleaned_data(form_data):
    gestation = float(form_data['gestation'])
    parity = int(form_data['parity'])
    age = float(form_data['age'])
    height = float(form_data['height'])
    weight = float(form_data['weight'])
    smoke = float(form_data['smoke'])  

    cleaned_data = {
        "gestation" : [gestation],
        "parity" : [parity],
        "age" : [age],
        "height" : [height],
        "weight" : [weight],
        "smoke" : [smoke]
    }
    return cleaned_data


@app.route('/' , methods = ["GET"])
def home():
    return render_template("index.html")




@app.route('/predict' , methods = ['POST'])
def get_prediction():
    baby_data_form = request.form

    baby_data_cleaned = get_cleaned_data(baby_data_form)
    baby_df = pd.DataFrame(baby_data_cleaned)

    with open('model.pkl', 'rb') as obj:
        model = pickle.load(obj)

    prediction = model.predict(baby_df)
    prediction = round(float(prediction[0]), 2)

    response = {'prediction' : prediction}
    return render_template("index.html" , prediction = prediction)

if __name__ == '__main__':
    app.run(debug= True)