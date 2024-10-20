import reflex as rx
from typing import Union
from sqlmodel import select, asc, desc, or_, func, cast, String
from datetime import datetime, timedelta


# class User(rx.Base):
#     job_description: str
#     resume: str
#     company: str

class State(rx.State):
    """The app state."""
    job_description: str
    resume: str
    company: str

    def update__info(self, new_jd: str, new_resume: str, new_company: str):
        self.job_description = new_jd
        self.resume = new_resume
        self.company = new_company

