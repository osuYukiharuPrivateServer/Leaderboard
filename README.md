# Leaderboard (V2) - Yukiharu osu！


This is the Leaderboard of the osu! Yukiharu Private Server
The frount end is in HTML and CSS
The back end is in Python
*This would be the same as the one in hedgehog-qd's repository

# What's new
In this branch (V2), we add the function that users can switch to see the leaderboard in the 4 main modes (osu!, osu!taiko, osu!mania, osu!catch)
The default mode is osu! (auto-switch by redirect)

# How to run

You need to install the python environment first (Python version >= 3.7)
In order to run it successfully, you need to install these (use pip):
- jinja2
- flask
- requests
- json

In Linux, you can use the following to run:
```md
python3 ./main.py

```
If you want to run it after you closed your shell / the SSH, you can:
```md
 nohup python3 main.py >/dev/null 2>&1 & //You'd better remember the process ID it returns you.

```
To close it, just use the "kill":
```md
kill *  //The * is the process ID it returns you in the last step

```
# !!TIPS:
- Our server is based on the bancho.py project (https://github.com/osuAkatsuki/bancho.py), so it might be useable on other servers based on it.
- This is the first version of our Leaderboard. We may rewrite all the codes there in the later versions.
- You can use the PyCharm to edit it (I used that to build). Just open the folder by that tool.

# Directory Structure
    .
    ├── templetes                 # code related to frount end
    |   └──index.html             # the page
    ├── api_dealing.py            # GET the json file from our api
    ├── json_dealing.py           # analyze the json file got by api_dealing.py
    └── main.py                   # the main back end file
