# MrktDB

<img src="./mrktdb.png" alt="MrktDB"/>

<br/>

View Platform: http://www.mrktdb.com/

Demo Video: https://youtu.be/Md8tcX2EX_s

<br/>

### Setup

1. Clone this repository
2. Create a virtual environment. (Follow tutorial [here](https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv))
    ```shell
    virtualenv myenv
    ```
3. Activate the virtual environment
    ```shell
    source myenv/bin/activate
    ```
4. Install all the required packages from `requirements.txt`
    ```shell
    pip install -r requirements.txt
    ```
    Install all the required packages for working with React.js
    ```shell
    npm install
    ```
5. Install mongodb-community version 4.2.8

    ##### On Mac-

    ```shell
    brew install mongodb-community@4.2
    ```

    ##### On Windows-

    Follow this tutorial to install it interactively:

    https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/

    Follow this to install from the command prompt:

    https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows-unattended/

6. Follow this tutorial to run mongodb:

    https://www.youtube.com/watch?v=nJVbTnNdqL0

7. You are ready to run the Django app. To run django app follow the django tutorial

### Running the server and react app

1. Go to the directory having manage.py

2. Run -
    ```shell
    python manage.py runserver
    ```
    to run the Django server. Open and terminal window and go to same directory as manage.py, and Run -
    ```shell
    npm run dev
    ```
    to run React

### Setting env variables

1. Create a .env file in the same directory as setting.py

2. Enter the secret variables and their values that you want to use

3. If you are using the application locally then set a variable LOCAL_DB_NAME in the .env file and give it the name of local database that you want to use

4. Go to the directory containing the .env file and run this command in the terminal:
    ```shell
    eb setenv `cat .env | sed '/^#/ d' | sed '/^$/ d'`
    ```

### Check if the database is connected successfully (To test the mongo database in EC2)

1.  Go to the admin page by using URL/admin as the url in the browser.

    URL = http://mrktdbapi-prod.eba-ae6apzne.us-west-2.elasticbeanstalk.com for the deployed app

    URL = http://127.0.0.1:8000 if you're running the app locally

2.  Enter the login credentials

3.  Then you'll land on the site administration page. Look for the TESTAPP and click Add.

4.  Make an entry in the testapp and click SAVE. (testapp is an app made solely for checking the database connection)

5.  Run this command in your terminal to access the database hosted in EC2:

    ```shell
    mongo -u user -p pwd IP/db
    ```

    where,

    user = username for the database hosted in EC2

    pwd = password for the database hosted in EC2

    IP = IP of EC2 instance

    db = database name that is hosted in EC2

                                               OR

    Run

    ```shell
    mongo
    ```

    in your terminal to enter the mongo console. Use the database: " market-db-local " and check for your entry.

### Working of Database

The application hits local MongoDB when running in our system and when it runs on AWS it uses the MongoDB in EC2 instance.

### How to make a contribution ?

1. Create a new branch before making any change.
2. Add all new packages to `requirements.txt` (Make sure you are in a virtual environment before doing this)
    ```shell
    pip freeze > requirements.txt
    ```
3. Put up a PR for review.

### How to transfer data from CIK_CUSIP.csv to Database ?

Run the following command in virtual environment.

```
python cik_scraper.py
```

### Version

-   Python 3.7.3
