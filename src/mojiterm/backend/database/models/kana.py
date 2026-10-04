from enum import Enum
from tortoise.models import Model
from tortoise import fields

class KanaCharacterType(str, Enum):
    HIRAGANA = "hiragana"
    KATAKANA = "katakana"

class KanaCategory(str, Enum):
	MAIN = "main"
	DAKUON = "dakuon"
	HANDAKUON = "handakuon"
	YOON = "yoon"

class Kana(Model):
    id = fields.IntField(pk=True)
	
	# ej. "あ", "カ", "きょ"	
    character = fields.CharField(max_length=5, unique=True) 
    romaji = fields.CharField(max_length=10) # ej. "a", "ka", "kyo"
	
	# HIRAGANA / KATAKANA
    type = fields.CharEnumField(KanaCharacterType, db_index=True)
	
	# Para filtrar por filas/grupos en la TUI
    category = fields.CharEnumField(KanaCategory, default=KanaCategory.MAIN)
	
	# ej. "a-row", "k-row" para los checkboxes de la UI
    group_name = fields.CharField(max_length=10, null=True)
