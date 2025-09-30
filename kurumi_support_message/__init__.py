"""Kurumi Tokisaki support message addon."""

from aqt.gui_hooks import main_window_did_init
from aqt.utils import tooltip

MESSAGE = "<span style='color: red;'>kurumi tokisaki supports passing of actuarial practice CP1</span>"
DISPLAY_DURATION_MS = 5000


def show_support_message(_mw=None):
    """Display the support message when Anki starts.

    The hook signature changed in Anki 25.07 so the `_mw` argument became
    optional. Accepting it as an optional parameter keeps compatibility with
    both old and new versions of Anki.
    """
    tooltip(MESSAGE, period=DISPLAY_DURATION_MS)


main_window_did_init.append(show_support_message)
