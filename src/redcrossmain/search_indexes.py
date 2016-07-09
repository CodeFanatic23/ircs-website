import datetime
from haystack import indexes
from .models import *

class RedcrossIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True,use_template=True)
	date = indexes.DateTimeField(model_attr='date')

	content_auto = indexes.EdgeNgramField(model_attr='title')

	def get_model(self):
		return Post

	def index_queryset(self,using=None):
		"""Used when the entire index for model is updated"""

		return self.get_model().objects.all()