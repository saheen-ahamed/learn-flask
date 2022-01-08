from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

# Resource -- > this class used to create a api requests
# reqparse --> add argument for request (post)
# abort --> send error message

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="view of the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="likes of the video is required", required=True)

videos = {}


def abort_if(video_id):
    if video_id not in videos:
        abort(404, message="video id is not valid...")
    elif video_id in videos:
        abort(409, message="video id already exists...")


class Video(Resource):
    def get(self, video_id):
        abort_if(video_id)
        return videos[video_id]

    def put(self, video_id):
        abort_if(video_id)
        # extracting all the arguments
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201  # can return a status code

    def delete(self, video_id):
        abort_if()
        del videos[video_id]
        return "", 204

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)