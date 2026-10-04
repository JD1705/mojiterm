from enum import Enum
from tortoise.models import Model
from tortoise import fields

class CharacterType(str, Enum):
  HIRAGANA = "hiragana"
  KATAKANA = "katakana"
  KANJI = "kanji"

class CharacterProgress(Model):
  id = fields.IntField(pk=True)

  # Character of this review/progress (ex. "a", "ka", "木", etc.)
  character_code = fields.CharField(max_length=10, db_index=True)
  
  # 'hiragana', 'katakana', 'kanji'
  character_type = fields.CharEnumField(
	  CharacterType,
	  max_length=10,
	  db_index=True
	)

  # Card statistics
  times_reviewed = fields.IntField(default=0)  # Times practiced
  times_correct = fields.IntField(default=0)  # Correct
  times_failed = fields.IntField(default=0)  # Misses

  # Para el algoritmo de Repetición Espaciada (SRS)
  streak = fields.IntField(default=0)  # Racha actual de aciertos
  ease_factor = fields.FloatField(default=2.5)  # Dificultad para el algoritmo
  next_review = fields.DatetimeField(null=True)  # Próxima fecha de práctica
  
  
class ReviewHistory(Model):
  id = fields.IntField(pk=True)

  # Tipo de carácter que se practicó
  character_code = fields.CharField(max_length=10, db_index=True)
  character_type = fields.CharEnumField(CharacterType)

  # Resultado de esta respuesta individual
  was_correct = fields.BooleanField()  # True si acertó, False si falló
  response_time_ms = fields.IntField(
      null=True
  )  # Tiempo que tardó en responder (en milisegundos)

  timestamp = fields.DatetimeField(auto_now_add=True, db_index=True)
