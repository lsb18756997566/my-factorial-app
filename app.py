import streamlit as st
import math
import pandas as pd
import altair as alt

# 1. 页面配置
st.set_page_config(
    page_title="✨ 超级阶乘探索器",
    page_icon="🚀",
    layout="wide"  # 使用宽屏模式，看起来更大气
)

# 2. 自定义 CSS (让标题居中且更大)
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #4CAF50;
        font-size: 3rem;
        margin-bottom: 20px;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="main-title">🚀 超级阶乘探索器</h1>', unsafe_allow_html=True)

# 3. 侧边栏输入
with st.sidebar:
    st.header("⚙️ 设置参数")
    number = st.number_input("请输入一个非负整数 (0-20)", min_value=0, max_value=20, value=5, step=1)
    st.info("💡 提示：阶乘增长极快，建议输入 20 以内的数字，否则图表会爆炸哦！")
    
    calculate_btn = st.button("开始计算", use_container_width=True)

# 4. 主区域逻辑
if calculate_btn:
    try:
        # 计算结果
        result = math.factorial(number)
        
        # 显示主要结果
        col1, col2 = st.columns([1, 2])
        with col1:
            st.metric(label=f"{number}! 的结果", value=result, delta=None)
            st.write(f"**位数**: {len(str(result))} 位")
        
        with col2:
            st.write("### 📊 阶乘增长趋势图")
            
            # 生成数据用于画图
            data = []
            for i in range(number + 1):
                data.append({"n": i, "factorial": math.factorial(i)})
            
            df = pd.DataFrame(data)
            
            # 使用 Altair 绘制交互式柱状图
            chart = alt.Chart(df).mark_bar(color='#4CAF50').encode(
                x=alt.X('n:O', title='数字 n'),
                y=alt.Y('factorial:Q', title='阶乘值 (n!)'),
                tooltip=['n', 'factorial']
            ).properties(
                height=400
            )
            
            st.altair_chart(chart, use_container_width=True)

        # 显示详细列表
        with st.expander("📜 查看详细计算过程"):
            st.dataframe(df, hide_index=True, use_container_width=True)

    except Exception as e:
        st.error(f"❌ 发生错误: {e}")
else:
    st.info("👈 请在左侧侧边栏输入数字并点击“开始计算”")

# 5. 页脚
st.markdown("---")
st.caption("Made with ❤️ by Streamlit & Python")
