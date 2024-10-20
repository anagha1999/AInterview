import reflex as rx
from reflex.components.radix.themes.base import (
    LiteralAccentColor,
)

from ..backend.backend import State


def _arrow_badge(arrow_icon: str, percentage_change: float, arrow_color: str):
    return rx.badge(
        rx.icon(
            tag=arrow_icon,
            color=rx.color(arrow_color, 9),
        ),
        rx.text(
            f"{percentage_change}%",
            size="2",
            color=rx.color(arrow_color, 9),
            weight="medium",
        ),
        color_scheme=arrow_color,
        radius="large",
        align_items="center",
    )


def stats_card(
    stat_name: str,
    value: int,
    prev_value: int,
    percentage_change: float,
    icon: str,
    icon_color: LiteralAccentColor,
    extra_char: str = "",
) -> rx.Component:
    return rx.card(
        rx.hstack(
            rx.vstack(
                rx.hstack(
                    rx.hstack(
                        rx.icon(
                            tag=icon,
                            size=22,
                            color=rx.color(icon_color, 11),
                        ),
                        rx.text(
                            stat_name,
                            size="4",
                            weight="medium",
                            color=rx.color("gray", 11),
                        ),
                        spacing="2",
                        align="center",
                    ),
                    rx.cond(
                        value > prev_value,
                        _arrow_badge("trending-up", percentage_change, "grass"),
                        _arrow_badge("trending-down", percentage_change, "tomato"),
                    ),
                    justify="between",
                    width="100%",
                ),
                rx.hstack(
                    rx.heading(
                        f"{extra_char}{value:,}",
                        size="7",
                        weight="bold",
                    ),
                    rx.text(
                        f"from {extra_char}{prev_value:,}",
                        size="3",
                        color=rx.color("gray", 10),
                    ),
                    spacing="2",
                    align_items="end",
                ),
                align_items="start",
                justify="between",
                width="100%",
            ),
            align_items="start",
            width="100%",
            justify="between",
        ),
        size="3",
        width="100%",
        max_width="22rem",
    )


def stats_cards_group() -> rx.Component:
    return rx.flex(
        rx.card(
            rx.vstack( 
                rx.hstack(
                    rx.icon(
                        tag="briefcase",
                        size=22,
                        color=rx.color("blue", 11),
                    ),
                    rx.text(
                        "Job Description",
                        size="4",
                        weight="medium",
                        color=rx.color("gray", 11),      
                    ),
                    spacing="2",
                    # align="center",
                    # width="100%"
                ),              
                rx.text_area(
                    placeholder="Paste the job description here",
                    color_scheme ="teal",
                    resize="vertical",
                    line="50",
                    width="100%",
                    height="80%",
                    # on_blur=TextAreaBlur.set_text,
                ),
                rx.hstack(
                    rx.icon(
                        tag="building-2",
                        size=22,
                        color=rx.color("blue", 11),
                    ),
                    rx.text(
                        "Company",
                        size="3",
                        color=rx.color("gray", 11),      
                    ),
                    rx.input(
                        placeholder="Optional ...",
                    ),
                    spacing="3",
                    width="100%",
                ),
                size="10",
                width="100%",
            ),
            # size="20",
             
            width="100%",
            # max_height = "100rem",
            max_width = "40rem",
        ),
        rx.card(
            rx.vstack(
                rx.hstack(
                    rx.icon(
                        tag="book-user",
                        size=22,
                        color=rx.color("blue", 11),
                    ),
                    rx.text(
                        "Resume",
                        size="4",
                        weight="medium",
                        color=rx.color("gray", 11),     

                    ),
                    spacing="2",
                    # align="center",
                ),
                rx.text_area(
                    placeholder="Paste the your resume here",
                    color_scheme = "teal",
                    resize="vertical",
                    size="10",
                    width="100%"
                    # on_blur=TextAreaBlur.set_text,
                ),
            ),
            size="20",
            width="100%",
            max_width="40rem",
        ),        
        spacing="6",
        width="100%",
        justify="center",
        wrap="wrap",
        # display=["none", "none", "flex"],
    )
