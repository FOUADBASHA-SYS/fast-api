# ⚡ FastAPI + PostgreSQL / SQLite Pure REST API Backend

مشروع باكد إند نقي عالي الأداء مبني باستخدام **Python FastAPI** وقاعدة بيانات **PostgreSQL / SQLite** مع نظام مصادقة وتوثيق آمن عبر **JWT (JSON Web Tokens)** و **Bcrypt** لتشفير كلمات المرور، وتوثيق تفاعلي فوري عبر **Swagger UI**.

---

## 🌟 المميزات (Features)
- 🚀 **RESTful APIs** سريعة وغير متزامنة (Asynchronous).
- 🐘 **دعم قواعد البيانات**: SQLAlchemy ORM مهيأ للعمل مع SQLite و PostgreSQL.
- 🔒 **نظام حماية ومصادقة متكامل**:
  - تشفير كلمات المرور باستخدام `bcrypt`.
  - توليد وإدارة `JWT Bearer Access Tokens`.
  - حماية المسارات بواسطة FastAPI Dependencies.
- 📖 **توثيق تفاعلي متكامل (Swagger UI & ReDoc)** متاح على `/docs` و `/redoc`.

---

## 🔌 نقاط الـ API المتاحة (API Endpoints)

| الطريقة (Method) | المسار (Endpoint) | الحماية (Auth) | الوصف |
|---|---|---|---|
| `GET` | `/` | عام (Public) | نظرة عامة وروابط الـ APIs وحالة الخادم (JSON) |
| `GET` | `/api/health` | عام (Public) | فحص سلامة وجاهزية السيرفر |
| `POST` | `/api/auth/register` | عام (Public) | تسجيل مستخدم جديد وتخزينه مشفراً |
| `POST` | `/api/auth/login` | عام (Public) | تسجيل الدخول وتوليد JWT Access Token |
| `GET` | `/api/home/me` | محمي (`Bearer Token`) | جلب بيانات حساب المستخدم الحالي |

---

## 📁 هيكل المشروع (Project Structure)

```
├── app/
│   ├── auth/                    # الأمان والمصادقة (Bcrypt + JWT + Dependencies)
│   ├── models/                  # نماذج قواعد البيانات (User Model)
│   ├── schemas/                 # مخططات Pydantic للتحقق من صحة البيانات
│   ├── routers/                 # مسارات الـ APIs (Auth, Home)
│   ├── config.py                # إعدادات التطبيق ومتغيرات البيئة
│   ├── database.py              # محرك SQLAlchemy والاتصال بقاعدة البيانات
│   └── main.py                  # نقطة انطلاق التطبيق الرئيسية
├── .env.example                 # نموذج إعدادات البيئة
├── .env                         # ملف الإعدادات المحلي
├── requirements.txt             # حزم ومكتبات المشروع
├── test_app.py                  # اختبارات شاملة لجميع الـ APIs
└── README.md                    # دليل الاستخدام
```

---

## ⚙️ تشغيل التطبيق (Run Server)

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

---

## 📖 روابط التوثيق (API Docs URLs)
- 📖 **Interactive Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- 📘 **ReDoc Documentation**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
- 🔍 **OpenAPI Schema (JSON)**: [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)
