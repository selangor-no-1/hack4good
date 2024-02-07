from pathlib import Path
from typing import List
from google.oauth2 import service_account
from googleapiclient.discovery import build
from concurrent.futures import ThreadPoolExecutor

from .models import Form, Responses
from ..ai import get_satisfaction_rating
from ..schemas import FormResponseSchema


class GoogleFormConnector:
    def __init__(self, path_to_creds: Path):
        self.credentials = service_account.Credentials.from_service_account_file(
            str(path_to_creds)
        )
        self.scopes = [
            "https://www.googleapis.com/auth/forms.body.readonly",
            "https://www.googleapis.com/auth/forms.responses.readonly",
        ]
        self.discovery_doc = "https://forms.googleapis.com/$discovery/rest?version=v1"

    @property
    def service(self):
        return build(
            serviceName="forms",
            version="v1",
            credentials=self.credentials,
            discoveryServiceUrl=self.discovery_doc,
            static_discovery=False,
        )

    @property
    def forms(self):
        return self.service.forms()

    @property
    def responses(self):
        return self.forms.responses()

    def fetch_form_details(self, id: str) -> Form:
        return Form.parse(self.forms.get(formId=id).execute())

    def fetch_form_responses(self, id: str) -> Responses:
        return Responses.parse(self.responses.list(formId=id, pageToken=None).execute())

    def process_responses(self, id: str) -> List[FormResponseSchema]:
        def async_fetch():
            with ThreadPoolExecutor() as exc:
                _form = exc.submit(self.fetch_form_details, id)
                _resps = exc.submit(self.fetch_form_responses, id)
                return _form.result(), _resps.result()

        form, resps = async_fetch()
        return get_satisfaction_rating(form_details=form, responses=resps)
