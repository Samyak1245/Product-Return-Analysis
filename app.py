import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Product Return Analysis",
    layout="wide"
)

st.title("Product Return Analysis System")
st.write(
    "Analyze product returns, customer complaints, "
    "and category-wise return patterns."
)

df = pd.read_csv("product_returns.csv")

df["Product_Category"] = (
    df["Product_Category"].astype(str).str.strip()
)

df["Return_Status"] = (
    df["Return_Status"].astype(str).str.strip().str.title()
)

df["Return_Reason"] = (
    df["Return_Reason"].fillna("Unknown").astype(str).str.strip()
)

df = df.drop_duplicates(subset=["Order_ID"])
df = df[df["Return_Status"].isin(["Yes", "No"])]

categories = sorted(df["Product_Category"].unique())

selected_categories = st.multiselect(
    "Select Product Categories",
    categories,
    default=categories
)

filtered_df = df[
    df["Product_Category"].isin(selected_categories)
]

total_orders = len(filtered_df)
returned_orders = (
    filtered_df["Return_Status"] == "Yes"
).sum()

return_rate = (
    returned_orders / total_orders * 100
    if total_orders else 0
)

col1, col2, col3 = st.columns(3)

col1.metric("Total Orders", total_orders)
col2.metric("Returned Orders", int(returned_orders))
col3.metric("Return Rate", f"{return_rate:.2f}%")

st.subheader("Category-wise Return Rate")

if not filtered_df.empty:
    summary = filtered_df.groupby("Product_Category").agg(
        Total=("Order_ID", "count"),
        Returned=(
            "Return_Status",
            lambda x: (x == "Yes").sum()
        )
    )

    summary["Return Rate (%)"] = (
        summary["Returned"] / summary["Total"] * 100
    )

    fig, ax = plt.subplots(figsize=(9, 5))

    sns.barplot(
        data=summary.reset_index(),
        x="Product_Category",
        y="Return Rate (%)",
        ax=ax
    )

    ax.set_title("Return Rate by Product Category")
    ax.set_xlabel("Product Category")
    ax.set_ylabel("Return Rate (%)")

    st.pyplot(fig)

st.subheader("Return Reasons")

returned_df = filtered_df[
    filtered_df["Return_Status"] == "Yes"
]

if not returned_df.empty:
    reason_counts = returned_df["Return_Reason"].value_counts()

    fig, ax = plt.subplots(figsize=(9, 5))

    reason_counts.plot(kind="bar", ax=ax)

    ax.set_xlabel("Return Reason")
    ax.set_ylabel("Number of Returns")
    ax.set_title("Distribution of Return Reasons")

    plt.xticks(rotation=35, ha="right")
    plt.tight_layout()

    st.pyplot(fig)
else:
    st.info("No returned orders found for the selected categories.")

st.subheader("Order Data")
st.dataframe(filtered_df, use_container_width=True)