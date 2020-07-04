def add_post():
    new_title= request.form['title']
    new_content=request.form['content']

    new_post = Posts(new_title= 'title' , new_content= 'content')

    try:
        db.session.add(new_post)
        db.session.commit()
        return 'Post successfully added!!'

    except:
        return 'Error!!'


def show_all():
    Posts=[Posts.query.all()]


def show_one():
    post =Posts.query.get_or_404


def update_post():


def delete_post():
    
