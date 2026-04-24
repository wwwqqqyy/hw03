# 人脸识别系统（HW03）
基于 OpenCV + Streamlit 实现的人脸检测 Web 应用，解决 dlib 编译问题，Windows 环境可直接运行。

## 项目结构
hw03/
├── app.py # 主程序：Streamlit 界面 + OpenCV 人脸检测逻辑
├── requirements.txt # 项目依赖库版本
└── README.md # 项目说明文档

## 功能说明
1.  **人脸检测**：上传图片后自动检测所有人脸，用蓝色框标注位置。
2.  **Web 界面**：使用 Streamlit 搭建，支持图片上传、结果可视化。

## 环境准备
1.  安装 Python 3.10+
2.  安装依赖：
    ```bash
    pip install -r requirements.txt访问 http://localhost:8501 即可使用。