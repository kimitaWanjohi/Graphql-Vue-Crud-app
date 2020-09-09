import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.forms.mutation import DjangoModelFormMutation

from .models import Cpu, Company, Laptop
from .forms import LaptopForm


class CpuType(DjangoObjectType):
    class Meta:
        model = Cpu


class CompanyType(DjangoObjectType):
    class Meta:
        model = Company


class LaptopType(DjangoObjectType):
    class Meta:
        model = Laptop
        convert_choices_to_enum = False


class LaptopUpdate(DjangoModelFormMutation):
    laptop = graphene.Field(LaptopType)

    class Meta:
        form_class = LaptopForm


class LaptopCreate(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        ram = graphene.String()
        cpu_id = graphene.Int()
        company_id = graphene.Int()

    laptop = graphene.Field(LaptopType)

    def mutate(self, info, name, ram, cpu_id, company_id):
        laptop = Laptop.objects.create(name=name, ram=ram, cpu_id=cpu_id, company_id=company_id)
        laptop.save()

        return LaptopCreate(laptop=laptop)


class LaptopDelete(graphene.Mutation):
    class Arguments:
        id = graphene.Int()

    laptop = graphene.Field(LaptopType)

    def mutate(self, info,  id):
        laptop = Laptop.objects.get(pk=id).delete(None, True)


class Mutation(graphene.ObjectType):
    laptop_update = LaptopUpdate.Field()
    laptop_create = LaptopCreate.Field()
    laptop_delete = LaptopDelete.Field()


class Query(object):
    all_cpus = graphene.List(CpuType)

    all_companies = graphene.List(CompanyType)

    all_laptops = graphene.List(LaptopType)

    cpu = graphene.Field(
        CpuType,
        id=graphene.Int(),
        name=graphene.String()
    )

    company = graphene.Field(
        CompanyType,
        id=graphene.Int(),
        name=graphene.String()
    )

    laptop = graphene.Field(
        LaptopType,
        id=graphene.Int(),
        name=graphene.String()
    )


    def resolve_all_companies(self, info, **kwargs):
        return Company.objects.all()

    def resolve_all_cpus(self, info, **kwargs):
        return Cpu.objects.all()

    def resolve_all_laptops(self, info, **kwargs):
        return Laptop.objects.all()

    def resolve_cpu(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Cpu.objects.get(pk=id)

        if name is not None:
            return Cpu.objects.get(name=name)

        return None

    def resolve_company(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Company.objects.get(pk=id)

        if name is not None:
            return Company.objects.get(name=name)

        return None

    def resolve_laptop(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')
        if id is not None:
            return Laptop.objects.get(pk=id)

        if name is not None:
            return Laptop.objects.get(name=name)

        return None
