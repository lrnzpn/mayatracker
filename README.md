# mayatracker

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

# tracker API

### Enter virtual environment and install dependencies
```
cd trackerapi 
source env/bin/activate
pip install -r requirements.txt
```

### Create .env and add secret key
```
cd trackerapi/trackerapi
touch .env

SECRET_KEY=django-insecure-s6%0&+0%pe$02$z@c05^qb+p9kxf^xr#w%duv(m7#c$u5&=dof
```

### Migrate and run the server
```
python manage.py migrate && python manage.py runserver
```
