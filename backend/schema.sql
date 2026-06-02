-- 80점 경영 진단
CREATE TABLE IF NOT EXISTS branch_diagnosis (
    id          SERIAL PRIMARY KEY,
    branch_name TEXT NOT NULL,
    diagnosed_at DATE NOT NULL DEFAULT CURRENT_DATE,
    achieved    BOOLEAN NOT NULL DEFAULT FALSE,
    note        TEXT,
    created_by  TEXT
);

CREATE TABLE IF NOT EXISTS diagnosis_items (
    id            SERIAL PRIMARY KEY,
    diagnosis_id  INTEGER NOT NULL REFERENCES branch_diagnosis(id) ON DELETE CASCADE,
    category      TEXT NOT NULL,
    sub_category  TEXT NOT NULL,
    item_text     TEXT NOT NULL,
    sort_order    INTEGER NOT NULL DEFAULT 0,
    checked       BOOLEAN NOT NULL DEFAULT FALSE,
    link          TEXT NOT NULL DEFAULT '',
    note          TEXT NOT NULL DEFAULT '',
    담당자        TEXT NOT NULL DEFAULT '',
    개선예정일    TEXT NOT NULL DEFAULT ''
);

-- 경영 매뉴얼 챗봇 캐시
CREATE TABLE IF NOT EXISTS manual_cache (
    id         TEXT PRIMARY KEY,
    title      TEXT,
    category1  TEXT,
    category2  TEXT,
    content    TEXT,
    updated_at TIMESTAMP DEFAULT NOW()
);
