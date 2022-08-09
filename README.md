# ParamChanger

ParamChanger is a tool allowing you to replace the parameters of a list of urls by a payload entered as an argument.

## Install:
```bash
$ git clone https://github.com/mathis2001/ParamChanger.git
```
## Usage:
```bash
$ cat urls.txt | python3 ParamChanger.py <payload>

or with other tools

$ python3 webhackurls.py -d target.com | python3 ParamChanger.py <payload> > urls.txt | eyewitness -f urls.txt --web

$ python3 webhackurls.py -d target.com | python3 ParamFirstChecker.py | python3 ParamChanger.py <payload>

and their is a lot of other combination possibilities.
```
## Screens:

![tempsnip](https://user-images.githubusercontent.com/40497633/183686034-c5833b20-a88e-435b-831a-62152dfa9abf.png)
