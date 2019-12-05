> Beginner project, OJ ignore

### Design

Set the time when a work start and end(9:00 and 11:30).
Set work time(30:00\45, thirty minutes or fouty-five seconds) and break time(3:00\5, three minutes or five seconds).<br>
->Start.<br>
->When work time exhaust, pop-up window fill all screen.<br>
->Back set menu, repeat set.

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
#windows icon need four size icons to combine a icon file. Generate "coffee.ico" with "Greenfish Icon Editor".
#-F: one file -w: no console -i: add icon
pyinstaller -F -w -i ..\coffee.ico ..\main.py
```

### Future

* add over button 
