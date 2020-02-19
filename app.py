from flask import render_template, request

from manage import app, mongo, Individual_GIS, Individual_NHIA, db


def add_citizens():
    person_1 = Individual_GIS(
       first_name="Priscy",
        last_name="Owusu",
        age=20,
        email="priscy@gmail.com"
    )
    person_2 = Individual_NHIA(
         first_name="Makay",
        last_name="Hotor",
        age=19,
        email="makay@gmai.com"
    )
    person_3 = {
        "first_name": "Jose",
        "last_name": "Akubilah",
        "age": "15",
        "email":"jose@gmail.com"
    }
    person_4 = Individual_GIS(
        first_name="Sumy",
        last_name="Asare",
        age=22,
        email="sumy@gamil.com"
    )
    person_5 = Individual_NHIA(
        first_name="Prince",
        last_name="Kwei",
        age=29,
        email="prince@gmail.com"
    )
    person_6 = {
        "first_name": "David",
        "last_name": "Appiah",
        "age": "25",
        "email":"david@gmail.com"
    }

    db.session.add(person_1)  # Adds new User record to database
    db.session.add(person_2)  # Adds new User record to database
    db.session.add(person_4)  # Adds new User record to database
    db.session.add(person_5)
    db.session.commit()
    mongo.db.individual_DVLA.insert(person_3, person_6)


@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []

    #add_citizens()
    if request.method == "POST":
        email = request.form['email']

        if email :
            results_GIS = Individual_GIS.query.filter_by(email=email).all()
            results_NHIA = Individual_NHIA.query.filter_by(email=email).all()

            citizens = mongo.db.individual_DVLA
            results_DVLA_1 = []
            for c in citizens.find():
                results_DVLA_1.append(
                    {'first_name': c['first_name'],  'last_name': c['last_name'],
                     'age': c['age'],'email': c['email']})

            results_DVLA = []
            for citizen in results_DVLA_1:
                if citizen['email'] == citizen['email'] == email:
                    results_DVLA.append(
                        {'first_name': citizen['first_name'],
                         'last_name': citizen['last_name'],
                         'age': citizen['age'],'email': c['email']})

            return render_template('results.html', results_GIS=results_GIS,
                                   results_NHIA=results_NHIA, results_DVLA=results_DVLA)
        else:
            errors = {"error": "The request payload is not in JSON format"}

    return render_template('index.html', errors=errors)


@app.route('/results', methods=['GET', ])
def results():
    return render_template('results.html')


if __name__ == "__main__":
    app.run()
