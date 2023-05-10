### titanic-ml-from-disaster

### Software and tools requirements

1. [GitHub account](https://github.com)
2. [VS code IDE](https://code.visualstudio.com)
3. [Heroku Account](https://heroku.com)
4. [GIT CLI](https://git-scm.com/downloads)

### Create new environment for this project
### using Python 3.11.3 for this project

1.  ```
    python -m venv env
    ```
2. ### Activate environment
    ```
    .\env\Scripts\activate
    ```
3. ### Install require packages
    ```
    pip install -r requirements.txt
    ```
### Config git account so that we can push work to repository
1. git config --global user.name "Sandip Deb"
2. git config --global user.email "debsandip.agt"

### Creat app.py file for Flusk configuration
### create another file called home.html file inside templates folder to rander that particular file
### [getBootStrep](https://getbootstrap.com/docs/5.3/getting-started/introduction/) and copy templete file in home.html

### Work with app.py file to create html home page and & predict_api using Flask
### Working with postman API 
1. [Download postman to use postman api ](https://www.postman.com/downloads/)
2.  Run app.py file and then open url in postman and provide relevent features as json format and then tested result and getting no error. 

### Create predict route to run the model in local server
1. After running successfully model in local server proced for next.

### Now we have to deploy the model IN cloud like AWS:
1. Create account in AWS and then Create EC2 instence and add required OS and security group.
2. Create Passkey and kept it safe for communication
3. Download WinSCP to upload model in our server.
4. Download Putty to communicate with server.
5. Check if python is installed on server and then install requirements.txt file
6. After testing the application and if it is working we have stopped and terminate the instences.
7. End
