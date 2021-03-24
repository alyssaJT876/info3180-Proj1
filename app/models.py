from . import db


class Property(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    bed = db.Column(db.String(200))
    bath = db.Column(db.String(255))
    price = db.Column(db.String(255))
    propType = db.Column(db.String(255))
    location = db.Column(db.String(255))
    description = db.Column(db.String(255))
    picture = db.Column(db.String(255))

    def __init__(self, title, bed, bath, price, propType, location, description, picture):
        self.title=title
        self.bed=bed
        self.bath=bath
        self.price=price
        self.propType=propType
        self.location=location
        self.picture=picture
        self.description = description



    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Property %r>' % (self.title)



