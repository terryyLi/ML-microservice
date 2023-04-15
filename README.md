# Career Recruiter ML Model Framework

## Overview
This repo contains an ML model for predicting whether a student applicant would be a good employee, along with some basic starter code for how to interact with the model.

This model should eventually be connected with the career page within NodeBB to allow recruiters to view a prediction of a student applicant's likeliness to be a good employee to hire.

## Setup
1. (Optional) Set up a [virtual environment](https://docs.python.org/3/library/venv.html) for Python
2. Run `pip install -r requirements.txt` to install all dependencies

## Running the Model
The file `predict.py` contains a function `predict` which, given a student application input, returns a prediction whether the student would be a good employee. 

Below is a sample run from the terminal:
```
% python3
>>> from predict import predict
>>> student = {
        "student_id": "student1",
        "major": "Computer Science",
        "age": "20",
        "gender": "M",
        "gpa": "4.0",
        "extra_curricular": "Men's Basketball",
        "num_programming_languages": "1",
        "num_past_internships": "2"
    }
>>> predict(student)
{'good_employee': 1}
```
Can also try on: https://ml-micro.fly.dev/docs
