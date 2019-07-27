from flask.views import MethodView
from flask import render_template



class Home(MethodView):
    
    def get(self):
        return render_template('homepage.html')
    
