from inspect import cleandoc
from typing import List
from ..google_forms.models import Form, Responses


def format_response_as_text(form_details: Form, responses: Responses) -> List[str]:
    res = []
    id2qn = {}
    for item in form_details.items:
        id2qn[item.question_id] = item.question
    for r in responses.responses:
        md = f"# {form_details.title}\n{form_details.description}\n\n\n### Response:\n\n\n "
        for k, v in r.answers.items():
            qn = id2qn[k]
            ans = v
            md += cleandoc(
                f"""
**Question:** {qn}  
**Answer:** {ans}  
  


"""
            )
        res.append(md)
    return res
