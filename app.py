import os
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
engine = create_engine(
    os.environ.get('DATABASE_URL', 'sqlite:////home/vagrant/database.sqlite'),
    convert_unicode=True)
db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)
Base = declarative_base()
Base.query = db_session.query_property()

class Text(Base):
    __tablename__ = 'text'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    
    def __init__(self, name):
        self.name = name

@app.route('/')
def index():
    texts = Text.query.all()
    return render_template('index.html', texts=texts)
    
@app.route('/create/', methods=['POST'])
def create():
    text = Text(name=request.form['name'])
    db_session.add(text)
    db_session.commit()
    return redirect(url_for('index'))  

@app.route('/update/<text_id>/', methods=['GET', 'POST'])
def update(text_id):
    text = Text.query.get(text_id)

    if request.method == 'POST':
        text.name = request.form['name']
        db_session.add(text)
        db_session.commit()
        return redirect(url_for('index'))
        
    return render_template('update.html', text=text)
 
@app.route('/delete/<text_id>/')
def delete(text_id):
    text = Text.query.get(text_id)
    db_session.delete(text)
    db_session.commit()
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    app.run(host='0.0.0.0')