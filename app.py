from flask import Flask, render_template

#initialization
app = Flask(__name__)

#configuration
app.config['FREEZER_DESTINATION'] = 'gh-pages'
app.config['FREEZER_DESTINATION_IGNORE'] = ['.git*', 'CNAME', '.gitignore', 'readme.md']
app.config['FREEZER_RELATIVE_URLS'] = True


HOSTING_DOMAIN = 'http://vsarathy.com/'

#controllers
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/bio.html')
def bio():
    return render_template('bio.html')

@app.route('/research.html')
def research():
    return render_template('research.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/404.html')
def static_404():
    return render_template('404.html')

@app.route('/sitemap.xml')
def generate_sitemap():
    locations = [
        ('',              '2015-06-24'),
    ]
    sites = [(HOSTING_DOMAIN + l[0], l[1]) for l in locations]
    return render_template('sitemap.xml', sites=sites)


#launch
if __name__ == "__main__":
    app.run(debug=True)