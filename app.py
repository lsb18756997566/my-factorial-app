import streamlit as st
import math

# 设置页面标题和图标
st.set_page_config(page_title="阶乘计算器", page_icon="🧮")

# 页面大标题
st.title("🧮 超级阶乘计算器")
st.write("请输入一个非负整数，我将为你计算它的阶乘！")

# 输入框
number = st.number_input("请输入数字:", min_value=0, step=1, value=5)

# 按钮
if st.button("开始计算"):
    try:
        result = math.factorial(int(number))
        st.success(f"✅ {int(number)} 的阶乘结果是: **{result}**")
    except Exception as e:
        st.error(f"❌ 发生错误: {e}")
