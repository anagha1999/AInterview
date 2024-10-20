import reflex as rx
from typing import Union
from sqlmodel import select, asc, desc, or_, func, cast, String
from datetime import datetime, timedelta


# class User(rx.Base):
#     job_description: str
#     resume: str
#     company: str

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
    
class State(rx.State):
    """The app state."""
    job_description: str
    resume: str
    company: str
    
    structure: Score = Score()
    relevance: Score = Score()
    volume: Score = Score()
    clarity: Score = Score()
    summary = "You demonstrated strong product management fundamentals, especially in prioritizing features and aligning product goals with business objectives. Your communication about working with cross-functional teams was clear, and you gave solid examples of driving feature development from concept to launch. However, your answers regarding handling unexpected product failures could have been more detailed, and expanding on how you measure product success beyond basic metrics would strengthen your responses."
    recommendation= "You could enhance your approach by discussing risk management and how you handle post-launch issues in more depth. Providing more detailed examples of how you adapt strategy based on stakeholder feedback would also be beneficial. Additionally, sharing insights into customer feedback loops and iterative development processes would showcase a more user-centered product approach."
    next_step = "You show great potential, but a follow-up interview focused on your experience with data-driven decision-making and product iterations based on user feedback would provide further insight. It might also be helpful to complete a product scenario exercise to assess your problem-solving and prioritization skills in a more practical setting before moving forward."       

    def update__info(self, new_jd: str, new_resume: str, new_company: str):
        self.job_description = new_jd
        self.resume = new_resume
        self.company = new_company
    
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
        self.structure.set_value("6")
        self.relevance.set_value("3"),
        self.volume.set_value("8"),
        self.clarity.set_value("5")


