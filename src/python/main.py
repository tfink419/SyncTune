from flask import Flask, session, redirect, url_for, escape, request, render_template
from urllib import urlencode
from env.dev import client_id, client_secret, SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY

@app.route('/')
def index():
    if 'spotify_code' in session:
        spotify_code = session['spotify_code']
    else:
        spotify_code = ''
    return render_template('dev_index.html', spotify_code=spotify_code)

@app.route('/login')
def spotify_login():
    if 'spotify_code' in session:
        spotify_code = session['spotify_code']
    scope = 'user-read-private user-read-email';
    url = 'https://accounts.spotify.com/authorize?'
    params = {
          'response_type': 'code',
          'client_id': client_id,
          'scope': scope,
          'redirect_uri': 'http://localhost:5000/spotify_auth'
        #   'state': 'ABC123'
        }
    return redirect(url+urlencode(params))
@app.route('/spotify_auth')
def spotify_login_callback():
    if request.args.get('code'):
        spotify_code = request.args.get('code')
    print('spotify code:', spotify_code)
    session['spotify_code'] = spotify_code
    return redirect('/')
  # 
  # // your application requests refresh and access tokens
  # // after checking the state parameter
  # 
  # var code = req.query.code || null;
  #   var authOptions = {
  #     url: 'https://accounts.spotify.com/api/token',
  #     form: {
  #       code: code,
  #       redirect_uri: redirect_uri,
  #       grant_type: 'authorization_code'
  #     },
  #     headers: {
  #       'Authorization': 'Basic ' + (new Buffer(client_id + ':' + client_secret).toString('base64'))
  #     },
  #     json: true
  #   };
  # 
  #   request.post(authOptions, function(error, response, body) {
  #     if (!error && response.statusCode === 200) {
  # 
  #       var access_token = body.access_token,
  #           refresh_token = body.refresh_token;
  # 
  #       var options = {
  #         url: 'https://api.spotify.com/v1/me',
  #         headers: { 'Authorization': 'Bearer ' + access_token },
  #         json: true
  #       };
  # 
  #       // use the access token to access the Spotify Web API
  #       request.get(options, function(error, response, body) {
  #         console.log(body);
  #       });
  # 
  #       // we can also pass the token to the browser to make requests from there
  #       res.redirect('/#' +
  #         querystring.stringify({
  #           access_token: access_token,
  #           refresh_token: refresh_token
  #         }));
  #     } else {
  #       res.redirect('/#' +
  #         querystring.stringify({
  #           error: 'invalid_token'
  #         }));
  #     }
  #   });
  # }


if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)
