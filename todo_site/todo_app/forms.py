from django.forms import ModelForm
from todo_app.models import Task, Comment, Tag

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['description']
        labels = {
            'description':'Add Task',
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        labels = {
            'body':'',
        }
    
    def __init__(self, *args, **kwargs):
        task = kwargs.pop('task_object')
        super().__init__(*args, **kwargs)
        
        self.instance.task = task
        
class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        labels = {
            'name': '',
        }
    
    def save(self, task, *args, **kwargs):
        tag_name = self.data['name']

        try:
            tag = Tag.objects.get(name=tag_name)
        except Tag.DoesNotExist:
            tag = Tag.objects.create(name=tag_name)

        task.tags.add(tag)
