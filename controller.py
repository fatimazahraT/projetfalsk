from flask import (
    Flask,
    send_file,
    redirect,
    render_template
)
from models import Client
from dal import IotDao
import matplotlib
from matplotlib import pyplot as plt
from io import BytesIO
app=Flask(__name__)
matplotlib.use('agg')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/visualize')
def visualise():
    figure=plt.figure()
    data=IotDao.getAllTemp()
    temp=[]
    dates=[]
    for id,mac,t,date in data:
        temp.append(t)
        dates.append(date)
    plt.plot(dates,temp)
    img=BytesIO()
    figure.savefig(img)
    img.seek(0)
    return send_file(img,mimetype='image/png')
   
@app.route('/clients')
def list_clients():
    clients = Client.query.all()

    return render_template('clients.html', clients=clients)  
    
