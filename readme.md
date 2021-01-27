# Worker Verifier

This is a project to verify authorized Mturkers. 

## How to setup

Make sure to have Python 3 installed, and run commands below to set up.

```bash
$ python -m venv ./env
$ source ./env/bin/activate
(env)$ pip install -r requirements.txt
```
```cmd
$ python -m venv env
$ env\Scripts\activate.bat
(ent) $ pip install -r requirements.txt
```
## How to develop

To run development server, run the command below.

```bash
(env)$ FLASK_ENV=development python main.py
```

## How to run in production mode

To run this web app in production mode, run the command below.
```bash
(env)$ sh run.sh
```
```cmd
set FLASK_APP=main
set FLASK_ENV=development
flask run
```
Try http://localhost:25100 on a web browser.


## Results

Participants who submitted the answer will get a code that looks like: 

`{user_id_with_16_digits_and_letters}`

The results are saved in `./user_ids/{user_id}.json`. 



