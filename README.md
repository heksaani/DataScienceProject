# HealthNotebook

This is a joint project created by [Heidi](https://github.com/heksaani), [Lotta](https://github.com/LottaPol) and [Tatu](https://github.com/tlinnala) for the course [Introduction to Data Science](https://studies.helsinki.fi/kurssit/opintojakso/hy-CU-118209216-2021-08-01) at the University of Helsinki.

## Project description
Our task was to come up with an inspiring idea to get familiar with different aspects of data science. We decided to create HealthNotebook, which analyses data given by the user and recommends ways to improve sleep. We decided to create an interactive Jupyter notebook since the time was limited. This could be further developed into a web and/or mobile application.

## Data
Used datasets:
<br>
- [Boston College COVID-19 Sleep and Well-Being Dataset](https://osf.io/gpxwa/?view_only=) <br>
- [FSD2326 University Student Health Survey 2004](https://urn.fi/urn:nbn:fi:fsd:T-FSD2326) <br>


## Instructions
1. Clone this repository to your computer
```bash
git clone https://github.com/heksaani/DataScienceProject.git
cd DataScienceProject
```
2. If you wish, you can install the required packages using the requirements.txt file
```bash
pip install -r requirements.txt
```
3. Launch the Jupyter notebook and open this project in your browser.
```bash
jupyter notebook
```
When using the notebook you can run the cells by pressing the play button or by pressing shift + enter. We recommend that you run the cells one by one and fill in the questions. Also, remember to push the button 'Submit' after filling in the question boxes. <br>
<br>
NOTE: if you are having trouble loading the regression models with Pickle, try running the following files to recreate the models: `analysis/linear_regression_covid19_dataset.ipynb` and `analysis/linear_regression_uhs_dataset.ipynb`.
