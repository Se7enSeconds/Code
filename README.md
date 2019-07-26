## About US_Presidents_Repo

US_Presidents.py processes US_Presidents.json file, manipulate the data and return a csv file from Flask

### Class and Methods

Private Method(s):

    ._removeFederalist() remove presidents from Federalist party
    
    ._sortCenturyFName() group data by century of start year then sort by first letter in first name
    
    ._reverseFName() keep only first name and reverse it, for example: "Benjamin" --> "nimajneB"
    
    ._acronymParty() store party information as an acronym, for example: "Whig" --> "W", "Democrat" --> "D"
    
    ._yearBegin() keep only the year the president began their term in "mm-dd-yyyy" format
    
    ._finalize() remove unneeded data and rename headers
    
    ._manipulate() integrate above private methods and execute in sequence to manipulate data
    
Public Method(s):

    .fetch_data() manipulate data, return as a pandas dataframe, then reset to default
