# Excel数据可视化看板

这是一个基于Streamlit的Excel数据可视化工具，可以帮助您快速分析和可视化Excel数据。

## 功能特点

- Excel文件上传
- 数据预览
- 数值数据分布可视化
- 分类数据饼图展示
- 交互式数据筛选

## 安装步骤

1. 确保您已安装Python 3.7或更高版本
2. 安装依赖包：
   ```
   pip install -r requirements.txt
   ```

## 运行应用

在命令行中运行：
```
streamlit run app.py
```

## 使用说明

1. 启动应用后，在浏览器中打开显示的地址（通常是 http://localhost:8501）
2. 点击"浏览文件"按钮上传Excel文件
3. 上传后可以：
   - 查看数据预览
   - 选择数值列查看分布图
   - 选择分类列查看饼图
   - 使用筛选器筛选数据

## 注意事项

- 支持的Excel文件格式：.xlsx, .xls
- 建议Excel文件大小不超过100MB
- 确保Excel文件中的数据格式正确 

# 假设有这些字段
fields = ['教师姓名', '时段', '日期']

# 动态生成筛选器
filters = {}
for field in fields:
    options = df[field].dropna().unique()
    selected = st.multiselect(f"筛选 {field}", options)
    if selected:
        filters[field] = selected

# 应用所有筛选条件
filtered_df = df.copy()
for field, selected in filters.items():
    filtered_df = filtered_df[filtered_df[field].isin(selected)]

st.dataframe(filtered_df) 