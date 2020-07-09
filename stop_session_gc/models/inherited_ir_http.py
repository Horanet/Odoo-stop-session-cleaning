from odoo import http


def session_gc_disabled(session_store):
    """Disable odoo garbage collector for performance reasons.

    Garbage collector should be done using a CRON.
    """
    pass

http.session_gc = session_gc_disabled
