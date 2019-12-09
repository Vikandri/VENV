import flask

app = flask.Flask(__name__)
app.secret_key = b'toto je zcela nahodny retezec nejlepsi os.urandom(24)'
app.secret_key = b'\xbfp\xf9h\xb8M\xef\xfa\xaduy\xd1\xe0\xf3+]^\x95!HxS\xd3'
