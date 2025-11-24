from flask import Flask, request, jsonify, abort
from dotenv import load_dotenv
from db import init_db
from blog import Blog

load_dotenv()

app = Flask(__name__)

init_db()

def require_json(keys):
    data = request.get_json(silent=True)
    if not data:
        abort(400, description="Expected JSON body")
    for k in keys:
        if k not in data:
            abort(400, description=f"Missing field: {k}")
    return data


@app.route("/blogs", methods=["POST"])
def create_blog():
    data = require_json(["title", "content"])
    blog = Blog(title=data["title"], content=data["content"])
    blog.save()
    return jsonify(blog.to_dict()), 201

@app.route("/blogs", methods=["GET"])
def list_blogs():
    blogs = Blog.get_all()
    blogs_json = list(map(lambda b: b.to_dict(), blogs))
    blogs_json = list(filter(lambda b: b.get("title"), blogs_json))
    return jsonify(blogs_json), 200

@app.route("/blogs/<int:blog_id>", methods=["GET"])
def get_blog(blog_id):
    blog = Blog.get_by_id(blog_id)
    if not blog:
        abort(404, description="Blog not found")
    return jsonify(blog.to_dict()), 200

@app.route("/blogs/<int:blog_id>", methods=["PUT"])
def update_blog(blog_id):
    blog = Blog.get_by_id(blog_id)
    if not blog:
        abort(404, description="Blog not found")
    data = require_json(["title", "content"])
    for key in ("title", "content"):
        if key in data:
            setattr(blog, key, data[key])
    blog.update()
    return jsonify(blog.to_dict()), 200

@app.route("/blogs/<int:blog_id>", methods=["DELETE"])
def delete_blog(blog_id):
    blog = Blog.get_by_id(blog_id)
    if not blog:
        abort(404, description="Blog not found")
    blog.delete()
    return jsonify({"message": "Deleted"}), 200

@app.route("/blogs/<int:blog_id>/translate", methods=["GET"])
def translate_blog(blog_id):
    source = request.args.get("source", "auto")
    target = request.args.get("target", "en")
    speak = request.args.get("speak", "false").lower() in ("1", "true", "yes")
    blog = Blog.get_by_id(blog_id)
    if not blog:
        abort(404, description="Blog not found")

    result = blog.translate_and_speak(source=source, target=target, speak=speak)
    response = {
        "id": blog.id,
        "original_title": blog.title,
        "original_content": blog.content,
        "translated_content": result.get("translated_text"),
        "audio_file": result.get("audio_file")
    }
    if result.get("error"):
        response["error"] = result["error"]
    return jsonify(response), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)