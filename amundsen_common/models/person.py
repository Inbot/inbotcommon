from typing import Optional

import attr
from marshmallow_annotations.ext.attrs import AttrsSchema


@attr.s(auto_attribs=True, kw_only=True)
class PersonSummary:
    name: str = attr.ib()
    profile_link: str = attr.ib()
    headline: Optional[str] = None
    company: Optional[str] = None
    company_url: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None

class PersonSummarySchema(AttrsSchema):
    class Meta:
        target = PersonSummary
        register_as_scheme = True
