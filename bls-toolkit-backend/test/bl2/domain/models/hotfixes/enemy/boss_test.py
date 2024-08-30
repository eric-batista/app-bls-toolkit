from src.bl2.domain.models.hotfixes.enemy.base import EnemySourceType
from src.bl2.domain.models.hotfixes.enemy.factory import EnemyFactory


def test_boss_enemy_create():
    payload = {
        "pool_id": "Test",
        "name": "Saturn",
        "code_name": "PawnBalance_LoaderGiant",
        "code_location": "Stockade_P",
        "code_population": "GD_Population_Loader",
        "code_balance_type": "Unique",
        "source_type": "BOSS",
        "location": "Stockade_P",
    }

    boss = EnemyFactory.generate(enemy_type=EnemySourceType.BOSS, **payload)

    assert boss.name == payload["name"]
    assert boss.code_name == payload["code_name"]
    assert boss.code_location == payload["code_location"]
    assert boss.code_population == payload["code_population"]
    assert boss.code_balance_type == payload["code_balance_type"]
    assert boss.source_type.value == payload["source_type"]
    assert boss.location == payload["location"]

    assert boss.create_pool_command() == "set Pool_Test BalancedItems "
    assert (
        boss.create_named_tag_command()
        == "Stockade_P,GD_Population_Loader.Balance.Unique.PawnBalance_LoaderGiant,DefaultItemPoolList,,"
    )
