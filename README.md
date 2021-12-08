# Flask Resume Builder
![Screenshot 2021-12-07 at 19-02-35 Flask Resume Builder-min](https://user-images.githubusercontent.com/71011395/145061360-6f62877e-b849-434a-a3c2-0bf7be21552b.png)

This is a really simple program but at the same time complete and usable. The user can register and enter the information needed to complete the resume after logging in to the account. At each step, after making any changes, the resume file changes and is visible. Finally, the user can download the PDF version of the resume.
- output resume file: [sajad_resume.pdf](https://github.com/zareisajad/resume-builder-flask/files/7670058/sajad_resume.pdf)
- click [here](#app-preview) to watch app preview.

## Used In This App:
- python3.8
- flask frameword
- Bootstrap5
- SQLite database
- [Flask-WeasyPrint](https://pythonhosted.org/Flask-WeasyPrint/) >> to render pdf file

## How To Run it:
- install ```python3```, ```pip3```, ```python3-venv``` in your machine.
- clone or download the project
- cd to the app directory then create a virtualenv named ```venv``` using ```python3 -m venv venv```
- connect to virtualenv using ```source venv/bin/activate``` (it's different on windows os).
- then install packages using ```pip install -r requirements.txt```
- next run this command: ```flask db upgrade```
- now you can run the sever using: ```flask run```
- finally enter this url in your browser: http://127.0.0.1:5000

## App preview:
![Peek 2021-12-07 19-46](https://user-images.githubusercontent.com/71011395/145066672-4e698efd-1725-4700-88d2-0e4eb4ea7f5a.gif)
