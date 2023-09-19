from .database import db

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, unique=False, nullable=True)
    start_date = db.Column(db.String(12), unique=False, nullable=False)
    end_date = db.Column(db.String(12), unique=False, nullable=False)
    prices = db.relationship('Build', back_populates='build')


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String(12), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), unique=False, nullable=False)
    profile_picture = db.Column(db.String(20), unique=False, nullable=False)
    dash_state = db.Column(db.String(20), unique=False, nullable=True)


class Manufacturer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False,   nullable=False)
    partner = db.Column(db.Boolean, nullable=False, default=False)
    sponsor = db.Column(db.Boolean, nullable=False, default=False)
    part_cpu = db.relationship('PartCpu', back_populates='manufacturer')
    part_cpu_cooler = db.relationship('PartCpuCooler', back_populates='manufacturer')
    part_motherboard = db.relationship('PartMotherboard', back_populates='manufacturer')
    part_memory = db.relationship('PartMemory', back_populates='manufacturer')
    part_storage = db.relationship('PartStorage', back_populates='manufacturer')
    part_gpu = db.relationship('PartGpu', back_populates='manufacturer')
    part_case = db.relationship('PartCase', back_populates='manufacturer')
    part_psu = db.relationship('PartPsu', back_populates='manufacturer')


class Build(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
    part_cpu = db.relationship('PartCpu', back_populates='build')
    part_cpu_cooler = db.relationship('PartCpuCooler', back_populates='build')
    part_motherboard = db.relationship('PartMotherboard', back_populates='build')
    part_memory = db.relationship('PartMemory', back_populates='build')
    part_storage = db.relationship('PartStorage', back_populates='build')
    part_gpu = db.relationship('PartGpu', back_populates='build')
    part_case = db.relationship('PartCase', back_populates='build')
    part_psu = db.relationship('PartPsu', back_populates='build')


class PartCpu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
    price = db.Column(db.Float, unique=False, nullable=False)
    dop = db.Column(db.Datetime, unique=False, nullable=False)
    purchased_by = db.Column(db.String(10), unique=False, nullable=False)
    generation = db.Column(db.Integer, unique=False, nullable=True)
    clockspeed = db.Column(db.String, unique=False, nullable=True)
    build_id = db.Column(db.Integer, db.ForeignKey('build.id'))
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturer.id'))
    build = db.relationship('Build', back_populates='part_cpu', lazy=True, nullable=True)
    manufacturer = db.relationship('Manufacturer', back_populates='part_cpu', lazy=True, nullable=False)


class PartCpuCooler(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
    price = db.Column(db.Float, unique=False, nullable=False)
    dop = db.Column(db.Datetime, unique=False, nullable=False)
    purchased_by = db.Column(db.String(10), unique=False, nullable=False)
    build_id = db.Column(db.Integer, db.ForeignKey('build.id'))
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturer.id'))
    build = db.relationship('Build', back_populates='part_cpu_cooler', lazy=True, nullable=True)
    manufacturer = db.relationship('Manufacturer', back_populates='part_cpu_cooler', lazy=True, nullable=False)


class PartMotherboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
    price = db.Column(db.Float, unique=False, nullable=False)
    dop = db.Column(db.Datetime, unique=False, nullable=False)
    purchased_by = db.Column(db.String(10), unique=False, nullable=False)
    build_id = db.Column(db.Integer, db.ForeignKey('build.id'))
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturer.id'))
    build = db.relationship('Build', back_populates='part_motherboard', lazy=True, nullable=True)
    manufacturer = db.relationship('Manufacturer', back_populates='part_motherboard', lazy=True, nullable=False)
    size = db.Column(db.String, unique=False)


class PartMemory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
    price = db.Column(db.Float, unique=False, nullable=False)
    dop  = db.Column(db.Datetime, unique=False, nullable=False)
    purchased_by = db.Column(db.String(10), unique=False, nullable=False)
    capacity = db.Column(db.Integer, unique=False)
    speed = db.Column(db.String, unique=False)
    build_id = db.Column(db.Integer, db.ForeignKey('build.id'))
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturer.id'))
    build = db.relationship('Build', back_populates='part_memory', lazy=True, nullable=True)
    manufacturer = db.relationship('Manufacturer', back_populates='part_memory', lazy=True, nullable=False)


class PartStorage(db.Model):
    id = db.Column(db.Integer,  primary_key=True)
    name = db.Column(db.String,   unique=False, nullable=False)
    price = db.Column(db.Float,    unique=False, nullable=False)
    dop = db.Column(db.Datetime, unique=False, nullable=False)
    purchased_by = db.Column(db.String(10), unique=False, nullable=False)
    category = db.Column(db.String, unique=False)
    build = db.relationship('Build', back_populates='part_storage', lazy=True, nullable=True)
    manufacturer = db.relationship('Manufacturer', back_populates='part_storage', lazy=True, nullable=False)
    build_id = db.Column(db.Integer, db.ForeignKey('build.id'))
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturer.id'))


class PartGpu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
    price = db.Column(db.Float, unique=False, nullable=False)
    dop = db.Column(db.Datetime, unique=False, nullable=False)
    purchased_by = db.Column(db.String(10), unique=False, nullable=False)
    vram = db.Column(db.Integer, unique=False)
    build = db.relationship('Build', back_populates='part_gpu', lazy=True, nullable=True)
    manufacturer = db.relationship('Manufacturer', back_populates='part_gpu', lazy=True, nullable=False)
    build_id = db.Column(db.Integer, db.ForeignKey('build.id'))
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturer.id'))

class PartCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
    price = db.Column(db.Float, unique=False, nullable=False)
    dop = db.Column(db.Datetime, unique=False, nullable=False)
    purchased_by = db.Column(db.String(10), unique=False, nullable=False)
    build_id = db.Column(db.Integer, db.ForeignKey('build.id'))
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturer.id'))
    manufacturer = db.relationship('Manufacturer', back_populates='part_case', lazy=True, nullable=False)
    build = db.relationship('Build', back_populates='part_case', lazy=True, nullable=True)


class PartPsu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
    price = db.Column(db.Float, unique=False, nullable=False)
    dop  = db.Column(db.Datetime, unique=False, nullable=False)
    purchased_by = db.Column(db.String(10), unique=False, nullable=False)
    wattage = db.Column(db.Integer, unique=False)
    build_id = db.Column(db.Integer, db.ForeignKey('build.id'))
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturer.id'))
    build = db.relationship('Build', back_populates='part_psu', lazy=True, nullable=True)
    manufacturer = db.relationship('Manufacturer', back_populates='part_psu', lazy=True, nullable=False)


