# SaSSy
petite, modular web-solution architecture as a service.

Swagger Docs: [URL when running](http://127.0.0.1:5000/apidocs/)

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

```shell
$ tox
```


## Project Status

####Tree:

```shell
tree -I "SaSSy.egg-info|*pyc|*.db|__pycache__" .
.
├── Jenkinsfile
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── README.md
├── junit-sassy.xml
├── requirements.txt
├── sassy
│   ├── __init__.py
│   ├── cortex
│   │   ├── __init__.py
│   │   ├── app.py
│   │   ├── config.py
│   │   ├── env.sh
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   ├── admin
│   │   │   │   └── __init__.py
│   │   │   ├── databases
│   │   │   │   └── __init__.py
│   │   │   ├── resources
│   │   │   │   └── __init__.py
│   │   │   ├── users
│   │   │   │   └── __init__.py
│   │   │   └── websites
│   │   │       └── __init__.py
│   │   └── views
│   │       ├── __init__.py
│   │       ├── admin
│   │       │   ├── __init__.py
│   │       │   ├── admin_base.yml
│   │       │   └── users.py
│   │       ├── base.py
│   │       ├── databases
│   │       │   ├── __init__.py
│   │       │   └── mysql.py
│   │       ├── resources
│   │       │   ├── __init__.py
│   │       │   ├── containers.py
│   │       │   ├── hosts.py
│   │       │   ├── providers.py
│   │       │   └── virtualmachines.py
│   │       ├── users
│   │       │   ├── __init__.py
│   │       │   └── manage_users.py
│   │       └── websites
│   │           ├── __init__.py
│   │           └── website.py
│   ├── neuron
│   │   └── __init__.py
│   ├── nurv
│   │   └── __init__.py
│   └── utils
│       ├── __init__.py
│       ├── communication
│       │   ├── __init__.py
│       │   └── sender.py
│       ├── database
│       │   ├── __init__.py
│       │   ├── db.py
│       │   └── sqlite
│       │       ├── __init__.py
│       │       └── queries.py
│       ├── errors
│       │   ├── __init__.py
│       │   ├── communications.py
│       │   └── database.py
│       ├── logger.py
│       └── tools.py
├── setup.py
├── tests
│   ├── __init__.py
│   ├── test_base.py
│   └── test_routes.py
└── tox.ini
```

####LOC:
```shell
     116 .gitignore
      12 Jenkinsfile
      21 LICENSE
      16 Pipfile
      62 Pipfile.lock
      44 README.md
      20 requirements.txt
       8 sassy/__init__.py
      14 sassy/cortex/__init__.py
      21 sassy/cortex/app.py
      19 sassy/cortex/config.py
       0 sassy/cortex/env.sh
       0 sassy/cortex/models/__init__.py
       0 sassy/cortex/models/admin/__init__.py
       0 sassy/cortex/models/databases/__init__.py
       0 sassy/cortex/models/resources/__init__.py
       0 sassy/cortex/models/users/__init__.py
       0 sassy/cortex/models/websites/__init__.py
       0 sassy/cortex/views/__init__.py
      15 sassy/cortex/views/admin/__init__.py
      15 sassy/cortex/views/admin/admin_base.yml
      14 sassy/cortex/views/admin/users.py
      57 sassy/cortex/views/base.py
      13 sassy/cortex/views/databases/__init__.py
       6 sassy/cortex/views/databases/mysql.py
      19 sassy/cortex/views/resources/__init__.py
       9 sassy/cortex/views/resources/containers.py
       9 sassy/cortex/views/resources/hosts.py
       9 sassy/cortex/views/resources/providers.py
       9 sassy/cortex/views/resources/virtualmachines.py
      13 sassy/cortex/views/users/__init__.py
       9 sassy/cortex/views/users/manage_users.py
      13 sassy/cortex/views/websites/__init__.py
       9 sassy/cortex/views/websites/website.py
       5 sassy/neuron/__init__.py
       2 sassy/nurv/__init__.py
       0 sassy/utils/__init__.py
     143 sassy/utils/communication/__init__.py
       8 sassy/utils/communication/sender.py
       0 sassy/utils/database/__init__.py
      26 sassy/utils/database/db.py
      60 sassy/utils/database/sqlite/__init__.py
     283 sassy/utils/database/sqlite/queries.py
      15 sassy/utils/errors/__init__.py
       6 sassy/utils/errors/communications.py
       7 sassy/utils/errors/database.py
      21 sassy/utils/logger.py
      50 sassy/utils/tools.py
      46 setup.py
       0 tests/__init__.py
      28 tests/test_base.py
     130 tests/test_routes.py
       6 tox.ini
    1408 total
```