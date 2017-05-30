from wdsauth import db


static_connections = db.Table(
    'static_connections',
    db.Column('system_id', db.Integer, db.ForeignKey('wormholes.system_id')),
    db.Column('static_code', db.String(4), db.ForeignKey('statics.code')),
)


class Static(db.Model):
    __tablename__ = "statics"

    code = db.Column(db.String(4), primary_key=True)
    destination = db.Column(db.String(16))
    stable_time = db.Column(db.Integer)
    total_mass = db.Column(db.Integer)
    max_jump = db.Column(db.Integer)
    info = db.Column(db.Text)

    def __repr__(self):
        static_repr = '[{}] leads to: {}. Life: {} hours. Max mass: {} kT. Max jump: {} kT.'.format(
            self.code,
            self.destination,
            self.stable_time,
            self.total_mass,
            self.max_jump
        )
        if self.info:
            static_repr += ' Info: {}.'.format(self.info)
        return static_repr


class Wormhole(db.Model):
    __tablename__ = "wormholes"

    system_id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(8))
    constellation = db.Column(db.String(8))
    system_name = db.Column(db.String(8))
    system_class = db.Column(db.Integer)
    effect = db.Column(db.String(32))
    radius = db.Column(db.Float)
    moons = db.Column(db.Integer)
    statics = db.relationship(
        'Static',
        secondary=static_connections,
        backref=db.backref('wormholes', lazy='dynamic'),
        lazy='dynamic'
    )

    # planets
    temperate = db.Column(db.Integer)
    ice = db.Column(db.Integer)
    gas = db.Column(db.Integer)
    oceanic = db.Column(db.Integer)
    lava = db.Column(db.Integer)
    barren = db.Column(db.Integer)
    storm = db.Column(db.Integer)
    plasma = db.Column(db.Integer)
    shattered = db.Column(db.Integer)

    # other information like lore
    info = db.Column(db.Text)

    def __repr__(self):
        return 'Wormhole <{}>'.format(self.system_name)

    def planet_count(self):
        return self.temperate + self.ice + self.gas + self.oceanic + self.lava + self.barren + self.storm + \
               self.plasma + self.shattered
