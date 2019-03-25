# this script is meant to be copied to the server and then executed there
# assumes that the user has read-access to the relevant repositories
#
# scp  update_sober* $sober_server_ip4:/tmp



ORIG_DIR=$(pwd)

real_site_specific_settings=$(cat update_sober_site_specific_settings.py)

cd $HOME/sober_deploy

source soberenv/bin/activate

# new clone to avoid merge conflicts
rm -rf django-sober
git clone --depth 1 git@localhost:django-sober

if [ -d "django-sober-site" ]; then
  # if the dir exists  make db backup before deleting the dir
  cd django-sober-site/sober_site
  python3 -c "import sober.utils as u; u.save_stripped_fixtures(backup=True)"
  cd ../..
fi

rm -rf django-sober-site
git clone --depth 1 git@localhost:django-sober-site


cd django-sober
# git checkout -f  || exit 1
# git pull  -f || exit 1
pip install -r requirements.txt

cd ../django-sober-site/
git checkout -f  || exit 1
git pull  -f || exit 1
pip install -r requirements.txt

# additional package which is used only to generate backups
pip install demjson


# this script assumes that the executing user is member of the group www-data

chgrp www-data sober_site
chmod 775 sober_site
cd sober_site


echo "$real_site_specific_settings" > sober_site/site_specific_settings.py

# create the data base (sqlite)
python3 manage.py makemigrations
python3 manage.py migrate

chgrp www-data db.sqlite3
chmod 664 db.sqlite3


# install the sample data from the sober app
python3 -c "import sober.utils as u; u.load_fixtures_to_db(ask=False)"

# ensure everything works
python3 manage.py test sober

python3 manage.py collectstatic

cd $ORIG_DIR

sudo apache2ctl restart

