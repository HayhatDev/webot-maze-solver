# 🤖 Maze Solver Robot / روبوت حل المتاهة

[English](#english) | [العربية](#arabic)

---

<a name="english"></a>
## English Version

### 📝 Description
A robot that solves a maze using the **Left-Hand Rule** algorithm, developed with Webots and Python. The robot keeps its left hand on the wall at all times, which guarantees exiting any simply connected maze.

### ✨ Features
- Follows the left wall continuously
- Avoids frontal collisions
- Handles dead ends and intersections
- Works in a custom-designed maze

### 🛠️ Technologies
- Webots R2025a
- Python
- Webots Controller API
- Distance sensors (ps1, ps7)

### 🎮 How to Run
1. Open `maze.wbt` in Webots
2. Select `maze_solver.py` as the robot controller
3. Press Run ▶️

### 🧠 Algorithm (Left-Hand Rule)
if front wall detected → turn right
else if no left wall → turn left
else → move forward

### 📁 Project Files
- `maze.wbt` - The maze world file
- `maze_solver.py` - Python controller code

### 🎥 Demo Video
(https://youtu.be/98hUGgJHHpc)

### 👨‍💻 Author
Hayhat Tahir

### 📄 License
MIT License

---

<a name="arabic"></a>
## النسخة العربية

### 📝 الوصف
روبوت يحل المتاهة باستخدام خوارزمية **قاعدة اليد اليسرى**، تم تطويره باستخدام Webots و Python. يحافظ الروبوت على يده اليسرى على الجدار طوال الوقت، مما يضمن خروجه من أي متاهة متصلة الجدران.

### ✨ الميزات
- يتبع الجدار على يساره باستمرار
- يتجنب الاصطدام بالجدران الأمامية
- يتعامل مع الطرق المسدودة والمفترقات
- يعمل في متاهة مصممة خصيصاً

### 🛠️ التقنيات المستخدمة
- Webots R2025a
- Python
- Webots Controller API
- حساسات المسافة (ps1, ps7)

### 🎮 كيفية التشغيل
1. افتح ملف `maze.wbt` في Webots
2. اختر `maze_solver.py` كـ controller للروبوت
3. اضغط زر التشغيل ▶️

### 🧠 الخوارزمية (قاعدة اليد اليسرى)
إذا كان هناك جدار أمامي → لف يمين
وإلا إذا لم يكن هناك جدار على اليسار → لف يسار
وإلا → تحرك للأمام


### 📁 ملفات المشروع
- `maze.wbt` - ملف عالم المتاهة
- `maze_solver.py` - كود التحكم بلغة Python

### 🎥 فيديو توضيحي
https://youtu.be/98hUGgJHHpc

### 👨‍💻 المؤلف
Hayhat Tahir

### 📄 الترخيص
MIT License
