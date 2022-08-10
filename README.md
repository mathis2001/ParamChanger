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

$ python3 webhackurls.py -d target.com | python3 ParamFirstChecker.py --lfi | python3 ParamChanger.py <payload>

and their is a lot of other combination possibilities.
```
## Screens:

![tempsnip](https://user-images.githubusercontent.com/40497633/183858251-22284e12-b246-46e3-a828-3a0ea519ef7c.png)
![tempsnip](https://user-images.githubusercontent.com/40497633/183859763-543abda7-9733-41af-9c70-62a50f216334.png)
![tempsnip](https://user-images.githubusercontent.com/40497633/183859689-02e99609-9a8f-426e-bdab-5bd91df128b7.png)
![tempsnip](https://user-images.githubusercontent.com/40497633/183860271-e7737c96-cab6-40ea-8c77-08c6774fe0c0.png)

