
# Graduate Admission Prediction Web Application

## Overview

This project is a web-based application designed to predict graduate admissions chances based on user-provided credentials. It utilizes a RandomForest machine learning model (`randomforest.sav`) to make predictions. The application is built using the Django framework, with the frontend designed in HTML.

## Features

- **Graduate Admission Prediction**: Users can input their academic and test scores to receive predictions on their chances of graduate admission.
- **Analysis Notebook**: A comprehensive Jupyter Notebook (`Graduate_Admission.ipynb`) detailing the data analysis, model selection, and training process.
- **Interactive Web Interface**: A user-friendly web interface (`index.html`, `result.html`) for inputting credentials and displaying predictions.

## Live Demo

The application is live and can be accessed [here](https://four-places-design.loca.lt).

## Installation

To run this project locally, follow these steps:

1. **Clone the Repository**

```bash
git clone <repository-url>
cd <repository-directory>
```

2. **Set Up the Environment**

Ensure you have Python installed, and set up a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```


```

3. **Run the Django Application**

```bash
python manage.py runserver
```

Now, the application should be running on `http://127.0.0.1:8000/`.

## Usage

- Navigate to the live demo link or the local server URL.
- Input your GRE score, TOEFL score, university rating, SOP, LOR, CGPA, and research experience.
- Submit the form to receive your admission prediction.

## Files Description

- `Graduate_Admission.ipynb`: Jupyter Notebook detailing model training and analysis.
- `manage.py`: Django's command-line utility for administrative tasks.
- `randomforest.sav`: Serialized RandomForest model used for predictions.
- `index.html` & `result.html`: Frontend HTML templates for the application.
- `settings.py`, `urls.py`, `views.py`: Django configuration and routing files.

