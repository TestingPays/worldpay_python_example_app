# Worldpay Python Example Application

Integrated example application using [Worldpay's Auth API](https://developer.worldpay.com/jsonapi/docs/make-payment).

## Requirements

This demo application will run with either 2.7.X and 3.6.X You can have multiple Python versions (2.x and 3.x) installed on the same system without problems. See [Python Virtual Environments](http://docs.python-guide.org/en/latest/dev/virtualenvs/) for more information.

## Running

### Requirements.txt

See [requirements.txt](requirements.txt) above for required packages or install using pip install as shown here.

```bash
$ pip install -r requirements.txt
```

### API Keys

Prior to running the server it is necessary to add your Worldpay Service key, or use your Testing Pays API key. By having setting file split between dev and prod this makes pointing to Testing Pays while in development mode seamless. Add the Testing Pays API key to WORLDPAY_SERVICE_KEY in the dev.py found in [worldpay_python_example_app/settings](worldpay_python_example_app/settings).

### Database migrations

Prior to starting the django server it is necessary to run data migrations. This can be done by running the following migrate command.

```bash
$ python manage.py migrate --settings=worldpay_python_example_app.settings.dev
```

### Run Server

```bash
$ python manage.py runserver 8000 --settings=worldpay_python_example_app.settings.dev
```

### Using it with Testing Pays

[Testing Pays](http://www.testingpays.com) lets you test and simulate more than you would be able to do with regular API sandboxes. The application is setup so you can avail using your [Testing Pays API key](https://admin.testingpays.com) to test and prepare for errors, validation issues, server errors or even network outages.
