import datetime,os
from flask import Flask,render_template,flash,url_for,redirect,request,session

# pip install Flask-SQLALchemy
# from flask_sqlalchemy import SQLAlchemy
# from passlib.hash import sha256_crypt
# import pymysql
# engine=create_engine("mysql+pymysql://root:123456@localhost/register")
                    #(mysql+pymysql://username:password@localhost/database)
# db=scoped_session(sessionmaker(bind=engine))
app=Flask(__name__)
_FOLDER = os.path.join('static', 'photos')
app.config['UPLOAD_FOLDER'] = _FOLDER
# # app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite'

# app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/test'
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# app.secret_key='amitsolasjdh367@ejhks'
# db=SQLAlchemy(app)

# class Register(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String(20))
#     email=db.Column(db.String(30),unique=True,nullable=False)
    # pwd=db.Column(db.String(100),nullable=False)
    # c_pwd=db.Column(db.String(100),nullable=False)
    # mobile=db.Column(db.String(10))

@app.route("/")
def home():
    print(request.data)
    # d=Register().query.all()
    d="none"
    return render_template("index.html",data=d)
        

@app.route("/add_new",methods=['POST'])
def generateQRcode():
    if request.method=="POST":
        code=request.form.get('code')
        if code:
            import qrcode
            qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=20,border=2)
            qr.add_data(code)
            qr.make(fit=True)
            img=qr.make_image()
            img=qr.make_image(fill_color='red',back_color='black')
            print(datetime.datetime.hour)
            t= os.path.join(app.config['UPLOAD_FOLDER'], str(232)+'.png')
            # t='amot.png'
            img.save(t)
        # t=datetime.datetime.now()
        # new_blg=blogs(user_name=name,email=email,title=title,blog_content=blog_data,blog_date=t)
        # db.session.add(new_blg)
        # db.session.commit()
            # return redirect(url_for("home",data=t))
            return render_template("index.html",data=t)
    return redirect(url_for("home"))


@app.route("/delete/<int:no>")
def delete(no):
    # result=blogs.query.filter_by(id=no).first()
    # db.session.delete(result)
    # db.session.commit()
    return redirect("/")


@app.route("/about")
def about():
    return render_template("about.html")    


if __name__=="__main__":
    if not os.path.exists('db.sqlite'):
        pass
        # db.create_all()
    app.run(debug=True,port=8080)
    

