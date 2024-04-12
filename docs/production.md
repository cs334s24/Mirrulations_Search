## Production

Launching our system in production assumes the same setup process as `development.md` provides.

This involves:
* Installing Node and generating the `node_modules` folder within the `frontend` directory
* Ingesting Data into MongoDB using the `mongo_db.py` script

If there are any issues with deployment, see the `development.md` setup step involving the process for troubleshooting.


### To launch the system manually in production:

* Build docker container
```
sudo docker-compose build
```

* Run docker container
```
sudo docker-compose up -d
```

* Bring the conatiner down
```
sudo docker-compose down
```

