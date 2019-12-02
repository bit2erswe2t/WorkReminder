> Beginner project, OJ ignore

### Design

Set the time when a work start and end.
Set work time(45m) and break time(5m).
-> 
Start.
-> 
When work time exhaust, pop-up window fill all screen.
->
Back set menu, repeat set.

### Run code

* git clone project
```sh
git clone ProjectAddress
```
* install PyQt5
```sh
#Carefully, pip installation package may have a virus if package name is error.
pip install PyQt5
```
* python3 main.py

### Package exe
```sh
#windows
cd .\release
pyinstaller -F -w ..\main.py
```

### Future

* add over button 
* add work time display lcd
* add to start work display lcd