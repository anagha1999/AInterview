import reflex as rx
from ..backend.backend import OutputState

def create_heading(
    font_size, font_weight, margin_bottom, text
):
    """Create a heading with customizable font size, weight, and margin."""
    return rx.heading(
        text,
        font_weight=font_weight,
        margin_bottom=margin_bottom,
        font_size=font_size,
        line_height="1.75rem",
        as_="h2",
    )


def create_colored_bar(color, width):
    """Create a colored bar with a specified width."""
    return rx.box(
        # class_name="bg-orange-500",
        background_color=color,
        width=width,
        height="1rem",
        border_radius="9999px",
    )


def create_progress_bar(color, progress_width):
    """Create a progress bar with a specified progress width."""
    return rx.box(
        create_colored_bar(color, width=progress_width),
        background_color="#E5E7EB",
        height="1rem",
        border_radius="9999px",
        width="100%",
    )


def create_right_aligned_text(text):
    """Create right-aligned text with a small top margin."""
    return rx.text(
        text, margin_top="0.25rem", text_align="right"
    )


def create_score_section(title, progress_width, score_text, color):
    """Create a score section with a title, progress bar, and score text."""
    return rx.box(
        create_heading(
            font_size="1.125rem",
            font_weight="600",
            margin_bottom="0.5rem",
            text=title,
        ),
        create_progress_bar(color, progress_width=progress_width),
        create_right_aligned_text(text=score_text),
    )


def create_green_bar(width):
    """Create a green bar with a specified width."""
    return rx.box(
        width=width,
        background_color="#10B981",
        height="1rem",
        border_radius="9999px",
    )



def create_strong_text(text):
    """Create strong (bold) text."""
    return rx.text.strong(text)

def create_small_strong_text(text):
    """Create small, strong (bold) text."""
    return rx.text(
        create_strong_text(text=text),
        font_size="0.875rem",
        line_height="1.25rem",
    )


def create_list_item(content):
    """Create a list item with the given content."""
    return rx.el.li(content)


def create_bullet_list(first_item, second_item):
    """Create a bullet list with two items."""
    return rx.list(
        create_list_item(content=first_item),
        create_list_item(content=second_item),
        list_style_type="disc",
        list_style_position="inside",
        margin_left="1rem",
        font_size="0.875rem",
        line_height="1.25rem",
    )


def create_detailed_report():
    """Create a detailed report section with summary, strengths, areas for improvement, recommendations, and next steps."""
    return rx.box(
        rx.text(
            create_strong_text(text="Summary:"),
            OutputState.summary,
            font_size="0.875rem",
            line_height="1.25rem",
        ),
        # create_small_strong_text(text="Strengths:"),
        # create_bullet_list(
        #     first_item="Excellent speech clarity (8/10)",
        #     second_item="Good volume control (7/10)",
        # ),
        # create_small_strong_text(
        #     text="Areas for Improvement:"
        # ),
        # create_bullet_list(
        #     first_item="Interview structure (4/10)",
        #     second_item="Relevance of answers (6/10)",
        # ),
        # create_small_strong_text(text="Recommendations:"),
        rx.text(
            create_strong_text(text="Recommendations:"),
            OutputState.recommendation,
            margin_top="1rem",
            font_size="0.875rem",
            line_height="1.25rem",
        ),
        # rx.list.ordered(
        #     create_list_item(
        #         content="Provide coaching on interview structure and organization"
        #     ),
        #     create_list_item(
        #         content="Practice answering questions more directly and relevantly"
        #     ),
        #     create_list_item(
        #         content="Consider a second interview to reassess improvements"
        #     ),
        #     list_style_type="decimal",
        #     list_style_position="inside",
        #     margin_left="1rem",
        #     font_size="0.875rem",
        #     line_height="1.25rem",
        # ),
        rx.text(
            create_strong_text(text="Next Steps:"),
            OutputState.next_step,
            margin_top="1rem",
            font_size="0.875rem",
            line_height="1.25rem",
        ),
        display="flex",
        flex_direction="column",
        gap="1rem",
    )


def create_interview_scores_layout():
    """Create the main layout for displaying interview scores and detailed report."""
    return rx.flex(
        rx.box(
            create_score_section(
                title="Structure",
                progress_width= f"{(OutputState.structure.value / 10) * 100:.0f}%",
                score_text=f"{OutputState.structure.value}/10",
                color = OutputState.structure.box_color,
            ),
            create_score_section(
                title="Relevance of Answers",
                progress_width= f"{(OutputState.relevance.value / 10) * 100:.0f}%",
                score_text=f"{OutputState.relevance.value}/10",
                color = OutputState.relevance.box_color,
            ),
            create_score_section(
                title="Volume Levels",
                progress_width= f"{(OutputState.volume.value / 10) * 100:.0f}%",
                score_text=f"{OutputState.volume.value}/10",
                color = OutputState.volume.box_color,
            ),
            create_score_section(
                title="Speech Clarity",
                progress_width= f"{(OutputState.clarity.value / 10) * 100:.0f}%",
                score_text=f"{OutputState.clarity.value}/10",
                color = OutputState.clarity.box_color,
            ),
            display="flex",
            flex_direction="column",
            padding_right="2rem",
            gap="1.5rem",
            width="50%",
        ),
        rx.box(
            create_heading(
                font_size="1.25rem",
                font_weight="700",
                margin_bottom="1rem",
                text="Detailed Report",
            ),
            create_detailed_report(),
            border_color="#D1D5DB",
            border_left_width="1px",
            padding_left="2rem",
            width="50%",
        ),
        display="flex",
    )


def create_interview_scores_card():
    """Create a card containing the interview scores and detailed report."""
    return rx.box(
        rx.heading(
            "Interview Scores",
            font_weight="700",
            margin_bottom="1.5rem",
            font_size="1.5rem",
            line_height="2rem",
            text_align="center",
            as_="h1",
        ),
        create_interview_scores_layout(),
        background_color="#ffffff",
        max_width="64rem",
        padding="2rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        width="100%",
    )


def create_interview_scores_page():
    """Create the full page layout for the interview scores, including Tailwind CSS setup."""
    return rx.fragment(
        rx.script(src="https://cdn.tailwindcss.com"),
        rx.box(
            create_interview_scores_card(),
            background_color="#F3F4F6",
            display="flex",
            align_items="center",
            justify_content="center",
            min_height="100vh",
        ),
        rx.button(
            "test",
            size="3",
            on_click=OutputState.increament(),
        )
    )