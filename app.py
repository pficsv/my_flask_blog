from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.now())


@app.route('/')
def index():
    posts = BlogPost.query.order_by(BlogPost.date_created.desc()).all()
    return render_template('index.html', posts=posts)

@app.route('/add', methods = ['POST'])
def add_post():
    title = request.form['title']
    content = request.form['content']
    new_post = BlogPost(title=title, content=content)
    db.session.add(new_post)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete_post(id):
    post_to_delete = BlogPost.query.get_or_404(id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
