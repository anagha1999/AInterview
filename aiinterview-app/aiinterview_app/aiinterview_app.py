import reflex as rx
from .components.stats_cards import stats_cards_group
from .views.navbar import navbar
from .views.table import main_table


def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        stats_cards_group(),
        rx.center(
            rx.button(
                rx.text("Confirm", size="4", display=["none", "none", "block"]),
                size="3",
                on_click=rx.redirect("/interview")
            ),
            width="100%",
        ),
        width="100%",
        spacing="6",
        justify = "center",
        padding_x=["1.5em", "1.5em", "3em"],
    )

def interview():
    return rx.text("TODO: access UserMedia, stream video")

app = rx.App(
    theme=rx.theme(
        appearance="light", has_background=True, radius="large", accent_color="grass"
    ),
)

app.add_page(
    index,
    title="AI Interview Coach ",
    description="A simple app to help you prepare for your interview!",
)

app.add_page(
    interview,
)
