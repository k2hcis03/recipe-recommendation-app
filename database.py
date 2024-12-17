import sqlite3
import os

def init_db():
    # 기존 데이터베이스 파일이 있다면 삭제
    if os.path.exists('recipes.db'):
        os.remove('recipes.db')
    
    conn = sqlite3.connect('recipes.db')
    c = conn.cursor()
    
    # 레시피 테이블 생성 (image_url 필드 포함)
    c.execute('''CREATE TABLE IF NOT EXISTS recipes
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  purpose TEXT NOT NULL,
                  ingredients TEXT NOT NULL,
                  instructions TEXT NOT NULL,
                  image_url TEXT)''')
    
    # 샘플 데이터 추가 (이미지 URL 포함)
    sample_recipes = [
        ('닭가슴살 샐러드', '다이어트', '닭가슴살, 양상추, 방울토마토, 올리브오일',
         '1. 닭가슴살을 삶아서 식힌다\n2. 야채를 씻어 손질한다\n3. 모든 재료를 섞어 드레싱을 뿌린다',
         'https://images.unsplash.com/photo-1546069901-ba9599a7e63c'),
        ('연어 스테이크', '건강', '연어, 레몬, 올리브오일, 로즈마리',
         '1. 연어에 올리브오일을 바른다\n2. 레몬과 로즈마리를 올려 구운다',
         'https://images.unsplash.com/photo-1467003909585-2f8a72700288'),
        ('초콜릿 케이크', '기념일', '밀가루, 달걀, 초콜릿, 우유',
         '1. 반죽을 만든다\n2. 오븐에 굽는다\n3. 초콜릿 장식을 한다',
         'https://images.unsplash.com/photo-1578985545062-69928b1d9587')
    ]
    
    c.executemany('INSERT INTO recipes (name, purpose, ingredients, instructions, image_url) VALUES (?, ?, ?, ?, ?)',
                  sample_recipes)
    
    conn.commit()
    conn.close()

def get_recipes_by_purpose(purpose):
    conn = sqlite3.connect('recipes.db')
    c = conn.cursor()
    c.execute('SELECT * FROM recipes WHERE purpose = ?', (purpose,))
    recipes = c.fetchall()
    conn.close()
    return recipes