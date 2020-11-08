# Docker-Compose-Nginx-ReverseBroxy

--> since i haven't uploaded anything to git since a while .. i found it useful to upload something related to DevOps as a change

## Nginx As Reverse Proxy for flask (development env)

(flask) dir -> contain the flask app<br />
(certs) dir -> contain tls certs for https (self signed)

----

docker-compose.yml -> docker-compose file to build the project from ..<br />
nginx.conf         -> change the nginx configuration<br />
nginx.Dockerfile   -> create nginx-custom image<br />
ubuntu.Dockerfile  -> create ubuntu-custom image<br />

