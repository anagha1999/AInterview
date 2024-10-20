import reflex as rx
from .components.stats_cards import stats_cards_group
from .components.videocam import webcam_upload_component
from .views.navbar import navbar
from .backend.backend import State

def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        stats_cards_group(),
        rx.center(
            # rx.button(
            #     rx.text("  Save  ", size="4", display=["none", "none", "block"]),
            #     size="3",
            #     on_click=State.update__info()
            # ),
            rx.button(
                rx.text("Start Interview", size="4", display=["none", "none", "block"]),
                size="3",
                on_click=rx.redirect("/interview")
            ),
            spacing="6",
            width="100%",
        ),
        width="100%",
        spacing="6",
        justify = "center",
        padding_x=["1.5em", "1.5em", "3em"],
    )

def interview() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.badge(
                rx.icon(tag="message-circle-question", size=28),
                rx.heading("Interview Room", size="6"),
                color_scheme="green",
                radius="large",
                align="center",
                variant="surface",
                padding="0.65rem",
            ),
            rx.flex(
                rx.card(
                    rx.center(
                    webcam_upload_component("webcam"),
                    width="100%",
                    height="100%",
                    ),
                ),
                rx.box(
                    rx.vstack(
                        rx.card(
                            rx.image(
                            alt="interviewer",
                            src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/38gX1mFs9ZpQNhfoAex3yaUgyzvyfqyPIgFndLtgPevsdPiOB/out-0.webp",
                            height="auto",
                            width="100%",
                            ),
                            background_color="#ffffff",
                            overflow="hidden",
                            border_radius="0.5rem",
                            box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
                        ),
                        spacing="6",
                    ),
                    width="25%",
                ),
                rx.box(
                    rx.button(
                        "Finish",
                        color_scheme="red",
                        size="4",
                        width="300px"
                        ),
                    position="absolute",
                    bottom="2rem",
                    right="5rem",
                ),
                spacing = "5",
                display="flex",
                height="90vh",
                padding_bottom="2em",
            ),
        ),
        padding="2em",
        spacing = "5",
        display="flex",
        max_width="100rem",
        height="100vh",
        width="100%",
        justify="center",
        wrap="wrap",
        )
    # )


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
