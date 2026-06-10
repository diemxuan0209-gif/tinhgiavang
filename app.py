import streamlit as st

st.set_page_config(
    page_title="Giá Vàng Thế Giới",
    layout="centered"
)

st.title("🌍 App Tính Giá Vàng Thế Giới")

# Giá vàng thế giới (USD/ounce)
gold_price = st.number_input(
    "Giá vàng thế giới (USD/ounce)",
    min_value=0.0,
    value=3400.0
)

# Tỷ giá USD/VND
exchange_rate = st.number_input(
    "Tỷ giá USD/VND",
    min_value=0.0,
    value=26000.0
)

# Số gram vàng
grams = st.number_input(
    "Khối lượng vàng (gram)",
    min_value=0.0,
    value=1.0
)

# Quy đổi
ounce_to_gram = 31.1035

price_per_gram_usd = gold_price / ounce_to_gram
price_per_gram_vnd = price_per_gram_usd * exchange_rate

total_usd = price_per_gram_usd * grams
total_vnd = price_per_gram_vnd * grams

if st.button("Tính giá"):
    st.success("Kết quả")

    st.write(f"Giá mỗi gram vàng: {price_per_gram_usd:,.2f} USD")
    st.write(f"Giá mỗi gram vàng: {price_per_gram_vnd:,.0f} VND")

    st.write(f"Giá trị {grams} gram vàng:")
    st.write(f"{total_usd:,.2f} USD")
    st.write(f"{total_vnd:,.0f} VND")
