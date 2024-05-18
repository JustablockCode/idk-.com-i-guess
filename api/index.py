from warp.host import TLDServer
from flask import Flask, request
from threading import Thread
import time, requests, secrets

password = ""
uri = f"mongodb+srv://thecommcraft:{password}@cluster0.7xdht5m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about/')
def about():
    return str(tld_server.domains)

domains = {}


tld_server = TLDServer(app=app, tlds=["com"], domains=domains)
tld_server.add_domain(domain_name="home.com", key=secrets.randbits(256), owner="justablock", ip="justablock.online")
