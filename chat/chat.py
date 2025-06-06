import reflex as rx
from chat.components import chat, navbar, action_bar
from reflex_chakra import box, flex, button, vstack, text
from chat.state import State

def index() -> rx.Component:
    """Основное приложение."""
    return box(
        flex(
            box(
                rx.foreach(
                    State.chat_titles,
                    lambda chat_name: button(
                        chat_name,
                        on_click=lambda: State.set_chat(chat_name),
                        width="100%",
                        padding="1em",
                        margin_bottom="0.5em",
                        background_color=rx.cond(
                            State.current_chat == chat_name,
                            rx.color("violet", 4),
                            rx.color("mauve", 2),
                        ),
                        color=rx.color("mauve", 12),
                        _hover={"background_color": rx.color("violet", 5)},
                    ),
                ),
                width="20%",
                background_color=rx.color("mauve", 2),
                padding="1em",
                height="100vh",
                overflow_y="auto",
            ),
            vstack(
                navbar(),
                chat(),
                action_bar(),
                width="80%",
                background_color=rx.color("mauve", 1),
                color=rx.color("mauve", 12),
                min_height="100vh",
                align_items="stretch",
                spacing="0",
            ),
            width="100%",
            height="100vh",
        ),
        width="100%",
        height="100vh",
    )

app = rx.App(
    theme=rx.theme(
        appearance="light",
        accent_color="violet",
    ),
)
app.add_page(index)