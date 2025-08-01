import reflex as rx

config = rx.Config(
    app_name="langchain_reflex_agent",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)