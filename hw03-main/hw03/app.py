import streamlit as st
import cv2
import numpy as np
from PIL import Image

# 页面标题
st.title("🤖 人脸识别系统（HW03）")
st.subheader("基于 OpenCV + Streamlit")

# 上传图片
uploaded_file = st.file_uploader("上传人脸图片", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # 读取并转换图片
    img = Image.open(uploaded_file)
    img_np = np.array(img)
    img_rgb = img_np.copy()

    # 加载OpenCV人脸检测器（内置，无需额外安装）
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # 转灰度图检测
    gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

    # 绘制人脸框
    for (x, y, w, h) in faces:
        cv2.rectangle(img_rgb, (x, y), (x+w, y+h), (255, 0, 0), 3)

    # 展示结果
    st.image(img_rgb, caption=f"检测到 {len(faces)} 张人脸", use_column_width=True)
    st.success(f"✅ 检测完成，共识别到 {len(faces)} 张人脸")
else:
    st.info("请上传一张包含人脸的图片开始检测")