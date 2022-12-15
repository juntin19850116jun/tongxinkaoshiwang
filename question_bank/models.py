from django.db import models
# 导入内建的User模型。
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField


# 博客文章数据模型
# class essay(models.Model):
#     #选择题的题目、选项、答案
#     title = models.TextField('题目',)
#     answer = models.TextField('答案')
#     analysis = models.TextField('解析')
#     tags = models.CharField('标签',max_length=20)
#
#     def __str__(self):
#         return self.title

class Tag(models.Model):
    name = models.CharField('文章标签', max_length=100)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class essay(models.Model):
    #选择题的题目、选项、答案
    title = models.TextField('题目',)
#    answer = models.TextField('答案')
    answer = UEditorField('答案', width=800, height=500,
                    toolbars="full", imagePath="upimg/", filePath="upfile/",
                    upload_settings={"imageMaxSize": 1204000},
                    settings={}, command=None, blank=True
                    )
    tags = models.ForeignKey(Tag,verbose_name='标签',on_delete=models.DO_NOTHING, blank=True,null=True)
    analysis = models.TextField('解析')
    img = models.ImageField(upload_to="upimg/%Y/%m/%d/", verbose_name='文章图片', blank=True, null=True)

    def __str__(self):
        return self.title