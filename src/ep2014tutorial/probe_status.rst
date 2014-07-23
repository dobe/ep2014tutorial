=================
Probe Status View
=================

The status of the service can be checked via the ``probe_status``
view. This view can be used by downstream load balancers in order to
check availability.

    >>> app.get('/probe_status')
    <200 OK text/plain body=b'OK'>

