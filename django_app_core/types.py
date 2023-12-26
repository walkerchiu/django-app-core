from graphene import ResolveInfo
import graphene


class MailingAddress(graphene.ObjectType):
    slug = graphene.String(required=True)
    country_code = graphene.String(
        description="The two-letter code for the country of the address."
    )
    city = graphene.String(
        description="The name of the city, district, village, or town."
    )
    province = graphene.String(
        description="The region of the address, such as the province, state, or district."
    )
    zip = graphene.String(description="The zip or postal code of the address.")
    address1 = graphene.String(
        description="The first line of the address. Typically the street address or PO Box number."
    )
    address2 = graphene.String(
        description="The second line of the address. Typically the number of the apartment, suite, or unit."
    )
    company = graphene.String(
        description="The name of the customer's company or organization."
    )
    first_name = graphene.String(description="The first name of the user.")
    last_name = graphene.String(description="The last name of the user.")
    name = graphene.String(
        description="The full name of the user, based on firstName and lastName."
    )
    phone = graphene.String(description="A unique phone number for the user.")

    class Meta:
        description = "Represents a mailing address for customers and shipping."

    @staticmethod
    def resolve_name(root, info: ResolveInfo):
        return root.firstName + " " + root.lastName


class MailingAddressInput(graphene.InputObjectType):
    slug = graphene.String(required=True, description="Accept: billing, shipping")
    country_code = graphene.String(
        description="The two-letter code for the country of the address.\nMax length: 6"
    )
    city = graphene.String(
        description="The name of the city, district, village, or town."
    )
    province = graphene.String(
        description="The region of the address, such as the province, state, or district."
    )
    zip = graphene.String(
        description="The zip or postal code of the address.\nMax length: 6"
    )
    address1 = graphene.String(
        description="The first line of the address. Typically the street address or PO Box number."
    )
    address2 = graphene.String(
        description="The second line of the address. Typically the number of the apartment, suite, or unit."
    )
    company = graphene.String(
        description="The name of the customer's company or organization."
    )
    first_name = graphene.String(description="The first name of the user.")
    last_name = graphene.String(description="The last name of the user.")
    phone = graphene.String(
        description="A unique phone number for the user.\nMax length: 20"
    )

    class Meta:
        description = "Represents a mailing address for customers and shipping."


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
