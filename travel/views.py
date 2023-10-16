from flask import Blueprint, render_template, request, redirect, url_for
from .models import Destination
from . import db

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    destinations = db.session.scalars(db.select(Destination)).all()    
    return render_template('index.html', destinations=destinations)

@mainbp.route('/search')
def search():
    search_term = request.args.get('search', '')

    if search_term:
        query = "%" + search_term + "%"
        destinations = db.session.execute(db.select(Destination).where(Destination.description.like(query)))
    else:
        destinations = db.session.execute(db.select(Destination))

    destinations = destinations.scalars().all()
    return render_template('index.html', destinations=destinations)