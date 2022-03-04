# Run the server
1. Create virtualenv `virtualenv venv -p PYTHON_3_10_PATH`
2. Activate virutalenv with:
    * `source venv/bin/activate` on linux
    * `venv/Scripts/activate.bat` on windows
4. `pip install -r req.txt`
5. Run one of:
    * `FLASK_APP="app" FLASK_ENV="development" python -m flask run` 
    * `python app.py`
