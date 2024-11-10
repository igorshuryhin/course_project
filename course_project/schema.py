import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql import GraphQLResolveInfo

from orders.models import Order, OrderCourse
from courses.models import Course


class CourseObjectType(DjangoObjectType):
    class Meta:
        model = Course
        filter_fields = ('id', 'name', 'course_price')
        interfaces = (graphene.relay.Node,)


class OrderCourseObjectType(DjangoObjectType):
    course = graphene.Field(CourseObjectType)

    class Meta:
        model = OrderCourse
        filter_fields = ('course', 'price')


class OrderObjectType(DjangoObjectType):
    order_courses = graphene.List(OrderCourseObjectType)

    def resolve_order_courses(self, info):
        return self.order_courses.all()

    class Meta:
        model = Order
        fields = ('uuid', 'user', 'total_price', 'created_at', 'updated_at', 'order_courses')


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")

    courses = DjangoFilterConnectionField(CourseObjectType)
    orders = graphene.List(OrderObjectType)

    def resolve_orders(self, info: GraphQLResolveInfo):

        queryset = Order.objects.all()

        fields = info.field_nodes[0].selection_set.selections

        for field in fields:
            if field.name.value == 'orderCourses':
                queryset = queryset.prefetch_related('order_courses')

                # Check for nested fields
                nested_fields = field.selection_set.selections

                for nested_field in nested_fields:
                    if nested_field.name.value == 'course':
                        queryset = queryset.prefetch_related('order_courses__course')
                        break

                break

        print("=" * 20)
        return queryset


schema = graphene.Schema(query=Query)
