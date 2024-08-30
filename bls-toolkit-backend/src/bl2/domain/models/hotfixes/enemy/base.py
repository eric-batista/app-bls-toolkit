import uuid
from enum import Enum

from devtools.models import Model


class EnemySourceType(str, Enum):
    NAMED_ENEMY = "NAMED_ENEMY"
    BOSS = "BOSS"
    RAID_BOSS = "RAID_BOSS"


class AbstractEnemy(Model):
    pool_id: str = str(uuid.uuid4())
    name: str
    location: str
    code_name: str
    code_location: str
    code_population: str
    code_balance_type: str | None
    source_type: EnemySourceType

    def _create_pool(self):
        return f"Pool_{self.pool_id.capitalize()}"

    def create_pool_command(self):
        return f"set {self._generate_balance_command()} "

    def _generate_balance_command(self):
        return f"{self._create_pool()} BalancedItems"

    def _generate_named_tag_command(self):
        if not self.code_balance_type:
            return f"{self.code_population}.Balance.{self.code_name}"
        return (
            f"{self.code_population}.Balance.{self.code_balance_type}.{self.code_name}"
        )

    def create_named_tag_command(self):
        return f"{self.code_location},{self._generate_named_tag_command()},DefaultItemPoolList,,"
