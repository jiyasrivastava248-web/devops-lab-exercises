\# Exercise 9: Jenkins Multi-Stage Pipeline



\## Objective

To create and run a Jenkins declarative pipeline for a Python Flask application using multiple stages.



\## Application Files

\- `app.py` — Flask web application that displays a greeting.

\- `requirements.txt` — specifies the Flask dependency.

\- `test\_app.py` — tests the application's home route and response.

\- `Jenkinsfile` — defines the Jenkins pipeline stages.



\## Pipeline Stages

1\. \*\*Build:\*\* Install the Python dependencies.

2\. \*\*Test:\*\* Run the unit tests.

3\. \*\*Deploy:\*\* Copy the application into the deployment directory.

4\. \*\*Run Application:\*\* Start the Flask application.

5\. \*\*Test Application:\*\* Test the application response.



\## Expected Application Response

`Hello, Jenkins Multi-Stage Pipeline!`



\## Verification

The Jenkins pipeline should complete all five stages successfully. The unit test should verify that the home route returns HTTP status code 200 and the expected greeting.



\## Evidence

Screenshots of the Jenkins job, console output, job configuration, and GitHub repository are provided as evidence of the exercise.



\## Conclusion

This exercise demonstrates how to define a multi-stage Jenkins pipeline to build, test, deploy, and run a Python Flask application.



