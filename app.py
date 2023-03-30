from flask import Flask, render_template, request 

import requests 


app = Flask(__name__) 


@app.route('/', methods=['GET', 'POST']) 

def index(): 

    movies = [] 
 

    if request.method == 'POST': 

        #this gets the search query text from the input box on the webpage and stores it in 
        #a local variable called search_query
        search_query = request.form['search_query'] 

        #this is an api key that allows us to search OMBD
        api_key = "f0674f3f" 

        #THis is the URL that goes to OMDB and uses parameters to search
        #the database such as s for movie title
        #Parameters are joined together by &
        url = f"http://www.omdbapi.com/?s={search_query}&apikey={api_key}" 

        # This makes a request to the url
        response = requests.get(url) 

        #This deserializes the response to JSON
        data = response.json() 

        print(data) #look in the terminal at the data 
    return render_template('index.html', movies=movies) 

if __name__ == "__main__": 

    app.run(debug=True) 