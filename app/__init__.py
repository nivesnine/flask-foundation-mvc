from flask import Flask, render_template
from datetime import datetime

application = Flask(__name__)

application.config.from_object('config')

@application.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app.site.controllers import site as site_module
application.register_blueprint(site_module)

@application.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

