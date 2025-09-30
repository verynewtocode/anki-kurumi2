"""Kurumi Tokisaki support message addon."""

from typing import Optional

from aqt import mw as main_window
from aqt.gui_hooks import main_window_did_init
from aqt.qt import QLabel, Qt

MESSAGE = "<span style='color: red;'>Kurumi Tokisaki supports passing of actuarial practice CP1</span>"
WIDGET_OBJECT_NAME = "kurumi_support_message_label"


def _remove_existing_label(parent) -> None:
    """Remove a previously injected label if it exists.

    Re-adding the widget on subsequent hook invocations without removing the
    old instance would lead to duplicated messages in the status bar.
    """

    for child in parent.findChildren(QLabel):
        if child.objectName() == WIDGET_OBJECT_NAME:
            parent.removeWidget(child)
            child.deleteLater()


def show_support_message(mw: Optional[object] = None) -> None:
    """Display the support message in Anki's status bar when it starts.

    The hook signature changed in Anki 25.07 so the ``mw`` argument became
    optional. Accepting it as an optional parameter keeps compatibility with
    both old and new versions of Anki.
    """

    if mw is None:
        mw = main_window

    if mw is None or not getattr(mw, "form", None):
        return

    status_bar = getattr(mw.form, "statusbar", None)
    if status_bar is None:
        return

    _remove_existing_label(status_bar)

    label = QLabel()
    label.setObjectName(WIDGET_OBJECT_NAME)
    label.setTextFormat(Qt.RichText)
    label.setText(MESSAGE)

    status_bar.addPermanentWidget(label)


main_window_did_init.append(show_support_message)
