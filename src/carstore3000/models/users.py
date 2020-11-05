from passlib.hash import sha1_crypt
from sqlalchemy import Column, Integer, String

from carstore3000.extensions import db, ma
from carstore3000.database import CRUDMixin


class UserModel(CRUDMixin, db.Model):
    __tablename__ = 'users'

    index = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    # 2 users can have the same password
    password = Column(String(128), nullable=False)

    @staticmethod
    def set_password(password):
        """Set password."""
        password = sha1_crypt.encrypt(password)
        return password

    def check_password(self, value):
        """Check password."""
        return sha1_crypt.verify(self.password, value)


class UserSchema(ma.SQLAlchemySchema):

    class Meta:
        model = UserModel
        fields = (
            "index",
            "username",
            "password",
        )
