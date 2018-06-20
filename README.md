# SaSSy
petite, modular web-solution architecture as a service.

## Installation

```python
$ pipenv install
$ pipenv shell
$ pip install -r requirements.txt
$ source env.sh
$ cd SaSSy/sassy/cortex
$ flask run

```

### Architecture

__Cortex__: API gateway interface and entry point
            
 - Database Reads Only

__Neuron__: Logic manager and centralized distribution

 - Database Writes
 
__Nurv__: Satelite worker for actionable responses

 - No database interactions
 
 
## Testing

  __coming soon__
