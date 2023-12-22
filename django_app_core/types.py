import graphene


class Money(graphene.ObjectType):
    amount = graphene.Float(description="Amount of money.", required=True)
    currency = graphene.String(description="Currency code.", required=True)

    class Meta:
        description = "Represents amount of money in specific currency."


class TaxedMoney(graphene.ObjectType):
    currency = graphene.String(description="Currency code.", required=True)
    gross = graphene.Field(
        Money, description="Amount of money including taxes.", required=True
    )
    net = graphene.Field(
        Money, description="Amount of money without taxes.", required=True
    )
    tax = graphene.Field(Money, description="Amount of taxes.", required=True)

    class Meta:
        description = (
            "Represents a monetary value with taxes. In cases where taxes were not "
            "applied, net and gross values will be equal."
        )


class TaskStatusType(graphene.ObjectType):
    done = graphene.List(graphene.String)
    error = graphene.List(graphene.String)
    in_protected = graphene.List(graphene.String)
    in_use = graphene.List(graphene.String)
    not_found = graphene.List(graphene.String)
    wait_to_do = graphene.List(graphene.String)


class TransTypeInput(graphene.InputObjectType):
    language_code = graphene.String(required=True)
