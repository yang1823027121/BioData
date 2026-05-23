from unittest import result

import streamlit as st

st.title("Simple calculater App")

n1 = st.number_input("Enter a number")
n2 = st.number_input("Enter a number")

operation = st.selectbox("Select an operation","Add","Subtract","Multiply","Divide")

if operation == "Add":
    result1 = n1 + n2
    st.success(f"{n1} +{n2}={result1}")
elif operation == "Subtract":
    result1 = n1 - n2
    st.success(f"{n1} - {n2} = {result1}")
elif operation == "Multiply":
    result1 = n1 * n2
    st.success(f"{n1} * {n2} = {result1}")
elif operation == "Divide":
    if n2==0:
        st.error("You can't divide by zero")
    else:
        result1 = n1 / n2
        st.success(f"{n1} / {n2} = {result1}")