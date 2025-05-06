import streamlit as st
import pandas as pd

# 设置页面配置
st.set_page_config(
    page_title="教师时段使用明细多字段筛选",
    page_icon="📊",
    layout="wide"
)

# 标题
st.title("教师时段使用明细多字段筛选")

# 文件上传
uploaded_file = st.file_uploader("请上传Excel文件（需包含'教师时段使用明细'工作表）", type=['xlsx', 'xls'])

if uploaded_file is not None:
    # 只读取指定工作表
    df = pd.read_excel(uploaded_file, sheet_name='教师时段使用明细', skiprows=2)

    st.subheader("多字段筛选")
    filters = {}
    cols = st.columns(4)  # 每行4个筛选器
    for idx, col in enumerate(df.columns):
        options = df[col].dropna().unique()
        if len(options) > 50:
            continue
        with cols[idx % 4]:
            selected = st.multiselect(f"筛选 {col}", options)
            if selected:
                filters[col] = selected

    # 应用所有筛选条件
    filtered_df = df.copy()
    for col, selected in filters.items():
        filtered_df = filtered_df[filtered_df[col].isin(selected)]

    st.subheader("筛选结果")
    st.dataframe(filtered_df) 