# GTbooru

GTbooru is a fork of the Boorunaut project. Please refer to the parent Git repository [GT](https://github.com/uaevuon/GT) for more information.

## Features

* Posts;
* Gallery system;
* Tagging system, with aliases and implications;
* Control panel, including mass renaming, hash banning, mod queue and more.
* Predicting tag, uploading pixiv image with url.

## Installation

```bash
pip install . -r requirements.txt
boorunaut startproject mysite
cd mysite
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Now your website should be running on the default `localhost:8000`.
