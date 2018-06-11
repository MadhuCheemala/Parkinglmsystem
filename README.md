**Parking Lot Management System SERVICE Implementation**

**Pre-requisites**

> The following software versions should be installed in your system:

* Anaconda python 3.5/python 2.7.13
* pip install flask_cors
* pip install cherrypy==13.0.0 paste


**Project Setup**

* Check out the project from BitBucket [Projectlotmg]

**Project Structure**

* **Projectlotmg**  **:Project name**
  * tdirdlotmg : Package Name (Package contains subpackages with several Python source files.)
  * bin  : List of conf files ,shell script and driver class
  * README.md : To explain and install your software configurations
  * Setup.cfg : Test functionality properties
  * Setup.py : Python packge creation(wheel/egg/zip)


**Python package build command**
 * **>>python setup.py bdist_wheel**


**Deployment requirement files**

> The following below listed files need to be copied from bin location of the project structure to the requred environment

   * plot_driver.py.py (driver class)


**Parking Lot Management System SERVICE details**

  **1.RESTAPI**: http://127.0.0.1:5000/plot/carentry
    **Requestjson**:{
    "carid":5}
     **Responsejson**:{
    "CarParrking_avialable_slot": 2,
    "car_slotid": "ac"}

  **2.RESTAPI**: http://127.0.0.1:5000/plot/carexit
    **Requestjson**:{"car_slotid":"ad"}
     **Responsejson**:{
    "CarParrking_avialable_slot": 4,
    "Remove_car_slotid": "ad"
}



