# djpass : django-password-generator

A simple password generator django app clubbed with Bootstrap 4, this project is just a django implemanation of one of my python script within my repository PythonXample  [PythonXample/PyPassGen.py](https://github.com/Jackuna/PythonXample/blob/master/PyPassGen.py). 

This project has been designed to meet the daily system admin requirement to generate strong and random passwords.


It has cool features like

* Cool and resposive UI

* Supports exclusions within random passwords too.

* Supports Multidigit password generation.

* Refresh dialog to regenerate same desired password length.

* Copy Content to avoid noisy data within password.

### Snapshots 

![djpass Home](https://github.com/Jackuna/djpass/blob/master/djPassDemo.gif)


### Installaton & Configuration

As a docker container.

* Download djpass docker imager
   ```docker pull jackuna/djpass
   ```
  Once the image has been downloded, find the image and initiate a container using it's corrosponding image ID.
  Find Image Id from the below docker command
   ``
   docker images 
   ``
   
   Now run the container.
   
   ```
    docker run -td --name djpass -p 9090:9090 < IMAGE ID >
   ```
   Login into the container and initiate our djpass django app
   
   ```
   cd /usr/local/djpass/
   
   python3 manage.py runserver 0.0.0.0:9090
   ```
   
   
   
