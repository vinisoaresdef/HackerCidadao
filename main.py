from flask import Flask, render_template
import googlemaps

app = Flask(__name__, template_folder='Bootstrap/Impact',static_folder='Bootstrap/Impact/assets')
gmaps = googlemaps.Client(key='AIzaSyBYx4u1Hc1VEeA8b8EscFBYTMJv0on1JRI')

@app.route('/mapa')
def exibir_mapa():
    return render_template('matel.html')

if __name__ == '__main__':
    app.run()