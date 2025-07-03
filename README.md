# Katex-Editor

![Screenshot 2025-05-29 202546](https://github.com/user-attachments/assets/17918bd0-1ea5-42ff-8301-ca625a457a57)

A web-based mathematical equation editor built with Django that supports real-time rendering of LaTeX equations using KaTeX.

## Features

 - Real-time equation rendering: See your LaTeX equations formatted as you type
 - Template insertion: Quick-insert templates for fractions, derivatives, integrals, and logarithms
 - Mixed content support: Combine regular text with mathematical equations
 - Save functionality: Store your equations and text for later use
 - Responsive design: Works on both desktop and mobile devices

## Prerequisites

- Python 3.6+
- Django 3.0+
- pip

## Installation
 Clone the repository:
 ```console
 git clone https://github.com/ridika-2004/Katex-Editor.git
 cd katex-editor
 ```
 Create and activate a virtual environment:
 ```console
 python -m venv venv
 source venv/bin/activate  # On Windows: venv\Scripts\activate
 ```
 Install dependencies:
 ```console
 pip install django
 ```
 Set up the database:
 ```console
 python manage.py migrate
 ```
 Run the development server:
 ```console
 python manage.py runserver
 ```
 Open your browser to:
 ```console
 http://127.0.0.1:8000/
 ```

## File Structure
 ```console
 katex-editor/
├── katex_project/          # Django project files
│   ├── settings.py         # Project settings
│   ├── urls.py             # URL routing
│   └── ...
├── editor/                 # Editor app
│   ├── migrations/         # Database migrations
│   ├── templates/          # HTML templates
│   ├── admin.py            # Admin configuration
│   ├── models.py           # Database models
│   ├── views.py            # View functions
│   └── ...
├── manage.py               # Django management script
└── README.md               # This file
 ```

## Customization

 - Equation templates: Edit the template strings in editor.html
 - Editor size: Adjust the height values in the CSS
 - Color scheme: Modify the color values in the style section
 - Additional KaTeX features: Add more KaTeX extensions as needed


## Acknowledgments

 - KaTeX for fast LaTeX rendering
 - Django for the web framework
 - All contributors and users






 
