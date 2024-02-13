import datetime
import enum

from sqlalchemy import create_engine, update, insert, delete, ForeignKey, Enum, String, Integer, DECIMAL, BigInteger, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column
from sqlalchemy.sql import exists


class DeviceType(enum.Enum):
    PHONE = 1,
    TABLET = 2,
    WATCH = 3


class CameraPosition(enum.Enum):
    BACK = 1,
    FRONT = 2


class Base(DeclarativeBase):
    pass


class Brand(Base):
    __tablename__ = 'brands'
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        name="id",
        autoincrement=True
    )
    name: Mapped[str] = mapped_column(
        String(200),
        name="name",
        nullable=True
    )


class Network(Base):
    __tablename__ = 'networks'
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        name="id",
        autoincrement=True
    )
    name: Mapped[str] = mapped_column(
        String(200),
        name="name",
        nullable=True
    )


class UnitOfMemory(Base):
    __tablename__ = 'unit_of_memories'
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        name="id",
        autoincrement=True
    )
    name: Mapped[str] = mapped_column(
        String(200),
        name="name",
        nullable=True
    )
    parent_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('unit_of_memories.id', ondelete="CASCADE"),
        name="parent_id",
        nullable=True
    )
    exchange: Mapped[int] = mapped_column(
        Integer,
        name="exchange",
        nullable=True
    )


class Technology(Base):
    __tablename__ = 'technologies'
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        name="id",
        autoincrement=True
    )
    name: Mapped[str] = mapped_column(
        String(200),
        name="name",
        nullable=True
    )


class OperationSystem(Base):
    __tablename__ = 'operation_systems'
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        name="id",
        autoincrement=True
    )
    name: Mapped[str] = mapped_column(
        String(200),
        name="name",
        nullable=True
    )


class Device(Base):
    __tablename__ = 'devices'
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        name="id",
        autoincrement=True
    )
    url: Mapped[str] = mapped_column(
        String(200),
        name="url",
        nullable=True
    )
    name: Mapped[str] = mapped_column(
        String(200),
        name="name",
        nullable=True
    )
    brand_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('brands.id', ondelete="CASCADE"),
        name="brand_id",
        nullable=True
    )
    type: Mapped[Enum] = mapped_column(
        Enum(DeviceType),
        name="type",
        nullable=True
    )
    display_ratio: Mapped[DECIMAL] = mapped_column(
        DECIMAL,
        name="display_ratio",
        nullable=True
    )
    display_size:  Mapped[DECIMAL] = mapped_column(
        DECIMAL,
        name="display_size",
        nullable=True
    )
    weight: Mapped[DECIMAL] = mapped_column(
        DECIMAL,
        name="weight",
        nullable=True
    )
    battery_capacity: Mapped[DECIMAL]= mapped_column(
        Integer,
        name="battery_capacity",
        nullable=True
    )
    pixel_per_inches: Mapped[DECIMAL] = mapped_column(
        Integer,
        name="pixel_per_inches",
        nullable=True
    )
    processor_model: Mapped[str] = mapped_column(
        String(200),
        name="processor_model",
        nullable=True
    )
    count_of_thread: Mapped[str] = mapped_column(
        String(200),
        name="count_of_thread",
        nullable=True
    )
    price: Mapped[DECIMAL] = mapped_column(
        DECIMAL,
        name="price",
        nullable=True
    )
    year_of_release: Mapped[datetime.date] = mapped_column(
        Date,
        name="year_of_release"
    )
    operation_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('operation_systems.id', ondelete="CASCADE"),
        name="operation_id",
        nullable=True
    )
    operation_system_version: Mapped[str] = mapped_column(
        String(200),
        name="operation_system_version",
        nullable=True
    )


class DeviceDimension(Base):
    __tablename__ = "devices_dimensions"
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        name="id",
        autoincrement=True
    )
    device_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('devices.id', ondelete="CASCADE"),
        name="device_id",
        nullable=True
    )
    height: Mapped[DECIMAL] = mapped_column(
        DECIMAL,
        name="height",
        nullable=True
    )
    width: Mapped[DECIMAL] = mapped_column(
        DECIMAL,
        name="width",
        nullable=True
    )
    depth: Mapped[DECIMAL] = mapped_column(
        DECIMAL,
        name="depth",
        nullable=True
    )


class DevicesCamera(Base):
    __tablename__ = "devices_cameras"
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        name="id",
        auto_increment=True
    )
    pixel: Mapped[DECIMAL] = mapped_column(
        DECIMAL,
        name="pixel",
        nullable=True
    )
    position: Mapped[Enum] = mapped_column(
        Enum(CameraPosition),
        name="position",
        nullable=True
    )
    type: Mapped[str] = mapped_column(
        String(200),
        name="type",
        nullable=True
    )
    device_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('devices.id', ondelete="CASCADE"),
        name="device_id"
    )


class DeviceNetwork(Base):
    __tablename__ = "devices_networks"
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        name="id",
        auto_increment=True
    )
    device_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('devices.id', ondelete="CASCADE"),
        name="device_id"
    )
    network_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('networks.id', ondelete="CASCADE"),
        name="network_id"
    )


class DeviceTechnology(Base):
    __tablename__ = "devices_technologies"
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        name="id",
        auto_increment=True
    )
    device_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('devices.id', ondelete="CASCADE"),
        name="device_id"
    )
    technology_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('technologies.id', ondelete="CASCADE"),
        name="technology_id"
    )


class DeviceMemory(Base):
    __tablename__ = ""
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        name="id",
        autoincrement=True
    )
    device_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('devices.id', ondelete="CASCADE"),
        name="device_id",
        nullable=True
    )
    memory_size: Mapped[DECIMAL] = mapped_column(
        DECIMAL,
        name="memory_size",
        nullable=True
    ),
    memory_unit_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('unit_of_memories.id', ondelete="CASCADE"),
        name="memory_unit_id"
    )
    ram_size: Mapped[int] = mapped_column(
        DECIMAL,
        name="ram_size",
        nullable=True
    ),
    ram_unit_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey('unit_of_memories.id', ondelete="CASCADE"),
        name="ram_unit_id"
    )

