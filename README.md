## ArcticleDirectoryApi

Compatibility
=============

Flask-RestPlus requires Python 3.7+

Installation
============
#### Clone the repo
    $ git clone https://github.com/olegrepetko/ArcticleDirectoryApi.git
    $ cd ArcticleDirectoryApi

##### Create the virtualenv
    $ py -3 -m pip install virtualenv
    $ py -3 -m virtualenv venv
    $ venv\Scripts\activate
    
##### Install dependencies
    $ py -3 -m pip install -r requirements.txt

## Test
    $ $env:ENV_FILE_LOCATION="../.env.test" 
    $ py -3 -m unittest discover tests
    
## Start 
    $ env:ENV_FILE_LOCATION="../.env"
    $ py -3 start.py
