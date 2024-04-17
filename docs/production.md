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

### Setup Certbot Certificates in Production

[Click Here For Official Documentation](https://certbot.eff.org/instructions?ws=other&os=pip)

* Make sure the server is not running

* Install Certbot
```
sudo python3 -m venv /opt/certbot/
sudo /opt/certbot/bin/pip install --upgrade pip
sudo /opt/certbot/bin/pip install certbot certbot
sudo ln -s /opt/certbot/bin/certbot /usr/bin/certbot
```

* Run Certbot to generate certificates
```
sudo certbot certonly --standalone
```

* Setup .env file with variables for NGINX

The files are stored in etc/letsencrypt </br>
Setup the CERT and KEY variable similiar to development </br>
The CERT variable is for fullchain.pem </br>
The KEY variable is for privkey.pem </br>

Look in the .env file in a production or test instance
in the root directory of the project for more detail.

### Give docker-compose executable permissions

* Run this command in the production instance
```
sudo chmod +x /usr/local/bin/docker-compose
```