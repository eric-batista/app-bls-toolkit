from typing import Union

from .base import EnemySourceType
from .bosses import BossEnemy
from .named_enemies import NamedEnemy
from .raid_bosses import RaidBossEnemy


class EnemyFactory:
    @classmethod
    def generate(cls, **kwargs) -> Union[BossEnemy, RaidBossEnemy, NamedEnemy]:
        match kwargs.get("enemy_type"):
            case EnemySourceType.BOSS:
                return BossEnemy(**kwargs)
            case EnemySourceType.RAID_BOSS:
                return RaidBossEnemy(**kwargs)
            case EnemySourceType.NAMED_ENEMY:
                return NamedEnemy(**kwargs)
            case _:
                raise
