"""Kurumi Tokisaki support message addon."""

from aqt.gui_hooks import main_window_did_init
from aqt.utils import tooltip

MESSAGE = "<span style='color: red;'>kurumi tokisaki supports passing of actuarial practice CP1</span>"
DISPLAY_DURATION_MS = 5000


def show_support_message(_mw):
    """Display the Kurumi Tokisaki support message when Anki starts."""
    tooltip(MESSAGE, period=DISPLAY_DURATION_MS)


main_window_did_init.append(show_support_message)
