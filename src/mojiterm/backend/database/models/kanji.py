from enum import Enum
from tortoise.models import Model
from tortoise import fields


class JLPTLevel(str, Enum):
  N5 = "N5"
  N4 = "N4"
  N3 = "N3"
  N2 = "N2"
  N1 = "N1"

class Kanji(Model):
  id = fields.IntField(pk=True)
  kanji = fields.CharField(max_length=5, unique=True, db_index=True)  # ej. "水"
  meaning = fields.TextField()  # ej. "water" / "agua"
  onyomi = fields.CharField(max_length=100)  # ej. "SUI" (lectura china)
  kunyomi = fields.CharField(max_length=100)  # ej. "mizu" (lectura japonesa)

  jlpt_level = fields.CharEnumField(JLPTLevel, default=JLPTLevel.N1)
  
  # Número de trazos (útil para la pantalla de Strokes/Radicals)
  stroke_count = fields.IntField()
  
  radical = fields.CharField(
      max_length=10, null=True
  )  # Radical principal (ej. "水" / "氵")
