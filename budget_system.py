import streamlit as st
import pandas as pd
from datetime import date
from pathlib import Path

DATA_FILE = Path("expenses.csv")

def load_expenses():
    if DATA_FILE.exists():
        df = pd.read_csv(DATA_FILE, parse_dates=["Date"])
        return df
    return pd.DataFrame(columns=["Date", "Item", "Amount (RM)"])

def save_expenses(df: pd.DataFrame):
    df.to_csv(DATA_FILE, index=False)

st.title("💸 Smart Budgeting System")
st.write("### 🧾 Input Expense Data")

if "df" not in st.session_state:
    st.session_state.df = load_expenses()

with st.form("expense_form", clear_on_submit=True):
    c1, c2, c3, c4 = st.columns([1, 2, 1, 1])
    with c1:
        d = st.date_input("Date", value=date.today(), format="DD/MM/YYYY")
    with c2:
        item = st.text_input("Item")
    with c3:
        amount = st.number_input("Amount (RM)", min_value=0.0, step=0.1)
    with c4:
        submitted = st.form_submit_button("Add")

    if submitted and item.strip():
        new_row = pd.DataFrame([{
            "Date": pd.to_datetime(d),
            "Item": item,
            "Amount (RM)": amount
        }])
        st.session_state.df = pd.concat([st.session_state.df, new_row], ignore_index=True)
        save_expenses(st.session_state.df)  # ✅ persist to disk
    elif submitted:
        st.warning("Please enter an item name.")

df = st.session_state.df.copy()

if not df.empty:
    df["Date"] = pd.to_datetime(df["Date"])
    min_d, max_d = df["Date"].min().date(), df["Date"].max().date()
    start_d, end_d = st.date_input("📅 Filter by date range", (min_d, max_d))

    if isinstance(start_d, tuple) or isinstance(start_d, list):
        start_d, end_d = start_d[0], start_d[1]
    mask = (df["Date"].dt.date >= start_d) & (df["Date"].dt.date <= end_d)
    df_filtered = df.loc[mask].sort_values("Date").reset_index(drop=True)
else:
    df_filtered = df

st.write("### 📊 Expense History")
st.dataframe(df_filtered, use_container_width=True)

total = df_filtered["Amount (RM)"].sum() if not df_filtered.empty else 0.0
st.markdown(f"### 💰 Total Spent: RM {total:.2f}")

colA, colB, colC = st.columns(3)
with colA:
    st.download_button("⬇️ Export CSV", st.session_state.df.to_csv(index=False), "expenses.csv", "text/csv")
with colB:
    if st.button("🗑️ Clear history"):
        st.session_state.df = st.session_state.df.iloc[0:0]
        save_expenses(st.session_state.df)
        st.success("History cleared.")
        st.rerun()
with colC:
    if not df_filtered.empty:
        monthly = (df_filtered
                   .assign(month=lambda x: x["Date"].dt.to_period("M").astype(str))
                   .groupby("month", as_index=False)["Amount (RM)"].sum())
        st.write("### 📅 Monthly Totals (Table)")
        st.dataframe(monthly, use_container_width=True)


st.write("### 📈 Visualizations")

if not df_filtered.empty:
    daily = df_filtered.groupby("Date", as_index=False)["Amount (RM)"].sum()
    daily = daily.sort_values("Date")
    daily["Cumulative"] = daily["Amount (RM)"].cumsum()

    st.subheader("Spending Over Time")
    st.line_chart(daily.set_index("Date")[["Amount (RM)", "Cumulative"]])

    monthly_chart = (df_filtered
                     .assign(Month=df_filtered["Date"].dt.to_period("M").astype(str))
                     .groupby("Month", as_index=False)["Amount (RM)"].sum()
                     .sort_values("Month"))
    st.subheader("Monthly Totals")
    st.bar_chart(monthly_chart.set_index("Month")["Amount (RM)"])

    top_items = (df_filtered
                 .groupby("Item", as_index=False)["Amount (RM)"].sum()
                 .sort_values("Amount (RM)", ascending=False)
                 .head(10))
    if not top_items.empty:
        st.subheader("Top 10 Items")
        st.bar_chart(top_items.set_index("Item")["Amount (RM)"])
else:
    st.info("Add a few expenses to see charts here.")
