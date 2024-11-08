from google_sheets.services import write_to_sheet
from vacancies.models import Vacancy


def report_vacancies():
    vacancies = Vacancy.objects.all()

    sheets_data = []
    for vacancy in vacancies:
        django_admin_link = "http://localhost:8000/admin/vacancies/vacancy/{}/change/".format(vacancy.id)

        sheets_data.append([
            str(vacancy.id),
            vacancy.name,
            vacancy.type.name,
            django_admin_link,
            vacancy.created_at.strftime("%Y-%m-%d, %H:%M:%S"),
        ])

    write_to_sheet('A2:E', sheets_data, "1XTiyd3I1D1qnW5R85qLWUj8WRlnBYU6iAiEF_Dju1h4")
