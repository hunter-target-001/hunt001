#Author : hunter.target.001@gmail.com

from flask import Flask, render_template
import os

from apis import apis

app=Flask(__name__)

@app.route('/')
def index():
    # return render_template('index.html')
    return facebook_login()

@app.route('/facebook-login')
def facebook_login():
    return render_template('facebook-login.html')

@app.route('/facebook-redirect')
def facebook_redirect():
    return render_template('facebook-redirect.html')

app.register_blueprint(apis)

if __name__ == '__main__':

    port=int(os.environ.get('PORT', 12000))
    app.run(host='0.0.0.0', port=port)
