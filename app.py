from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
engine = create_engine('sqlite:////home/vagrant/database.sqlite', convert_unicode=True)
db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)
Base = declarative_base()
Base.query = db_session.query_property()

class Language(Base):
    __tablename__ = 'language'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    
    def __init__(self, name):
        self.name = name

@app.route('/')
def index():
    languages = Language.query.all()
    return render_template('index.html', languages=languages)
    
@app.route('/create/', methods=['POST'])
def create():
    language = Language(name=request.form['name'])
    db_session.add(language)
    db_session.commit()
    return redirect(url_for('index'))  

@app.route('/update/<language_id>/', methods=['GET', 'POST'])
def update(language_id):
    language = Language.query.get(language_id)

    if request.method == 'POST':
        language.name = request.form['name']
        db_session.add(language)
        db_session.commit()
        return redirect(url_for('index'))
        
    return render_template('update.html', language=language)
 
@app.route('/delete/<language_id>/')
def delete(language_id):
    language = Language.query.get(language_id)
    db_session.delete(language)
    db_session.commit()
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    app.run(host='0.0.0.0')