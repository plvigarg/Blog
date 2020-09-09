from flask import Blueprint, render_template

error_pages = Blueprint('error_pages', __name__)


@error_pages.app_errorhandler(404)
def error_404(error):
    return render_template('error_pages/404.html'), 404


@error_pages.app_errorhandler(403)
def bar(error):
    return render_templaerror_pages.te('error.html/403.html'), 403
