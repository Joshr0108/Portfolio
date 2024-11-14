# Project Portfolio Website

### Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technology Used](#technology-used)
4. [Development Process](#development-process)
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