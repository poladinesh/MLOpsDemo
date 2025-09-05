### Install Python Virtual Environment (Mac)

    For Mac:
        
        python3 -m venv .
        source ./bin/activate
        python3 -m pip install -r requirements.txt

    For Windows:

        python3 -m venv .
        .\Scripts\activate
        python3 -m pip install -r requirements.txt

### Train the Model (produce pkl file required)

        python train.py

### Run the app

        uvicorn main:app --reload