## Nepali Friendly Datetime Applet

A simple taskbar applet to show realtime date along with nepali-miti for linux desktops

<img src="presentlook.png"/>

## Installation

1. Under the root folder add a virtual environment `python3 -m venv venv`
2. Activate the venv by using `source venv/bin/activate`
3. Now, install dependencies from requirements.txt `pip3 install -r requirements.txt`
4. Run the main.py `python3 main.py`


### TODOS:

01. [x] Make it self-updating
02. [ ] Build it with meson
03. [ ] Build it with GTK
04. [ ] Add Nepali date specifiers like strftime
05. [ ] Support for custom Nepali date specifiers
06. [x] Make flask app out of this

#### Tested with python 3 and all the latest python versions 3.6, 3.7, 3.8.
