from course_project.celery import app
from vacancies.reporter import report_vacancies


@app.task(bind=True)
def report_vacancies_on_google_sheets(self):
    report_vacancies()
