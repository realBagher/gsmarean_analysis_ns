import datetime
import enum

from sqlalchemy import create_engine, update, insert, delete, ForeignKey, Enum, String, Integer, BigInteger, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column
from sqlalchemy.sql import exists


class DeviceType(enum.Enum):
    Phone = 1,
    Tablet = 2,
    Watch = 3


class Base(DeclarativeBase):
    pass


class Price(Base):
    __tablename__ = 'prices'
    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        name="id",
        autoincrement=True
    )
    name: Mapped[str] = mapped_column(
        String(30),
        name="name"
    )


class UnitOfMemory(Base):
    __tablename__ = 'unit_of_memories'
    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        name="id",
        autoincrement=True
    )
    name: Mapped[str] = mapped_column(
        String(30),
        name="name"
    )
    parent_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey('unit_of_memories.id', ondelete="CASCADE"),
        name="parent_id",
        nullable=True
    )
    exchange: Mapped[int] = mapped_column(
        BigInteger,
        name="exchange",
        nullable=True
    )


class Network(Base):
    __tablename__ = 'networks'
    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        name="id",
        autoincrement=True
    )
    name: Mapped[str] = mapped_column(
        String(30),
        name="name"
    )


class OperationSystem(Base):
    __tablename__ = 'operation_systems'
    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        name="id",
        autoincrement=True
    )
    name: Mapped[str] = mapped_column(
        String(30),
        name="name"
    )


class SimTechnology(Base):
    __tablename__ = 'sim_technologies'
    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        name="id",
        autoincrement=True
    )
    name: Mapped[str] = mapped_column(
        String(30),
        name="name"
    )


class Brand(Base):
    __tablename__ = 'brands'
    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        name="id",
        autoincrement=True
    )
    name: Mapped[str] = mapped_column(
        String(30),
        name="name"
    )


class Device(Base):
    __tablename__ = 'devices'
    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        name="id",
        autoincrement=True
    )
    name: Mapped[str] = mapped_column(
        String(30),
        name="name"
    )
    type: Mapped[Enum] = mapped_column(
        Enum(DeviceType),
        name="type"
    )
    brand_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey('brands.id', ondelete="CASCADE"),
        name="brand_id"
    )
    weight: Mapped[int] = mapped_column(
        Integer,
        name="size_of_display",
        nullable=True
    )
    size_of_display:  Mapped[int] = mapped_column(
        Integer,
        name="size_of_display",
        nullable=True
    )
    battery_capacity: Mapped[int]= mapped_column(
        Integer,
        name="battery_capacity",
        nullable=True
    )
    cpu_model: Mapped[str] = mapped_column(
        String,
        name="cpu_model",
        nullable=True
    )
    count_of_threads: Mapped[int] = mapped_column(
        Integer,
        name="count_of_threads",
        nullable=True
    )
    memory_size: Mapped[int] = mapped_column(
        BigInteger,
        name="memory_size"
    ),
    memory_unit_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey('unit_of_memories.id', ondelete="CASCADE"),
        name="memory_unit_id"
    )
    ram_size: Mapped[int] = mapped_column(
        BigInteger,
        name="ram_size"
    ),
    ram_unit_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey('unit_of_memories.id', ondelete="CASCADE"),
        name="ram_unit_id"
    )
    year_of_the_release: Mapped[datetime.date] = mapped_column(
        Date,
        name="year_of_the_release"
    )


class DeviceNetwork(Base):
    __tablename__ = "device_network"
    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        name="id",
        auto_increment=True
    )
    device_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey('devices.id', ondelete="CASCADE"),
        name="device_id"
    )
    network_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey('networks.id', ondelete="CASCADE"),
        name="network_id"
    )


class DeviceOperationSystem(Base):
    __tablename__ = "device_operation_system"
    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        name="id",
        auto_increment=True
    )
    device_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey('devices.id', ondelete="CASCADE"),
        name="device_id"
    )
    network_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey('operation_systems.id', ondelete="CASCADE"),
        name="network_id"
    )


class DeviceSimTechnology(Base):
    __tablename__ = "device_sim_technology"
    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        name="id",
        auto_increment=True
    )
    device_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey('devices.id', ondelete="CASCADE"),
        name="device_id"
    )
    sim_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey('sim_technologies.id', ondelete="CASCADE"),
        name="sim_id"
    )


if __name__ == "__main__":
    engine = create_engine("mysql+mysqlconnector://quera:123456@localhost:3306/quera_gsmarena", echo=True)
    Base.metadata.create_all(engine)