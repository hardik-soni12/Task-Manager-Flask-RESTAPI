from ..extensions import ma, db
from ..models.task import Task

class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task
        load_instance = True
        include_fk = True
        sqla_session = db.session
        dump_only = ('user_id', 'task_id', 'created_at')

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)