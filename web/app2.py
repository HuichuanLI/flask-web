from werkzeug.wrappers import Request, Response


class Shortly(object):
    def __call__(self, environ, start_response):
        # start_response('200 ok', [('Content-type', 'text/plain')])
        # return [b'hello world~']
        request = Request(environ)
        text = "Hello world~" + request.args.get('a', '123')
        response = Response(text, mimetype="text/plain")
        return response(environ, start_response)


if __name__ == "__main__":
    from werkzeug.serving import run_simple

    app = Shortly()
    run_simple('0.0.0.0', 5000, app)
