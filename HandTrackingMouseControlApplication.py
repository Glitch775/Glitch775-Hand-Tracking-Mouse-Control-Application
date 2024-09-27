import cv2
import pyautogui
import os
from cvzone.HandTrackingModule import HandDetector
import tkinter as tk
from tkinter import filedialog

# إعداد Mediapipe
detector = HandDetector(detectionCon=0.8)
cap = cv2.VideoCapture(0)

# إعداد متغيرات للتحكم في الماوس
previous_x, previous_y = 0, 0
smoothing = 0.5  # تسريع الحركة
is_clicking = False  # حالة النقر
selected_file = None  # متغير لتخزين الملف المحدد

# دالة لاختيار ملف
def select_file():
    global selected_file
    root = tk.Tk()
    root.withdraw()  # إخفاء نافذة tkinter الرئيسية
    selected_file = filedialog.askopenfilename()  # اختيار ملف
    if selected_file:
        print(f"تم اختيار الملف: {selected_file}")

# اختيار الملف عند بدء البرنامج
select_file()

while True:
    success, img = cap.read()
    if not success:
        print("فشل في قراءة الكاميرا.")
        break
    
    img = cv2.flip(img, 1)  # عكس الصورة
    hands, img = detector.findHands(img)  # تحديد مواقع اليدين

    if hands:
        # الحصول على موقع إصبع السبابة
        index_finger_tip = hands[0]["lmList"][8]  # الحصول على إحداثيات النقطة 8 (إصبع السبابة)
        
        # طباعة القيم لتفحصها
        print("index_finger_tip:", index_finger_tip)  

        if len(index_finger_tip) >= 2:
            index_x, index_y = index_finger_tip[0], index_finger_tip[1]  # استخدام أول قيمتين
            
            # حساب المسافة للحركة
            distance_x = index_x - previous_x
            distance_y = index_y - previous_y
            
            # تحريك الماوس
            new_x = previous_x + distance_x * smoothing
            new_y = previous_y + distance_y * smoothing
            
            pyautogui.moveTo(new_x, new_y)

            # رسم دائرة حول إصبع السبابة
            cv2.circle(img, (int(new_x), int(new_y)), 15, (255, 0, 255), cv2.FILLED)

            # تحديث الإحداثيات السابقة
            previous_x, previous_y = new_x, new_y

            # تحقق من الضغط
            if hands[0]["lmList"][4][1] < index_y < hands[0]["lmList"][3][1]:  # التحقق من وجود إبهام مغلق
                if not is_clicking:
                    is_clicking = True
                    pyautogui.click()
                    print("نقر!")

                    # فتح الملف المحدد
                    if selected_file and os.path.exists(selected_file):
                        os.startfile(selected_file)  # فتح الملف المحدد
                    else:
                        print("الملف المحدد غير موجود.")
            else:
                is_clicking = False

    # إضافة نص لتوجيه المستخدم
    cv2.putText(img, "قم بتحريك إصبع السبابة, انقر لفتح الملف", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow("Hand Tracking", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
