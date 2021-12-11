from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("root", "root", "./output", perm="elradfmwMT")

handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(("192.168.0.31", 21), handler)
server.serve_forever()