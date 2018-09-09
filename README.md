# sober_site

This repo serves as deployment helper for [django-sober][1].

Django distinguishes between projects and apps. One project can include multiple apps and one app
can be part of many projects. [django-sober][1] is an app. This repo contains a django-project,
which is configured such that the app can be tested locally with little effort

[1]: https://to-be-announced
# Local deployment

**Note: The following instructions are for experienced users which understand each command.
Obviously they are meant to simplify a first test but not recommended for production deployment.
They are tested on Debian 8 and 9.**

    mkdir sober_deploy
    cd sober_deploy

    # download the django-app
    git clone url:sober


    # download the django-project
    git clone url:sober_site

    virtualenv soberenv
    source soberenv/bin/activate

    cd sober

    # install app in development mode (symliks to this dir)
    # all dependencies should be installed automatically
    pip install -e .

    cd ../sober_site

    # create the data base (sqlite)
    python3 manage.py migrate

    # fill out the questions
    python3 manage.py createsuperuser

    # install the sample data from the sober app
    python3 -c "import sober.utils as u; u.load_fixtures_to_db()"

    # ensure everything works
    python3 manage.py test sober

    python3 manage.py runserver

