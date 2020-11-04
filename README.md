# carstore3000

This application/api aims to connect a car stock to a client.

This application uses the folowing technologies:
* docker
* docker-compose
* python 3.9
* python Flask
* postgres

# Startup

Start a postgres database with the `dockerfiles/db/conf.env` configurations

```bash
./run.sh
```

# Functional Tests

```bash
./test.connect_api*.sh
```

# TODO

* Properly setup basic auth
* Add relationship between tables. A user should pick a car and buy it.
  It implies activating a status on each cars (available/locked).
  If a user is in transaction mode, other users should not see the car while
  it is not released or in the best case purchased.
* method `get` to list users should/must be only available for admin
* In case of multiple cars stores are handle the dataset should be reworked.
  There is no need to create a `CarsStore` model.
