from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'dedkek'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False