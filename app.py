from flask import Flask
import config
from flask_restful import Api,Resource,fields,marshal_with

app = Flask(__name__)
app.config.from_object(config)
api = Api(app)


class Article(object):
    def __init__(self,title,content):
        self.title=title
        self.content = content

article = Article(title='abc1',content='xx111')

class ArticleView(Resource):

    resource_fields={
        'title':fields.String,
        'content':fields.String
    }

    #     # restful规范中，要求，定义好了返回的参数
    #     # 即使这个参数没有值，也应该返回，返回一个None回去

    @marshal_with(resource_fields)
    def get(self):
        return article


api.add_resource(ArticleView,'/article/',endpoint='article')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
