from flask import Flask,request,url_for,redirect,render_template,session
import urllib2, json

app=Flask(__name__)
app.secret_key = 'hi'

@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="GET":
        return render_template("index.html")
    else:
        search = request.form['search']
        button = request.form['b']
        session['search'] = search
        if (button == "Clear" or search == None):
            return render_template("index.html")
        else:
            return redirect(url_for('results'))

@app.route("/results")
def results():
    query = session.pop('search', None)
    api_key = 'krzzdufmpnnbcv4evzufshcd'
    movie = query.replace(' ', '+')
    url = 'http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=' + api_key + '&q=' + movie + '&page_limit=1'
    json_obj = urllib2.urlopen(url)
    data = json.load(json_obj)
    critic = data['movies'][0]['ratings']['critics_score']
    audience = data['movies'][0]['ratings']['audience_score']
    synopsis = data['movies'][0]['synopsis']
    poster = data['movies'][0]['posters']['profile']
    release_date = data['movies'][0]['release_dates']['theater']
    cast = ''
    for item in data['movies'][0]['abridged_cast']:
        cast = cast + item['name'] + ', '
    cast = cast[:-1]    
    movie = query
    return render_template("results.html",critic=critic,audience=audience,synopsis=synopsis,poster=poster,release_date=release_date,cast=cast,movie=movie)



if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=8008)

