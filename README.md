# Glitch775-Hand-Tracking-Mouse-Control-Application

تطبيق التحكم بالماوس بتقنية تتبع اليد
الوصف
هذا التطبيق بلغة بايثون يستخدم تقنية تتبع اليد للتحكم في حركة الماوس ومحاكاة النقرات باستخدام موقع إصبع السبابة للمستخدم. يعتمد على مكتبة cvzone لاكتشاف اليدين ومكتبة pyautogui للتحكم في الماوس، مما يوفر وسيلة خالية من اليدين للتفاعل مع جهاز الكمبيوتر الخاص بك.

الميزات
تتبع اليد: يستخدم التطبيق كاميرا الويب لاكتشاف يد المستخدم وتتبع موقع إصبع السبابة.
حركة الماوس: يتحكم موقع إصبع السبابة في مؤشر الماوس على الشاشة، مما يوفر تنقلًا سلسًا وبديهيًا.
محاكاة النقر: يمكن للمستخدم النقر على العناصر باستخدام وضع إصبع الإبهام، مما يحاكي تجربة النقر بالماوس.


Description
This Python application leverages hand tracking technology to control mouse movements and simulate clicks using the position of the user's index finger. It employs the cvzone library for hand detection and the pyautogui library for mouse control, providing a hands-free way to interact with your computer.

Features
Hand Tracking: The application uses a webcam to detect the user's hand and track the position of the index finger.
Mouse Movement: The position of the index finger controls the mouse cursor on the screen, providing smooth and intuitive navigation.
Click Simulation: The application simulates a mouse click when the user's thumb is pressed down in relation to the index finger, allowing for easy file opening.
File Selection: At the start of the application, a file dialog prompts the user to select any file (such as documents, images, etc.) to be opened when clicked.
Real-time Feedback: Visual feedback is provided on the screen, indicating the position of the index finger and guiding the user on how to interact with the application.
Dependencies
To run this application, make sure you have the following Python packages installed:

cv2 (OpenCV)
pyautogui
cvzone
tkinter (usually comes pre-installed with Python)
Usage
Ensure your webcam is functional and accessible.
Run the script in your preferred Python environment.
Select a file to open from the file dialog that appears.
Move your index finger in front of the webcam to control the mouse cursor.
Simulate a click by pressing your thumb down near your index finger to open the selected file.
Note
Ensure that the file path you select is valid and that the file exists on your system to avoid errors during opening.
Press 'q' to quit the application.
