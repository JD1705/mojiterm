from tortoise.models import Model
from tortoise import fields

class UserProgress(Model):
	id = fields.IntField(pk=True)
	
	# to use in the progress bars
	hiragana_progress = fields.FloatField()
	katakana_progress = fields.FloatField()
	kanji_progress = fields.FloatField()
	
	# to use in the labels
	hiragana_level = fields.IntField()
	katakana_level = fields.IntField()
	kanji_level = fields.IntField()
	
	# statistics
	hiragana_seen = fields.IntField()
	katakana_seen = fields.IntField()
	kanji_seen = fields.IntField()
	
	# metadata
	last_session = fields.DatetimeField(db_index=True, auto_now=True)
	created_at = fields.DatetimeField(auto_now_add=True)
	
