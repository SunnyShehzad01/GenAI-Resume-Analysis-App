# Project Synopsis
Here you can check your resume with the job description and get the score and insights such as:
* ATS Score of the resume
* Probability of getting hired
* Keyword analysis
* SWOT Analysis
* Suggestions for overall improvement

## Steps for creating the project
1. Create the virtual environment - ``python -m venv .venv``
2. Activate the virtual environment - ``source .venv/bin/activate``
3. Create the .env file to store the api key.
4. Create the requirements.txt file and add the libraries for installation - ``pip install -r requirements.txt``

## Architecture
1. app.py: Frontend creation and output of the GenAI Model.
2. It will have the feature of capturing information such as Resume and JD.
3. Information we are capturing is ``Resume.pdf`` and ``job desc``.
4. pdf.py that will process the information in pdf and thats why we have installed ``pypdf``
5. analysis.py that will triangulate the pdf information and the JD and will provide insights.