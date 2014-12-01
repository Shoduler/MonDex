# MonDex
This application provides information about various POKÈMON. It does not have a GUI, only a Python-based API which follows the *REST* standards and uses *JSON*.

## Installation
The MonDex API requires the Python modules *Flask*, *SQLAlchemy*, *Flask-SQLAlchemy*, *itsdangerous*, *Jinja2*, *MarkupSafe* and *Werkzeug*.

## Usage
To use the API, the module [requests](http://docs.python-requests.org/en/latest/) is recommended. No authentication is needed to access the data.


##### Access all POKÈMON
Use the HTTP method ```GET``` and the URI ```/mondex``` to access a list of all POKÈMON.

```python
	r = requests.get(url + "/mondex")
	all = json.loads(r.text) # Contains a map of all POKÈMON and their respective features.
	print(all[0]["name"]) # Prints the name of the POKÈMON at index 0.
```


##### Access a single POKÈMON
Use the HTTP method ```GET``` and the URI ```/mondex/id``` to access a specific POKÈMON.

```python
	r = requests.get(url + "/mondex/1")
	mon = json.loads(r.text) # Contains a map of BULBASAUR's features.
	print(mon["name"]) # Prints "Bulbasaur".
```