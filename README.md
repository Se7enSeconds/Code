## About US_Presidents_Repo

US_Presidents.py manipulate US_Presidents.json file, produce a Pandas Dataframe

US_Presidents_API.py create a Flask API to download manipulated data as CSV file

### About US_Presidents Module

Private Method(s):

    ._removeFederalist() remove presidents from Federalist party
    
    ._sortCenturyFName() group data by century of start year then sort by first letter in first name
    
    ._reverseFName() keep only first name and reverse it, for example: "Benjamin" --> "nimajneB"
    
    ._acronymParty() store party information as an acronym, for example: "Whig" --> "W", "Democrat" --> "D"
    
    ._yearBegin() keep only the year the presidents began their term in "mm-dd-yyyy" format
    
    ._finalize() remove unneeded data and rename headers
    
    ._manipulate() integrate above private methods and execute in sequence to manipulate data
    
Public Method(s):

    .fetch_data() manipulate data, return as a Pandas Dataframe, then reset to default

### To Run Application

Step 1: Launch command prompt, change directory to US_Presidents_Repo

Step 2: Type "python US_Presidents_API.py", press Enter

Step 3: Open web browser, go to http://127.0.0.1:5000/US_Presidents/, manipulated data should display

Step 4: Go to http://127.0.0.1:5000/US_Presidents/download, a CSV file should automatically start downloading


