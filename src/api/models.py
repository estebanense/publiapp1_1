from enum import unique
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=False, nullable=False) 
    email = db.Column(db.String(120), unique=True, nullable=False) 
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)  
    vallas= db.relationship('Valla', backref='user', lazy=True)   # relationship
    orders= db.relationship('Order', backref='user', lazy=True)    # relationship
    clients= db.relationship('Client', backref='user', lazy=True)    # relationship
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)  #FK

   
  

    def __repr__(self):
        return 'User %r' % self.name   # printed at shell

    def serialize(self):
        #role = Role.query.filter_by(id=self.role_id).first() 
        return {
            "id": self.id,
            "name":self.name,
            "email": self.email,
            "is_active":self.is_active,
            "role_id": self.role_id,
            

            # do not serialize the password, its a security breach
        }

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    users= db.relationship('User', backref='role', lazy=True)   # relationship

    def __repr__(self):
        return '%r' % self.name    # <'Role %r'> % self.name
    
    def serialize(self):
        return {
            "role_id": self.id,
            "role_name": self.name,
        }

        
class Order(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    order_price = db.Column(db.Integer, unique=False)
    created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)  
    start_date = db.Column(db.DateTime, unique=False, nullable=False)
    finish_date = db.Column(db.DateTime, unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  #FK
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)  #FK
    vallas= db.relationship('Valla', backref='order', lazy=True)   # relationship
    payments= db.relationship('Payment', backref='order', lazy=True)    # relationship
    
    def __repr__(self):
        return '<Order %r>' % self.id
    
    def serialize(self):
        return {
            "order_id": self.id,
        }
class Payment(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    due_date = db.Column(db.DateTime, unique=False, nullable=True)
    payment_date = db.Column(db.DateTime, unique=False, nullable=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)  #FK
    
    def __repr__(self):
        return '<Payment %r>' % self.id
    
    def serialize(self):
        return {
            "payment_id": self.id,
        }        
        
class Valla(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(150), unique=False, nullable=False)
    format = db.Column(db.String(20), unique=False,default='Horizontal / Vertical', nullable= False)
    light = db.Column(db.Boolean, default='True') 
    price_low = db.Column(db.Float, unique=False, nullable=True)  
    price_high = db.Column(db.Float, unique=False, nullable=True)
    view = db.Column(db.String(150), unique=False, nullable=False)
    route = db.Column(db.String(150), unique=False, nullable=False)
    dateCreated = db.Column(db.DateTime, default=datetime.utcnow, nullable=False) 
    comment = db.Column(db.Text, unique=False, nullable=True) 
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=False) #FK
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=True) #FK
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) #FK
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=True) #FK
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=True) #FK
    size_id = db.Column(db.Integer, db.ForeignKey('size.id'), nullable=True) #FK
    type_id = db.Column(db.Integer, db.ForeignKey('type.id'), nullable=False) #FK   
    
    def __repr__(self):
        return '<Valla %r>' % self.code

    def serialize(self):
         status = Status.query.filter_by(id=self.status_id).first() 
         client = Client.query.filter_by(id=self.client_id).first() 
         owner = Owner.query.filter_by(id=self.owner_id).first() 
         
         return  {
            "id": self.id,
            "code": self.code,
            "name": self.name,
            "format": self.format,
            "light": self.light,
            "price_low": self.price_low,
            "price_high": self.price_high,
            "view": self.view,
            "route":self.route,
            "dateCreated": self.dateCreated,
            "comment": self.comment,
            "owner_id": self.owner_id,
            "client_id": self.client_id,
            "user_id": self.user_id,
            "order_id": self.order_id,
            "status_id": self.status_id,
            "size_id": self.size_id,
            "type_id": self.client_id
        }
        
class Status(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=True)
    vallas = db.relationship('Valla', backref='status', lazy=True)   # relationship
    
    def __repr__(self):
        return '<%r>' % self.name
    
    def serialize(self):
        return {
            "status_id": self.id,
            "self_name": self.name
        }   
        
class Size(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=False, nullable=True)
    vallas = db.relationship('Valla', backref='size', lazy=True)   # relationship
    
    def __repr__(self):
        return '<%r>' % self.name
    
    def serialize(self):
        return {
            "size_id": self.id,
            "self_name": self.name,
        }  
        
class Type(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=True)
    vallas = db.relationship('Valla', backref='type', lazy=True)   # relationship
    
    def __repr__(self):
        return '<%r>' % self.name
    
    def serialize(self):
        return {
            "size_id": self.id,
            "self_name": self.name,
        }                                      

class Owner(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=False, nullable=False)
    code = db.Column(db.String(10), unique=True, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False) 
    phone = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    company = db.Column(db.String(80), unique=True, nullable=True)
    vallas = db.relationship('Valla', backref='owner', lazy=True)   # relationship
    
    def __repr__(self):
        return '<%r>' % self.name
    
    def serialize(self):
        return {
            "owner_id": self.id,
            "owner_name": self.name,
            "owner_code": self.code,
            "phone": self.phone,
            "email": self.email, 
            "company": self.company,
        }
        
class Client(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=False, nullable=False)
    code = db.Column(db.String(10), unique=True, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)  
    phone = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    company = db.Column(db.String(80), unique=True, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) #FK
    vallas = db.relationship('Valla', backref='client', lazy=True)   # relationship
    orders = db.relationship('Order', backref='client', lazy=True)    # relationship
    
    
    def __repr__(self):
        return '<%r>' % self.name
    
    def serialize(self):
        return {
            "client_id": self.id,
            "client_name": self.name,
            "client_code": self.code,
            "phone": self.phone,
            "email": self.email, 
            "company": self.company,
        }   