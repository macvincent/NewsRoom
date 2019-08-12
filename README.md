# NewsRoom

NewsRoom is a web app aimed at combating disinformation in the political space by crowd sourcing news analysis.

Running this project requires you installing dependent libraries from the `requrements.txt` file

## To install and run app libraries:

1. Run
```
sudo install requirements.txt
```
from the root folder directory. It is advisable to do this from a [virtual environment](https://www.django-rest-framework.org/tutorial/1-serialization/)

2. To make our initial migration of the app model and to sync the database for the first time we run
```
python manage.py makemigrations
python manage.py migrate
```
you should rerun this command anytime you make changes to the `..blog/models.py` file

3. Start the app with a local server by running
```
 python manage.py startserver
```

You can now go ahead, sign up, and change the word by sharing your unbiased news analaysis.

This project is still in it's early stages and open to contribution