import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql import GraphQLResolveInfo
from django.contrib.auth.models import User

from orders.models import Order, OrderCourse
from courses.models import Course
from vacancies.models import Vacancy
from awards.models import Award
from homework.models import Homework, Grade
from lesson.models import Lesson, Attendance


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


class VacancyObjectType(DjangoObjectType):
    class Meta:
        model = Vacancy
        filter_fields = ('id', 'name')
        interfaces = (graphene.relay.Node,)


class UserObjectType(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = ('id', 'username', 'email')
        interfaces = (graphene.relay.Node,)


class AwardObjectType(DjangoObjectType):
    user = graphene.Field(UserObjectType)  # Custom field for user

    class Meta:
        model = Award
        filter_fields = ('id', 'name')
        interfaces = (graphene.relay.Node,)

    def resolve_user(self, info):
        return self.user  # or `self.user_set.first()` if it's a reverse relationship


class GradeObjectType(DjangoObjectType):
    class Meta:
        model = Grade
        fields = ('id', 'user', 'grade', 'created_at')


class HomeworkObjectType(DjangoObjectType):
    grades = graphene.List(GradeObjectType)  # List of associated grades

    class Meta:
        model = Homework
        fields = (
            'id', 'name', 'deadline', 'retakes_amount', 'complexity',
            'passed_amount', 'avg_grade', 'description', 'created_at', 'updated_at', 'grades'
        )

    def resolve_grades(self, info):
        return self.grades.all()


class AttendanceObjectType(DjangoObjectType):
    class Meta:
        model = Attendance
        fields = ('id', 'user', 'lesson', 'present', 'created_at')


class LessonObjectType(DjangoObjectType):
    homework = graphene.Field(HomeworkObjectType)  # Single Homework associated with this Lesson
    attendance = graphene.List(AttendanceObjectType)  # List of Attendance records for the Lesson

    class Meta:
        model = Lesson
        fields = ('id', 'name', 'date', 'notes', 'video', 'homework', 'created_at', 'updated_at')

    def resolve_attendance(self, info):
        return self.attendance_set.all()


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")

    courses = DjangoFilterConnectionField(CourseObjectType)
    orders = graphene.List(OrderObjectType)
    awards = DjangoFilterConnectionField(AwardObjectType)
    vacancies = DjangoFilterConnectionField(VacancyObjectType)
    homeworks = graphene.List(HomeworkObjectType)
    grades = graphene.List(GradeObjectType)
    lessons = graphene.List(LessonObjectType)
    attendances = graphene.List(AttendanceObjectType)

    def resolve_orders(self, info: GraphQLResolveInfo):
        queryset = Order.objects.all()

        fields = info.field_nodes[0].selection_set.selections
        for field in fields:
            if field.name.value == 'orderCourses':
                queryset = queryset.prefetch_related('order_courses')
                nested_fields = field.selection_set.selections
                for nested_field in nested_fields:
                    if nested_field.name.value == 'course':
                        queryset = queryset.prefetch_related('order_courses__course')
                        break
                break
        return queryset

    def resolve_homeworks(self, info):
        return Homework.objects.all()

    def resolve_grades(self, info):
        return Grade.objects.all()

    def resolve_lessons(self, info):
        return Lesson.objects.all()

    def resolve_attendances(self, info):
        return Attendance.objects.all()


schema = graphene.Schema(query=Query)
