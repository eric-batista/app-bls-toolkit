from enum import Enum

from devtools.models import Model


class ItemPoolType(str, Enum):
    DEFAULT = "KeyedItemPoolDefinition"
    DEFINITION = "ItemPoolDefinition"


class AttributeDefinition(Model):
    attr_root: str
    attr_type: str
    attr_name: str

    def get_attr_name(self):
        return (
            f"AttributeDefinition'{self.attr_root}.{self.attr_type}.{self.attr_name}'"
        )


class AttributeInitializationDefinition(Model):
    attr_root: str | None = "GD_Balance"
    attr_type: str | None = "Weighting"
    attr_name: str | None = "Weight_1_Common"

    def get_attr_init_name(self) -> str:
        if not all([self.attr_name, self.attr_root, self.attr_type]):
            return "None"
        return f"AttributeInitializationDefinition'{self.attr_root}.{self.attr_type}.{self.attr_name}'"


class ItemPool(Model):
    pool_type: ItemPoolType = ItemPoolType.DEFAULT
    pool_name: str
    pool_root: str = "GD_Itempools.Runnables"

    def get_pool_type(self):
        return f"ItemPool={self.pool_type}'{self.pool_root}.{self.pool_name}'"


class ItemPoolProbability(Model):
    base_value_constant: str = "0.000000"
    base_attribute: AttributeDefinition
    initialization_definition: AttributeInitializationDefinition = (
        AttributeInitializationDefinition(
            **{"attr_root": None, "attr_name": None, "attr_type": None}
        )
    )
    base_value_scale_constant: str = "1.000000"

    def get_item_pool_probability(self):
        return f"PoolProbability=(BaseValueConstant={self.base_value_constant},BaseValueAttribute={self.base_attribute.get_attr_name()},InitializationDefinition={self.initialization_definition.get_attr_init_name()},BaseValueScaleConstant={self.base_value_scale_constant})"


class ItemPoolInvBalanceDefinition(Model):
    item_pool_definition_root: str
    item_pool_definition_type: str
    item_pool_definition_name: str

    def get_balance_definition(self):
        return f"WeaponBalanceDefinition'{self.item_pool_definition_root}.{self.item_pool_definition_type}.{self.item_pool_definition_name}'"


class ItemPoolDefinitionProbability(ItemPoolProbability):
    def get_item_pool_probability(self):
        return f"(BaseValueConstant={self.base_value_constant},BaseValueAttribute=None,InitializationDefinition={self.initialization_definition.get_attr_init_name()},BaseValueScaleConstant={self.base_value_scale_constant})"


class ItemPoolDefinition(Model):
    inv_balance_definition: ItemPoolInvBalanceDefinition
    probability: ItemPoolDefinitionProbability

    def get_item_pool_definition(self):
        return f"(ItmPoolDefinition=None,InvBalanceDefinition={self.inv_balance_definition.get_balance_definition()},Probability={self.probability.get_item_pool_probability()},bDropOnDeath=True)"
