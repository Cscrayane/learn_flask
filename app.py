from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Algiers',
    'salary': 'DZD 100000'
  },
  {
    'id': 2,
    'title': 'Data Science',
    'location': 'Oran',
    'salary': 'DZD 200000'
  },
  {
    'id': 3,
    'title': 'Telco',
    'location': 'Remote',
    'salary': 'DZD 120000'
  }
]
  

@app.route('/')
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs, company_name='Ooredoo')

@app.route('/api/jobs')
def return_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route('/job/<id>')
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return 'Not Found', 404
  return render_template('jobpage.html', job=job)

@app.route('/job/<id>/apply',methods=['post'])
def apply_to_job(id):
  data = request.form
  job = load_job_from_db(id)
  return render_template('application_submitted.html', application=data, job=job)
  

app.run(host='0.0.0.0', debug=True)