from sqlalchemy import Column, Float, Integer, String

from carstore3000.extensions import db, ma
from carstore3000.database import CRUDMixin


class CarModel(CRUDMixin, db.Model):
    __tablename__ = 'cars'

    index = Column(Integer, primary_key=True)
    car_id = Column(String)
    color_slug = Column(String)
    door_count = Column(Integer)
    engine_displacement = Column(String)
    engine_power = Column(String)
    fuel_type = Column(String)
    maker = Column(String)
    model = Column(String)
    mileage = Column(Integer)
    manufacture_year = Column(String)
    price_eur = Column(Float)
    seat_count = Column(Integer)
    transmission = Column(String)


class CarSchema(ma.SQLAlchemySchema):

    class Meta:
        model = CarModel
        fields = (
            "index",
            "car_id",
            "color_slug",
            "door_count",
            "engine_displacement",
            "engine_power",
            "fuel_type",
            "maker",
            "model",
            "mileage",
            "manufacture_year",
            "price_eur",
            "seat_count",
            "transmission",
        )
