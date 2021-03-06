from pyramid.view import view_config
from pyramid.response import Response
from .model import DBSession, Tweet
import sqlalchemy.exc
from pyramid.renderers import JSON


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


@view_config(route_name='latest')
def latest_tweets(request, request_method='GET'):
    limit = int(request.GET.get('limit', 10))
    query = DBSession.query(Tweet).order_by(
                Tweet.created_at.desc(), Tweet.id.desc()
            ).limit(limit)
    return list(query)


def includeme(config):
    # use the JSON response renderer for all views
    config.add_renderer(None, JSON(indent=4))
    config.add_route("probe_status", "/probe_status")
    config.add_route("latest", "/latest")
