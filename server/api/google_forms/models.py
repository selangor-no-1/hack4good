from typing import Any, Dict, List, Literal, Optional, Self
from ninja import Schema


class FormItem(Schema):
    itemId: str
    question_id: str
    question: str
    question_type: Literal["textQuestion", "choiceQuestion"]
    options: List[str]


class Form(Schema):
    formId: str
    url: str
    description: str
    title: str
    items: List[FormItem]

    @classmethod
    def parse(cls, json: Dict[str, Any]) -> Self:
        form_dict = {
            "formId": json["formId"],
            "url": json["responderUri"],
            "description": json["info"]["description"],
            "title": json["info"]["title"],
            "items": [],
        }

        for item in json["items"]:
            itemId = item["itemId"]
            question_id = item["questionItem"]["question"]["questionId"]
            question = item["title"]
            question_type = (
                "textQuestion"
                if "textQuestion" in set(item["questionItem"]["question"].keys())
                else "choiceQuestion"
            )
            options = []
            if question_type == "choiceQuestion":
                opts = item["questionItem"]["question"]["choiceQuestion"]["options"]
                for opt in opts:
                    for k, v in opt.items():
                        if k == "value":
                            options.append(v)
            form_dict["items"].append(
                FormItem(
                    itemId=itemId,
                    question_id=question_id,
                    question=question,
                    question_type=question_type,
                    options=options,
                )
            )

        return cls(**form_dict)


class ResponseItem(Schema):
    responseId: str
    respondentEmail: Optional[str]
    createTime: str
    answers: Dict[str, str | List[str]]


class Responses(Schema):
    responses: List[ResponseItem]

    @classmethod
    def parse(cls, json: Dict[str, Any]) -> Self:
        _responses = []
        responses = json["responses"]

        for resp in responses:
            responseId = resp["responseId"]
            createTime = resp["createTime"]
            respondentEmail = resp.get("respondentEmail", "")

            answers = resp["answers"]
            answers_processed = {}
            for key in answers:
                vals = answers[key]["textAnswers"]["answers"]
                if len(vals) == 1:
                    answers_processed[key] = vals[0]["value"]
                else:
                    answers_processed[key] = [v["value"] for v in vals]
            _responses.append(
                ResponseItem(
                    responseId=responseId,
                    respondentEmail=respondentEmail,
                    createTime=createTime,
                    answers=answers_processed,
                )
            )
        return cls(responses=_responses)
