# Spartz Challenge
Objective was to implement some basic API end points. In the project exists a set of sample data in `cities.csv` and `users.csv`. A few basic operations on the data provided are implemented, including listing the cities in a given state, listing cities near another city, and registering a visit to a particular city by a user. 

## Prerequisites
*	[Python](https://www.python.org/)
* 	[Flask](http://flask.pocoo.org/)
*	[pip](https://www.pypa.io/en/latest/)
*	[virtualenv](https://virtualenv.pypa.io/en/stable/)

## Installation

1. Clone the repository
```
git clone git@github.com:smithsa/spartz_api.git
```
2. Install requirements found in requirements.txt. You can install manually or using pip. To instal via pip follow theses commands:

a. navigate to directory
```
cd spartz_api
```

b. pip install requirements

```
pip install -r requirements.txt
```

3. Once requirements are installed activate the virutal environement
```
source venv/bin/activate
```

4. run the server
```
 python server.py
```



## Usage

1. List all cities in a state

	`GET /v1/states/{state}/cities`

2. List cities within a 100 mile radius of a city

	`GET /v1/states/{state}/cities/{city}?radius=100`

3. Allow a user to update a row of data to indicate they have visited a particular city.

	`POST /v1/users/{user}/visits`

	```
	{
		"city": "Chicago",
		"state": "IL"
	}
	```

4. Return a list of cities the user has visited

	`GET /v1/users/{user}/visits`


## Additional Notes
I chose to use python and flask because flask-Restful provided a light weight solution.
It's a json api since json is simple and easy to use compared to xml.
In addition, I am utilizing an ORM, SQLAlchemy because it provided for faster development.
