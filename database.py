from sqlalchemy import create_engine, text
import os 


engine = create_engine(f'postgresql+psycopg2://{os.environ['db']}:{os.environ['db_pass']}@{os.environ['host']}/postgres?sslmode=require')

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    result_dicts = []
    for row in result.all():
      result_dicts.append(row._asdict())
    return result_dicts

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f'SELECT * from jobs where id = {id}'))
    row = result.all()
    if len(row) == 0:
      return None
    else : return row[0]._asdict()