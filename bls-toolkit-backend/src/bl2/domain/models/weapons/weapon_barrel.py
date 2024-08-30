from abc import abstractmethod
from enum import Enum
from typing import List

from devtools.models import Model

from src.bl2.domain.models.weapons import WeaponManufacturer, exceptions


class WeaponType(str, Enum):
    SMG = "SMG"
    ASSAULT_RIFLE = "ASSAULT_RIFLE"
    SNIPER = "SNIPER"
    ROCKER_LAUNCHER = "ROCKER_LAUNCHER"
    PISTOL = "PISTOL"
    SHOTGUN = "SHOTGUN"


class WeaponAttrs(Model):
    manufacturer: WeaponManufacturer
    attrs: List[str]


class WeaponBarrel(Model):
    def __init__(self, weapon_type: WeaponType, weapon_attrs: WeaponAttrs):
        self._weapon_type = weapon_type
        self._weapon_attrs = weapon_attrs

    @abstractmethod
    def acquire_weapon_barrel_type(self) -> str:
        return self._weapon_type

    @abstractmethod
    def acquire_barrel_status(self) -> List:
        return self._weapon_attrs.attrs


class SMGWeaponBarrel(WeaponBarrel):
    def __init__(self, weapon_attrs: WeaponAttrs):
        super().__init__(WeaponType.SMG, weapon_attrs)


class AssaultRifleWeaponBarrel(WeaponBarrel):
    def __init__(self, weapon_attrs: WeaponAttrs):
        super().__init__(WeaponType.ASSAULT_RIFLE, weapon_attrs)


class RocketLauncherWeaponBarrel(WeaponBarrel):
    def __init__(self, weapon_attrs: WeaponAttrs):
        super().__init__(WeaponType.ROCKER_LAUNCHER, weapon_attrs)


class ShotgunWeaponBarrel(WeaponBarrel):
    def __init__(self, weapon_attrs: WeaponAttrs):
        super().__init__(WeaponType.SHOTGUN, weapon_attrs)


class SniperWeaponBarrel(WeaponBarrel):
    def __init__(self, weapon_attrs: WeaponAttrs):
        super().__init__(WeaponType.SNIPER, weapon_attrs)


class WeaponBarrelFactory:
    @classmethod
    def create(cls, *args):
        match args[0]:
            case WeaponType.SMG:
                return SMGWeaponBarrel(args[1])
            case WeaponType.ASSAULT_RIFLE:
                return AssaultRifleWeaponBarrel(args[1])
            case WeaponType.ROCKER_LAUNCHER:
                return RocketLauncherWeaponBarrel(args[1])
            case WeaponType.SHOTGUN:
                return ShotgunWeaponBarrel(args[1])
            case _:
                raise exceptions.InvalidWeaponType()
