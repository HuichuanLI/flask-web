
from application import app
from indexController import index_page
from postController import post_page


app.register_blueprint(index_page, url_prefix="/huichuan")
app.register_blueprint(post_page, url_prefix="/post")
