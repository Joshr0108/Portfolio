# Project Portfolio Website

### Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technology Used](#technology-used)
4. [Development Process](#development-process)
    - [Planning & Design](#planning--design)
    - [Installing](#installing)
    - [Deployment](#deployment)

## Project Overview
This is a portfolio website built to showcase projects, skills and experience. I used Django as the backend framework as python is my primary coding language and used this as an opportunity to increase my width of knowledge on its use and application

## Features 
- Editable data table to display skills and CPD
- Downloadable CV and links to GitHub/LinkedIn
- Minimalist Design
- Responsive layout for desktop and mobile
- Project showcase w/ details & image

## Technology Used
- Django: Backend Framework
- HTML/CSS: For structuring and styling 
- Bootstrap: frontend Framework
- Git/GitHub: Code versioning, management and deployment

# Development Process

## Planning & Design
I Designed the page to meet my needs, It would centre around a projects page but would first greet the viewer with a welcome page, summarising key skills and CPD. The look would be minimalist and limited on bloat, the  dark theme and monospaced font suited that. 
I had Python as my backend to lower development time and leverage existing knowledge of the language. With minimal pre-existing knowledge of frontend language I used bootstrap as a framework. 
I built the Apps and associated models, the apps were `pages` and `projects` each representing the homepage and projects page respectively. Within those I needed models to store the data for skills, CPD, CV and projects. 
I created a base template and statics folder for components that would be used throughout the website such as the footer and header to which each page could then add to. In my base `.css` file I create a frame that would set the colours and fonts so that they could be inherited to any additional apps.
With each addition there was bugging and testing to confirm features were functional and aesthetic.

## Installing
*To set up locally*

1. Clone repo.
```Bash
git clone https://github.com/JoshR/Portfolio.git
```
2. Create virtual environment 
```Bash
python -m venv venv
source venv/bin/activate #Windows: venv/Scripts/activate
```
3. Install dependencies
```bash
pip install -r requirement.txt
```
4. Set DEBUG and ALLOWED_HOSTS
```python
DEBUG = True
ALLOWED_HOSTS = [ ]
```
5. Run development server
```bash
python manage.py runserver
```

## Deployment
This site is hosted on PythonAnywhere.eu . This was chosen as the website will have low traffic and doesn't require significant hardware demand so their offer of free hosting is best.