## Deployment on Heroku

### Procfile

Create Procfile for Heroku in root, and edit:

```
web: gunicorn app:app
```

### Install heroku-cli and create a new app on Heroku

[Download and install the Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line).

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.

Also create a new MY_SECRET_KEY with your app config environ variable

```bash=
$ heroku login
```

### Create a new Git repository

Initialize a git repository in a new or existing directory

```bash=
$ cd my-project/
$ git init
$ heroku git:remote -a 'your app name'
```

### Deploy your application

Commit your code to the repository and deploy it to Heroku using Git.

```bash=
$ git add .
$ git commit -m "make it better"
$ git push heroku master
```

For existing repositories, simply add the heroku remote

```
$ heroku git:remote -a 'your app name'
$ git add .
$ git commit -m "make it better"
$ git push heroku master
```

### Create new postgres db for your new app

```
$ heroku addons:create heroku-postgresql:hobby-dev --app 'new app name'
```

### Run db migrate on Heroku

```bash=
$ heroku run flask db upgrade
```

### Logging

```
heroku logs --tail
```
