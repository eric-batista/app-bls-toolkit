from devtools.models import Model

from src.bl2.domain.models.weapons import (
    WeaponAttrs,
    WeaponBarrelFactory,
    WeaponManufacturer,
    WeaponType,
)


class BarrelGenerator(Model):
    @classmethod
    def _attrs(cls, weapon_type: WeaponType, weapon_manufacturer: WeaponManufacturer):
        _mapping_weapon = {
            WeaponType.SMG: {
                WeaponManufacturer.DAHL: WeaponAttrs(
                    manufacturer=WeaponManufacturer.DAHL, attrs=["+recoil_reduction"]
                ),
                WeaponManufacturer.MALIWAN: WeaponAttrs(
                    manufacturer=WeaponManufacturer.MALIWAN,
                    attrs=[
                        "+elemental_status_damage",
                        "+elemental_status_chance",
                        "+accuracy",
                    ],
                ),
            }
        }

    @classmethod
    def generate(cls, weapon_type: WeaponType, weapon_manufacturer: WeaponManufacturer):
        return WeaponBarrelFactory.create(
            weapon_type, cls._attrs(weapon_type, weapon_manufacturer)
        )
