from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

# 환경 변수에서 데이터베이스 URL 가져오기
FOLDER_DATABASE_URL = os.getenv("FOLDER_DATABASE_URL", "mysql+pymysql://root:password@localhost:3306/folder")
FILE_DATABASE_URL = os.getenv("FILE_DATABASE_URL", "mysql+pymysql://root:password@localhost:3306/file")
USER_DATABASE_URL = os.getenv("USER_DATABASE_URL", "mysql+pymysql://root:password@localhost:3306/user")
QUIZ_DATABASE_URL = os.getenv("QUIZ_DATABASE_URL", "mysql+pymysql://root:password@localhost:3306/quiz")
RETRY_DATABASE_URL = os.getenv("RETRY_DATABASE_URL", "mysql+pymysql://root:password@localhost:3306/retry")

# 엔진 생성
folder_engine = create_engine(FOLDER_DATABASE_URL, echo=False)
file_engine = create_engine(FILE_DATABASE_URL, echo=False)
user_engine = create_engine(USER_DATABASE_URL, echo=False)
quiz_engine = create_engine(QUIZ_DATABASE_URL, echo=False)
retry_engine = create_engine(RETRY_DATABASE_URL, echo=False)

# 세션 로컬 생성
FolderSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=folder_engine)
FileSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=file_engine)
UserSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=user_engine)
QuizSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=quiz_engine)
RetrySessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=retry_engine)

# 베이스 클래스 정의
class FolderBase(DeclarativeBase):
    pass

class FileBase(DeclarativeBase):
    pass

class UserBase(DeclarativeBase):
    pass

class QuizBase(DeclarativeBase):
    pass

class RetryBase(DeclarativeBase):
    pass

# 세션 의존성 함수 정의
def get_folderdb():
    db = FolderSessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_filedb():
    db = FileSessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_userdb():
    db = UserSessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_quizdb():
    db = QuizSessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_retrydb():
    db = RetrySessionLocal()
    try:
        yield db
    finally:
        db.close()

# 데이터베이스 초기화 함수
def init_databases():
    from models import User, Quiz, Retry
    UserBase.metadata.create_all(bind=user_engine)
    QuizBase.metadata.create_all(bind=quiz_engine)
    RetryBase.metadata.create_all(bind=retry_engine)
