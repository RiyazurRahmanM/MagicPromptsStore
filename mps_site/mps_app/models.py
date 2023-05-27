from django.db import models

# Create your models here.
class Prompts(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    no_of_prompts = models.IntegerField()
    prompt1 = models.CharField(max_length=1000,default='Null')
    sample_op_input1 = models.CharField(max_length=100,default='Null')
    prompt2 = models.CharField(max_length=1000,default='Null')
    sample_op_input2 = models.CharField(max_length=100,default='Null')
    prompt3 = models.CharField(max_length=1000,default='Null')
    sample_op_input3 = models.CharField(max_length=100,default='Null')
    prompt4 = models.CharField(max_length=1000,default='Null')
    sample_op_input4 = models.CharField(max_length=100,default='Null')
    prompt5 = models.CharField(max_length=1000,default='Null')
    sample_op_input5 = models.CharField(max_length=100,default='Null')
    prompt6 = models.CharField(max_length=1000,default='Null')
    sample_op_input6 = models.CharField(max_length=100,default='Null')
    prompt7 = models.CharField(max_length=1000,default='Null')
    sample_op_input7 = models.CharField(max_length=100,default='Null')
    prompt8 = models.CharField(max_length=1000,default='Null')
    sample_op_input8 = models.CharField(max_length=100,default='Null')
    prompt9 = models.CharField(max_length=1000,default='Null')
    sample_op_input9 = models.CharField(max_length=100,default='Null')
    prompt10 = models.CharField(max_length=1000,default='Null')
    sample_op_input10 = models.CharField(max_length=100,default='Null')


