# Database Models
## User Models
```python
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
	
```
## Kana Models
```python
from enum import Enum
from tortoise.models import Model
from tortoise import fields

class KanaCategory(str, Enum):
	MAIN = "main"
	DAKUON = "dakuon"
	HANDAKUON = "handakuon"
	YOON = "yoon"

class Kana(Model):
	id = fields.Intfield(pk=True)
	
	# ej. "あ", "カ", "きょ"	
	character = fields.CharField(max_length=5, unique=True) 
	romaji = fields.CharField(max_length=10) # ej. "a", "ka", "kyo"
	
	# HIRAGANA / KATAKANA
	type = fields.CharEnumField(CharacterType, db_index=True)
	
	# Para filtrar por filas/grupos en la TUI
	category = fields.CharEnumField(KanaCategory, default=KanaCategory.MAIN)
	
	# ej. "a-row", "k-row" para los checkboxes de la UI
	group_name = fields.CharField(max_length=10, null=True)
```
## Kanji Models
```python
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

  jlpt_level = fields.CharEnumField(JLPTLevel, default=JLPTLevel.N5)
  
  # Número de trazos (útil para la pantalla de Strokes/Radicals)
  stroke_count = fields.IntField()
  
  radical = fields.CharField(
      max_length=10, null=True
  )  # Radical principal (ej. "水" / "氵")
```
## Progress Models
```python
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
```

## Schema de importacion en Pydantic
```python
# backend/schemas/kanji_import.py
from typing import Any
from pydantic import BaseModel, Field, field_validator


class RawKanjiDictValue(BaseModel):
  meaning: list[str] = Field(default_factory=list)
  onyomi: list[str] = Field(default_factory=list)
  kunyomi: list[str] = Field(default_factory=list)
  nanori: list[str] | str = Field(default_factory=list)

  # Pueden venir como lista ["1"], como string " N/A " o como int
  freq: Any = None
  jlpt: Any = None

  class Config:
    extra = "ignore"

  # Validador para unificar valores que vienen como lista ["1"] o " N/A "
  @field_validator("jlpt", "freq", mode="before")
  @classmethod
  def clean_inconsistent_fields(cls, v: Any) -> str | None:
    if isinstance(v, list) and len(v) > 0:
      v = v[0]  # Extrae el valor de la lista ["1"] -> "1"

    if isinstance(v, str):
      cleaned = v.strip()
      if cleaned in ("", "N/A"):
        return None
      return cleaned

    return str(v) if v is not None else None
```
