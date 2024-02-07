import inspect
import instructor
from typing import List, Literal
from openai import OpenAI
from pydantic import BaseModel
from django.conf import settings
from ..google_forms.models import Form, Responses
from ..schemas import FormResponseSchema
from .utils import format_response_as_text


__PROMPT = inspect.cleandoc(
    """
We are from Ground Up Initiative (GUI), a non-profit community here in Singapore
focused on urban sustainability and eco-conciousness.

We just held a volunteering event and would like to review the responses.

The following is a Google Form response. Give your rating on the volunteer satisfaction from
1 (worst) to 5 (best). Also provide your reasoning from the perspective of an organizer.

We will tip you $200 for a good job.
"""
)

mixtral = OpenAI(
    base_url="https://api.together.xyz/v1",
    api_key=settings.TOGETHER_AI_KEY,
)

mixtral = instructor.patch(mixtral, mode=instructor.Mode.TOOLS)


class SatisfactionRating(BaseModel):
    score: Literal[1, 2, 3, 4, 5]
    reason: str


def process_form(md) -> SatisfactionRating:
    return mixtral.chat.completions.create(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        response_model=SatisfactionRating,
        messages=[
            {"role": "system", "content": __PROMPT},
            {"role": "user", "content": md},
        ],
    )


def get_satisfaction_rating(
    form_details: Form, responses: Responses
) -> List[FormResponseSchema]:
    res = []
    md_list = format_response_as_text(form_details, responses)
    for i in range(len(md_list)):
        rsp = responses.responses[i]
        md = md_list[i]
        ai_result = process_form(md)
        res.append(
            FormResponseSchema(
                id=rsp.responseId,
                email=rsp.respondentEmail,
                submit_date=rsp.lastSubmittedTime,
                content=md,
                satisfaction=ai_result.score,
                reason=ai_result.reason,
            )
        )
    return res
