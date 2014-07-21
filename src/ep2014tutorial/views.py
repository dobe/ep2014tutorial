from pyramid.view import view_config
from pyramid.response import Response
from .model import DBSession
import sqlalchemy.exc

@view_config(route_name='probe_status')
def probe_status_view(request):
    response = Response("OK")
    response.content_type = 'text/plain'
    try:
        DBSession.execute('select name from sys.cluster')
    except sqlalchemy.exc.DBAPIError as e:
        response.status = 503
        response.text = 'DBFailure {}'.format(e)
    return response

def includeme(config):
    config.add_route("probe_status", "/probe_status")
