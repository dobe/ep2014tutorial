=====
Views
=====

    >>> from datetime import datetime

Latest Tweets
=============

It is possible to request the lastest tweets using the `latest` endpoint.

Nothing is returned because our test database is empty::

    >>> pprint(app.get('/latest').json)
    []

Create a Tweet::

    >>> from ep2014tutorial import model
    >>> model.DBSession.add(model.Tweet(
    ...              id='1',
    ...              created_at=datetime(2014, 7, 23, 14, 0, 0),
    ...              text='tweet1',
    ...              source='test'
    ... ))
    >>> refresh()

    >>> pprint(app.get('/latest').json)
    [{'created_at': '2014-07-23T14:00:00', 'id': '1', 'text': 'tweet1'}]

A tweet with user data::

    >>> model.DBSession.add(model.Tweet(
    ...              id='2',
    ...              created_at=datetime(2014, 7, 23, 14, 0, 1),
    ...              text='tweet2',
    ...              source='test',
    ...              user={'id': 'user_id1'},
    ... ))
    >>> refresh()

    >>> pprint(app.get('/latest').json)
    [{'created_at': '2014-07-23T14:00:01',
      'id': '2',
      'text': 'tweet2',
      'user': 'user_id1'},
     {'created_at': '2014-07-23T14:00:00', 'id': '1', 'text': 'tweet1'}]

Use the `limit` GET parameter::

    >>> pprint(app.get('/latest?limit=1').json)
    [{'created_at': '2014-07-23T14:00:01',
      'id': '2',
      'text': 'tweet2',
      'user': 'user_id1'}]
