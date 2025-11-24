import os
import platform
from datetime import datetime
from typing import List, Optional
from translate import Translator
from gtts import gTTS
from dotenv import load_dotenv
from db import get_conn

load_dotenv()

AUDIO_DIR = os.path.join(os.path.dirname(__file__), "audio")
os.makedirs(AUDIO_DIR, exist_ok=True)

class Blog:
    def __init__(self, title: str, content: str, id: Optional[int] = None,
                 created_at: Optional[datetime] = None, updated_at: Optional[datetime] = None):
        self.id = id
        self.title = title
        self.content = content
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

    def save(self):
        """
        Insert this blog into the DB and update self.id / timestamps.
        """
        sql = """
        INSERT INTO blogs (title, content)
        VALUES (%s, %s)
        RETURNING id, created_at, updated_at;
        """
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (self.title, self.content))
                row = cur.fetchone()
                if row:
                    self.id = row["id"]
                    self.created_at = row["created_at"]
                    self.updated_at = row["updated_at"]
        return self

    def update(self):
        """
        Update title/content and updated_at in DB. Requires self.id.
        """
        if not self.id:
            raise ValueError("Cannot update blog without id.")
        sql = """
        UPDATE blogs
        SET title = %s, content = %s, updated_at = NOW()
        WHERE id = %s
        RETURNING updated_at;
        """
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (self.title, self.content, self.id))
                row = cur.fetchone()
                if row:
                    self.updated_at = row["updated_at"]
        return self

    def delete(self):
        """
        Delete blog from DB.
        """
        if not self.id:
            raise ValueError("Cannot delete blog without id.")
        sql = "DELETE FROM blogs WHERE id = %s;"
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (self.id,))
        return True


    @staticmethod
    def get_by_id(blog_id: int) -> Optional["Blog"]:
        sql = "SELECT id, title, content, created_at, updated_at FROM blogs WHERE id = %s;"
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (blog_id,))
                row = cur.fetchone()
                if not row:
                    return None
                return Blog(
                    id=row["id"],
                    title=row["title"],
                    content=row["content"],
                    created_at=row["created_at"],
                    updated_at=row["updated_at"]
                )

    @staticmethod
    def get_all() -> List["Blog"]:
        sql = "SELECT id, title, content, created_at, updated_at FROM blogs ORDER BY created_at DESC;"
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                rows = cur.fetchall()
                blogs = []
                for r in rows:
                    blogs.append(Blog(
                        id=r["id"],
                        title=r["title"],
                        content=r["content"],
                        created_at=r["created_at"],
                        updated_at=r["updated_at"]
                    ))
                return blogs

    def translate_and_speak(self, source: str = "auto", target: str = "en", speak: bool = False):
        """
        Translate the blog content and generate TTS audio of the translated text.
        Returns a dict: {"translated_text": ..., "audio_file": <path> or None}
        """
        if not self.content:
            raise ValueError("No content to translate")

       
        translator = Translator(from_lang=source, to_lang=target)
        translated = translator.translate(self.content)

        translated_text = str(translated)
        filename = f"blog_{self.id or 'new'}_audio.mp3"
        filepath = os.path.join(AUDIO_DIR, filename)

        try:
            tts = gTTS(text=translated_text, lang=target)
            tts.save(filepath)
        except Exception as e:
            try:
                tts = gTTS(text=translated_text, lang="en")
                filepath = os.path.join(AUDIO_DIR, f"blog_{self.id or 'new'}_audio_fallback_en.mp3")
                tts.save(filepath)
            except Exception as e2:
                return {"translated_text": translated_text, "audio_file": None, "error": str(e2)}

        if speak:
            try:
                sys_platform = platform.system()
                if sys_platform == "Darwin":  # macOS
                    os.system(f"afplay {filepath}")
                elif sys_platform == "Linux":
                    # mpg123 might not be installed
                    os.system(f"mpg123 {filepath}")
                elif sys_platform == "Windows":
                    os.system(f"start {filepath}")
            except Exception:
                pass

        return {"translated_text": translated_text, "audio_file": filepath}
