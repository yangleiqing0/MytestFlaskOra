from flask.views import MethodView
from flask import render_template
from modles.testcase import TestCases
from flask import Blueprint
from app import cdb


testcase_blueprint = Blueprint('testcase_blueprint', __name__)



# @app.route('/testcaselist/')
class TestCastList(MethodView):


    def get(self):
        sql = 'select ROWID,id,name,url,data,result,method from testcases'
        tests = cdb().query_db(sql)
        return render_template('test_case_list.html', items=tests)
    
testcase_blueprint.add_url_rule('/testcaselist/', view_func=TestCastList.as_view('testcaselist'))