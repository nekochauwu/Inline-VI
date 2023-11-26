from flask import render_template, url_for
from app import app, db, mail
from app.models import Users
from app.forms import UserForm

bike_brands = ['bmw', 'ducati', 'harley_davidson', 'honda', 'kawasaki', 'royal_enfield', 'suzuki', 'triumph']
parts_list = ['agv_helmets', 'air_filters', 'auto_spare_parts', 'brake_pads', 'chain_set', 'liqui_moli']

@app.route('/')
@app.route('/index')
def index():
  return render_template('./pages/home.html')

@app.route('/about')
def about():
  return render_template('./pages/about.html')

@app.route('/brands')
def brands():
  return render_template('./pages/brands.html', brands=bike_brands)

@app.route('/parts')
def parts():
  return render_template('./pages/parts.html', parts=parts_list)

@app.route('/personal_details', methods=['GET','POST'])
def personal_details():
  form = UserForm()

  if form.is_submitted():
    mail.send(to=form.email.data,
              subject='Support',
              contents=f'Hi {form.first_name.data},\n\nAn agent will contact you shortly\n\nRegards,\nInline VI')
    user = Users(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data)
    with app.app_context():
      db.session.add(user)
      db.session.commit()
  else:
    print('Data not inserted')

  return render_template('personal_details.html', form=form)

@app.route('/brand/<string:name>')
def brand(name):
  return render_template('./bikes/'+name+'.html')