# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import streamlit as st

# 定义计算函数
def calculate_ead(current_balance, limit):
    ead = current_balance + 0.2436 * (limit - current_balance)
    return ead

# 创建 Streamlit 应用程序
def main():
    # 设置页面标题
    st.title('EAD Calculator')

    # 添加输入框
    current_balance = st.number_input('Current Balance', value=0.0, step=1.0)
    limit = st.number_input('Limit', value=0.0, step=1.0)

    # 添加按钮，触发计算并显示结果
    if st.button('Calculate'):
        ead = calculate_ead(current_balance, limit)
        st.write(f'EAD: {ead}')

# 运行应用程序
if __name__ == '__main__':
    main()
