import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]

# Load credentials from environment variables
client_email = os.getenv("GOOGLE_CLIENT_EMAIL")
private_key = os.getenv("GOOGLE_PRIVATE_KEY").replace('\\n', '\n')  # replace \n with newline

credentials = ServiceAccountCredentials.from_json_keyfile_dict(
    {
        "type": "service_account",
        "project_id": "your_project_id",
        "private_key_id": "your_private_key_id",
        "private_key": private_key,
        "client_email": client_email,
        "client_id": "your_client_id",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": f"https://www.googleapis.com/robot/v1/metadata/x509/{client_email}"
    },
    scope
)

SPREADSHEET_ID = '1S6npDwV9TYoRb7yamHBbrm-Uz0j0ttN_s06gCXS9ItE'


def get_google_sheets_client():
    return gspread.authorize(credentials)


def read_from_sheet(sheet_id):
    client = get_google_sheets_client()
    spreadsheet = client.open_by_key(sheet_id)
    sheet = spreadsheet.sheet1
    return sheet.get("A1:B3")


def write_to_sheet(range, data, spreadsheet_id=SPREADSHEET_ID):
    client = get_google_sheets_client()
    spreadsheet = client.open_by_key(spreadsheet_id)

    return spreadsheet.values_update(
        range,
        params={'valueInputOption': 'RAW'},
        body={'values': data},
    )


def bulk_write_to_sheet(sheet_id, data):
    client = get_google_sheets_client()
    spreadsheet = client.open_by_key(sheet_id)
    sheet = spreadsheet.sheet1  # or you can specify the sheet you want to write to

    # Write to multiple ranges
    request_data = []

    for range_name, values in data.items():
        request_data.append({
            'range': range_name,
            'majorDimension': 'ROWS',  # or 'COLUMNS' if you prefer
            'values': values
        })

    return sheet.batch_update(request_data)
