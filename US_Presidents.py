from flask import *
from datetime import datetime
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None

class US_Presidents:

  _json_file = r"./US_Presidents.json"

  def __init__(self):
    self._reset()

  def _reset(self):
    self._data = pd.read_json(self._json_file)

  def _removeFederalist(self):
    self._data = self._data[self._data['pp'].apply(lambda val: 'Federalist' not in val)]

  def _sortCenturyFName(self):
    self._data['ct'] = self._data['tm'].str.split('-')
    self._data['ct'] = self._data['ct'].apply(lambda val: val[0])
    self._data['ct'] = self._data['ct'].apply(lambda val: int(np.floor(int(val)/100))+1)
    self._data.sort_values(by=['ct','nm'],ascending=[True,True],inplace=True)

  def _reverseFName(self):
    self._data['nm'] = self._data['nm'].str.split(' ')
    self._data['nm'] = self._data['nm'].apply(lambda val: val[0][::-1])

  def _acronymParty(self):
    self._data['pp'] = self._data['pp'].apply(lambda val: ''.join([c for c in val if c.isupper()]))

  def _yearBegin(self):
    self._data['tm'] = self._data['tm'].str.split('-')
    self._data['tm'] = self._data['tm'].apply(lambda val: 'mm-dd-%s' % val[0])

  def _finalize(self):
    self._data.reset_index(drop=True,inplace=True)
    self._data.drop(labels=['id','ct'],axis=1,inplace=True)
    self._data = self._data.reindex(['nm','pp','tm','president'],axis=1)
    new_names = {
      'nm':'Name',
      'pp':'Party',
      'tm':'Presidential Term',
      'president':'President Number'
    }
    self._data.rename(new_names,axis=1,inplace=True)

  def _manipulate(self):
    for func in (self._removeFederalist,
                 self._sortCenturyFName,
                 self._reverseFName,
                 self._acronymParty,
                 self._yearBegin,
                 self._finalize):
      func()

  def fetch_data(self):
    self._manipulate()
    manipulated_data = self._data
    self._reset()
    return manipulated_data

app = Flask(__name__)

@app.route("/US_Presidents")
def display():
  data = US_Presidents().fetch_data()
  return data.to_html(index=False)

@app.route("/US_Presidents/download")
def download_csv():
  data = US_Presidents().fetch_data()
  data['Ingestion Time'] = datetime.now().strftime('%b-%d-%Y %H:%M:%S')
  resp = make_response(data.to_csv(index=False))
  resp.headers["Content-Disposition"] = "attachment; filename=US_Presidents.csv"
  resp.headers["Content-Type"] = "text/csv"
  return resp

if __name__ == "__main__":
  app.run(debug=True)
