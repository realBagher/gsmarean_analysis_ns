from __future__ import annotations

import configparser

from sqlalchemy import create_engine, insert, select, update
from sqlalchemy.orm import Session
from sqlalchemy.sql import exists

from entities import (Brand as BrandEntity,
                      Device as DeviceEntity,
                      Technology as TechnologyEntity,
                      DeviceTechnology as DeviceTechnologyEntity,
                      Sensor as SensorEntity,
                      DeviceSensor as DeviceSensorEntity,
                      Network as NetworkEntity,
                      DeviceNetwork as DeviceNetworkEntity,
                      OperationSystem as OperationSystemEntity,
                      DeviceDimension as DeviceDimensionEntity,
                      DeviceCamera as DeviceCameraEntity,
                      DeviceMemory as DeviceMemoryEntity,
UnitOfMemory as UnitOfMemoryMemoryEntity
                      )


class BaseRepository(object):
    def __init__(self):
        self._config = configparser.ConfigParser()
        with open('config.ini') as configfile:
            self._config.read_string(configfile.read())

    @property
    def config(self):
        return self._config

    @property
    def connection_string(self):
        conne = f'mysql+mysqlconnector://{self.config["database"]["username"]}:{self.config["database"]["password"]}@{self.config["database"]["server"]}:3306/{self.config["database"]["database"]}'
        print(conne)
        return conne


class DeviceRepository(BaseRepository):
    def __check_device_exists(self, url: str) -> bool:
        with Session(create_engine(self.connection_string)) as session:
            return session.query(exists().where(DeviceEntity.url == url)).scalar() is False

    def save(self, device: DeviceEntity):
        if self.__check_device_exists(device.url) is False:
            with Session(create_engine(self.connection_string)) as session:
                session.execute(insert(DeviceEntity).values({
                    "url": device.url,
                    "name": device.name,
                    "bran_id": device.brand_id,
                    "type": device.type,
                    "display_ratio": device.display_ratio,
                    "display_size": device.display_size,
                    "weight": device.weight,
                    "battery_capacity": device.battery_capacity,
                    "pixel_per_inches": device.pixel_per_inches,
                    "processor_model": device.processor_model,
                    "count_of_thread": device.count_of_thread,
                    "price": device.price,
                    "year_of_release": device.year_of_release,
                    "operation_id": device.operation_id,
                    "operation_system_version": device.operation_system_version
                }))


class TechnologyRepository(BaseRepository):
    def get_id_by_name(self, name: str) -> int | None:
        with Session(create_engine(self.connection_string)) as session:
            return session.scalars(select(TechnologyEntity.id).where(TechnologyEntity.name == name)).first()

    def save(self, name: str) -> int:
        id = self.get_id_by_name(name)
        if id is None:
            with Session(create_engine(self.connection_string)) as session:
                session.execute(insert(TechnologyEntity).values({"name": name}))
            id = self.get_id_by_name(name)
        return id

    def check_connection_between(self, device: int, technology: int) -> int:
        with Session(create_engine(self.connection_string)) as session:
            return session.scalars(select(DeviceTechnologyEntity.id).where(
                DeviceTechnologyEntity.device_id == device and DeviceTechnologyEntity.technology_id == technology)).first()

    def connect_to_device(self, device: int, technology: int) -> int:
        id = self.check_connection_between(device, technology)
        if id is None:
            with Session(create_engine(self.connection_string)) as session:
                session.execute(
                    insert(DeviceTechnologyEntity).values({"device_id": device, "technology_id": technology}))
            id = self.check_connection_between(device, technology)
        return id


class SensorRepository(BaseRepository):
    def get_id_by_name(self, name: str) -> int | None:
        with Session(create_engine(self.connection_string)) as session:
            return session.scalars(select(SensorEntity.id).where(SensorEntity.name == name)).first()

    def save(self, name: str) -> int:
        id = self.get_id_by_name(name)
        if id is None:
            with Session(create_engine(self.connection_string)) as session:
                session.execute(insert(SensorEntity).values({"name": name}))
            id = self.get_id_by_name(name)
        return id

    def check_connection_between(self, device: int, sensor: int) -> int:
        with Session(create_engine(self.connection_string)) as session:
            return session.scalars(select(DeviceSensorEntity.id).where(
                DeviceSensorEntity.device_id == device and DeviceSensorEntity.sensor_id == sensor)).first()

    def connect_to_device(self, device: int, sensor: int) -> int:
        id = self.check_connection_between(device, sensor)
        if id is None:
            with Session(create_engine(self.connection_string)) as session:
                session.execute(insert(DeviceSensorEntity).values({"device_id": device, "sensor_id": sensor}))
            id = self.check_connection_between(device, sensor)
        return id


class NetworkRepository(BaseRepository):
    def get_id_by_name(self, name: str) -> int | None:
        with Session(create_engine(self.connection_string)) as session:
            return session.scalars(select(NetworkEntity.id).where(NetworkEntity.name == name)).first()

    def save(self, name: str) -> int:
        id = self.get_id_by_name(name)
        if id is None:
            with Session(create_engine(self.connection_string)) as session:
                session.execute(insert(NetworkEntity).values({"name": name}))
            id = self.get_id_by_name(name)
        return id

    def check_connection_between(self, device: int, network: int) -> int:
        with Session(create_engine(self.connection_string)) as session:
            return session.scalars(select(DeviceNetworkEntity.id).where(
                DeviceNetworkEntity.device_id == device and DeviceNetworkEntity.network_id == network)).first()

    def connect_to_device(self, device: int, network: int) -> int:
        id = self.check_connection_between(device, network)
        if id is None:
            with Session(create_engine(self.connection_string)) as session:
                session.execute(insert(DeviceNetworkEntity).values({"device_id": device, "network_id": network}))
            id = self.check_connection_between(device, network)
        return id


class BrandRepository(BaseRepository):
    def get_id_by_name(self, name: str) -> int | None:
        engine = create_engine(self.connection_string)
        with Session(engine) as session:
            return session.scalars(select(BrandEntity.id).where(BrandEntity.name == name)).first()

    def save(self, name: str) -> int:
        id = self.get_id_by_name(name)
        if id is None:
            with Session(create_engine(self.connection_string)) as session:
                session.execute(insert(BrandEntity).values({"name": name}))
            id = self.get_id_by_name(name)
        return id


class OperationSystemRepository(BaseRepository):
    def get_id_by_name(self, name: str) -> int | None:
        engine = create_engine(self.connection_string)
        with Session(engine) as session:
            return session.scalars(select(OperationSystemEntity.id).where(OperationSystemEntity.name == name)).first()

    def save(self, name: str) -> int:
        id = self.get_id_by_name(name)
        if id is None:
            with Session(create_engine(self.connection_string)) as session:
                session.execute(insert(OperationSystemEntity).values({"name": name}))
            id = self.get_id_by_name(name)
        return id


class DeviceDimensionRepository(BaseRepository):
    def get_id_by_device_id(self, device_id: int) -> int | None:
        engine = create_engine(self.connection_string)
        with Session(engine) as session:
            return session.scalars(
                select(DeviceDimensionEntity.id).where(DeviceDimensionEntity.device_id == device_id)).first()

    def save(self, dimension: DeviceDimensionEntity) -> int:
        id = self.get_id_by_device_id(dimension.device_id)
        if id is None:
            with Session(create_engine(self.connection_string)) as session:
                session.execute(insert(DeviceDimensionEntity).values({
                    "height": dimension.height,
                    "width": dimension.width,
                    "depth": dimension.depth,
                    "device_id": dimension.device_id
                }))
            id = self.get_id_by_device_id(dimension.device_id)
        else:
            self.update(id, dimension)
        return id

    def update(self, id: int, dimension: DeviceDimensionEntity) -> int:
        with Session(create_engine(self.connection_string)) as session:
            session.execute(update(DeviceDimensionEntity).where(DeviceDimensionEntity.id == id).values(
                {
                    "height": dimension.height,
                    "width": dimension.width,
                    "depth": dimension.depth
                }
            ))
        return id


class DeviceCameraRepository(BaseRepository):
    def save(self, camera: DeviceCameraEntity):
        with Session(create_engine(self.connection_string)) as session:
            session.execute(insert(DeviceCameraEntity).values({
                "pixel": camera.pixel,
                "position": camera.position,
                "type": camera.type,
                "device_id": camera.device_id
            }))


class DeviceMemoryRepository(BaseRepository):
    def save(self, memory: DeviceMemoryEntity):
        with Session(create_engine(self.connection_string)) as session:
            session.execute(insert(DeviceMemoryEntity).values({
                "memory_size": memory.memory_size,
                "memory_unit_id": memory.memory_unit_id,
                "ram_size": memory.ram_size,
                "ram_unit_id": memory.ram_unit_id,
                "device_id": memory.device_id
            }))


class UnitOfMemoryRepository(BaseRepository):
    def get_id_by_name(self, name: str) -> int | None:
        engine = create_engine(self.connection_string)
        with Session(engine) as session:
            return session.scalars(select(UnitOfMemoryMemoryEntity.id).where(UnitOfMemoryMemoryEntity.name == name)).first()

    def save(self, memory: UnitOfMemoryMemoryEntity) -> int:
        id = self.get_id_by_name(memory.name)
        if id is None:
            with Session(create_engine(self.connection_string)) as session:
                session.execute(insert(OperationSystemEntity).values({
                    "name": memory.name,
                    "parent_id": memory.parent_id,
                    "exchange": memory.exchange
                }))
            id = self.get_id_by_name(memory.name)
        return id



if __name__ == "__main__":
    brand = BrandRepository()
    print(brand.get_id_by_name("Apple"))
