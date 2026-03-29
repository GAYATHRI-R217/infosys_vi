"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
def index():
    return rx.container(
        rx.heading("AI Based Document search and Knowledge Base", size="8"),
        rx.text_area(placeholder="Paste your text here...", width="100%",height="300px"),
        rx.upload_files(rx.text("Upload your documents here..."), margin_top="10px"),
        rx.button("Get Information",margin_top="10px"),
        rx.divider(),
    )

app = rx.App()
app.add_page(index)
