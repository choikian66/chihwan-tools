import logging
from pathlib import Path

from utils.db import _get_conn

logger = logging.getLogger(__name__)

_SCHEMA_PATH = Path(__file__).parent.parent / "schema.sql"


def run_migrations():
    if not _SCHEMA_PATH.exists():
        logger.warning(f"schema.sql 없음: {_SCHEMA_PATH}")
        return
    schema_sql = _SCHEMA_PATH.read_text(encoding="utf-8")
    try:
        conn = _get_conn()
        with conn:
            with conn.cursor() as cur:
                cur.execute(schema_sql)
        conn.close()
        logger.info("마이그레이션 완료 ✓")
    except Exception as e:
        logger.error(f"마이그레이션 실패 — {e}")
