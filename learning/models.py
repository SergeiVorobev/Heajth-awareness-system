"""Define models for learning package"""
from django.db import models
from PIL import Image
from django.utils.timezone import now
from django.contrib.auth.models import User
import random


DIFF_CHOICES = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
)

class Material(models.Model):
    """Define data for Material model"""

    title = models.CharField(max_length=100)
    img = models.ImageField(default='diabetes.png', upload_to='card_images')
    description = models.TextField()
    created_date = models.DateTimeField(default=now, editable=False)



    def __str__(self):
        return self.title
    
    # # resizing images
    def save(self, *args, **kwargs):
        """save learning cards"""

        super().save()

        image = Image.open(self.img.path)
        
        if round(image.width/image.height, 1) > 1.2:
            new_width = round(image.height * 1.2)
            new_height = image.height
            crop_l_r = round((image.width - new_width) / 2)
            image.crop((crop_l_r, 0, image.width - crop_l_r, 0))

        else:
            new_height = round(image.width / 1.2)
            new_width = image.width
            crop_t_b = round((image.height - new_height) / 2)
            image.crop((0, crop_t_b, 0, image.height - crop_t_b))

        new_img = (500, round(new_width/round(new_height/500, 2)))
        image.thumbnail(new_img)
        rgb_im = image.convert('RGB')
        rgb_im.save(self.img.path)


class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="duration of the quiz in minutes")
    required_score_to_pass = models.IntegerField(help_text="required score in %")
    difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES)

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

    class Meta:
        verbose_name_plural = 'Quizes'


class Question(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()

class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"


class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return str(self.pk)