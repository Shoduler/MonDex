# MonDex
This application provides information about various POKéMON. It does not have a GUI, only a Python-based API which follows the *REST* standards and uses *JSON*.

## Installation
The MonDex API requires the Python modules *Flask*, *SQLAlchemy*, *Flask-SQLAlchemy*, *itsdangerous*, *Jinja2*, *MarkupSafe* and *Werkzeug*.

## Usage
To use the API, the module [requests](http://docs.python-requests.org/en/latest/) is recommended. No authentication is needed to access the data.


##### Access all POKéMON
Use the HTTP method ```GET``` and the URI ```/mondex``` to access a list of all POKéMON.

```python
	r = requests.get(url + "/mondex")
	all = json.loads(r.text)["mon"] # Contains a map of all POKéMON and their respective features.
	print(all[0]["name"]) # Prints the name of the POKéMON at index 0.
```


##### Access a single POKéMON
Use the HTTP method ```GET``` and the URI ```/mondex/id``` to access a specific POKéMON.

```python
	r = requests.get(url + "/mondex/1")
	mon = json.loads(r.text)["mon"] # Contains a map of BULBASAUR's features.
	print(mon["name"]) # Prints "Bulbasaur".
```
