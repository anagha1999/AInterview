import reflex as rx
from typing import Union
from sqlmodel import select, asc, desc, or_, func, cast, String
from datetime import datetime, timedelta


# class User(rx.Base):
#     job_description: str
#     resume: str
#     company: str
#     name: str

class Score(rx.Base):
    value = 1
    box_color = "red"

    def set_value(self, new_value: str):
        self.value = int(new_value)
        self.update_color()

    def update_color(self):
        if self.value < 4:
            self.box_color = "red"
        elif self.value < 8:
            self.box_color = "orange"
        else:
            self.box_color = "green"
    
class OutputState(rx.State):
    structure: Score = Score()
    relevance: Score = Score()
    volume: Score = Score()
    clarity: Score = Score()
    summary = " Schedule a follow-up session to address the identified areas for improvement. If significant progress is made, proceed with the next round of interviews.",
    recommendation= " Schedule a follow-up session to address the identified areas for improvement. If significant progress is made, proceed with the next round of interviews.",
    next_step = " Schedule a follow-up session to address the identified areas for improvement. If significant progress is made, proceed with the next round of interviews.",
                   

    def update__info(self, new_jd: str, new_resume: str, new_company: str, new_name: str):
        self.job_description = new_jd
        self.resume = new_resume
        self.company = new_company
        self.name = new_name
    
    def update_score(self, structure :str, relevance :str, volume: str, clarity: str):
        self.structure.set_value(structure)
        self.relevance.set_value(relevance),
        self.volume.set_value(volume),
        self.clarity.set_value(clarity)
    
    def update_report(self, summary: str, recommendation :str, next_step: str):
        self.summary = summary
        self.recommendation = recommendation
        self.next_step = next_step

    def test_increament(self):
        self.structure.set_value("1")
        self.relevance.set_value("4"),
        self.volume.set_value("7"),
        self.clarity.set_value("9")


