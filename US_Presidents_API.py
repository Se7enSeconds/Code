from flask import *
from datetime import datetime
from US_Presidents import US_Presidents

app = Flask(__name__)

onInstance = US_Presidents()
data = onInstance.fetch_data()

@app.route("/US_Presidents/")
def display():
  data['Ingestion Time'] = datetime.now().strftime('%b-%d-%Y %H:%M:%S')
  return data.to_html(index=False)

@app.route("/US_Presidents/download")
def download_csv():
  response = make_response(data.to_csv(index=False))
  response.headers["Content-Disposition"] = "attachment; filename=US_Presidents.csv"
  response.headers["Content-Type"] = "text/csv"
  return response

if __name__ == "__main__":
  app.run(debug=True)