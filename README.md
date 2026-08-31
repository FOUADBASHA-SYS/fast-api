# ⚡ FastAPI + PostgreSQL Authentication Portal

تطبيق ويب متكامل عالي الأداء مبني باستخدام **Python FastAPI** وقاعدة بيانات **PostgreSQL** مع نظام مصادقة آمن باستخدام **JWT (JSON Web Tokens)** و **Bcrypt** لتشفير كلمات المرور، وواجهات أمامية تفاعلية وعصرية.

---

## 🌟 المميزات (Features)
- 🚀 **أداء فائق وغير متزامن (High-Performance Async Backend)** باستخدام FastAPI و Uvicorn.
- 🐘 **قاعدة بيانات PostgreSQL** عبر SQLAlchemy ORM مع دعم التحقق التلقائي من الجداول.
- 🔒 **مصادقة آمنة 100%**:
  - تشفير كلمات المرور باستخدام `bcrypt`.
  - توليد `JWT Bearer Access Tokens`.
- 🎨 **واجهات مستخدم تفاعلية وعصرية (Modern Glassmorphism UI)**:
  - **الصفحة الرئيسية (`/`)**: تعرض مميزات النظام ونقاط الـ API، وتتحول تلقائياً إلى لوحة تحكم تعرض بيانات المستخدم عند تسجيل الدخول.
  - **صفحة تسجيل الدخول (`/login`)**: نموذج دخول سريع وتفاعلي مع إمكانية الدخول باسم المستخدم أو البريد الإلكتروني.
  - **صفحة إنشاء الحساب (`/register`)**: نموذج إنشاء حساب مع فحص فوري للحقول وتوجيه تلقائي.
- 📖 **توثيق تفاعلي فوري (Interactive Swagger Docs)** متاح على `/docs`.

---

## 🔌 نقاط الـ API الأساسية (The 3 Core APIs)

| # | الطريقة (Method) | المسار (Endpoint) | الحماية (Auth) | الوصف |
|---|---|---|---|---|
| 1 | `POST` | `/api/auth/register` | عام (Public) | تسجيل مستخدم جديد في قاعدة البيانات |
| 2 | `POST` | `/api/auth/login` | عام (Public) | التحقق من بيانات المستخدم وإصدار JWT Token |
| 3 | `GET` | `/api/home/me` | محمي (Bearer Token) | جلب بيانات المستخدم المسجل وإحصائيات الرئيسية |

بالإضافة لمسار فحص حالة السيرفر: `GET /api/health`.

---

## 📁 هيكل المشروع (Project Structure)

```
├── app/
│   ├── auth/                    # الأمان والمصادقة (Bcrypt + JWT + Dependencies)
│   ├── models/                  # نماذج قواعد البيانات (User Model)
│   ├── schemas/                 # مخططات Pydantic للتحقق من صحة البيانات
│   ├── routers/                 # مسارات الـ APIs وصفحات الويب
│   ├── templates/               # قوالب Jinja2 HTML (Home, Login, Register)
│   ├── static/                  # ملفات CSS والتصميم و JavaScript التفاعلية
│   ├── config.py                # إعدادات التطبيق ومتغيرات البيئة
│   ├── database.py              # محرك SQLAlchemy والاتصال بـ PostgreSQL
│   └── main.py                  # نقطة انطلاق التطبيق الرئيسية
├── .env.example                 # نموذج إعدادات البيئة
├── .env                         # ملف الإعدادات المحلي
├── requirements.txt             # متطلبات ومكتبات المشروع
└── README.md                    # دليل الاستخدام
```

---

## ⚙️ متطلبات التشغيل والتثبيت (Setup & Installation)

### 1. تثبيت الحزم والمكتبات
```bash
pip install -r requirements.txt
```

### 2. إعداد قاعدة بيانات PostgreSQL
قم بإنشاء قاعدة بيانات باسم `fastapi_db` في PostgreSQL:
```sql
CREATE DATABASE fastapi_db;
```

ثم قم بضبط بيانات الاتصال في ملف `.env`:
```ini
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/fastapi_db
SECRET_KEY=your_super_secret_jwt_key
```

*(ملاحظة: إذا أردت تجربة التطبيق فوراً بدون تشغيل PostgreSQL محلياً، يمكنك استخدام SQLite مؤقتاً عبر وضع `DATABASE_URL=sqlite:///./test.db` في ملف `.env`)*

### 3. تشغيل خادم التطبيق (Run Server)
```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

---

## 🌐 روابط الوصول (Application URLs)
- 🏠 **الصفحة الرئيسية**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- 🔑 **صفحة تسجيل الدخول**: [http://127.0.0.1:8000/login](http://127.0.0.1:8000/login)
- ✨ **صفحة إنشاء الحساب**: [http://127.0.0.1:8000/register](http://127.0.0.1:8000/register)
- 📖 **توثيق Swagger API**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
