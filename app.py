import streamlit as st

st.set_page_config(page_title="Lagrange Interpolation Solver", layout="wide")

st.title("📘 Lagrange Interpolation Solver")

st.markdown(r"""
### Formula

\[
P(x)=\sum_{i=0}^{n} y_i
\prod_{j=0,j\ne i}^{n}
\frac{(x-x_j)}{(x_i-x_j)}
\]

Enter x-values, y-values and the interpolation point.
""")

x_input = st.text_input(
    "X Values (comma separated)",
    "5,6,9,11"
)

y_input = st.text_input(
    "Y Values (comma separated)",
    "12,13,14,16"
)

xp = st.number_input(
    "Find y at x =",
    value=10.0
)

if st.button("Calculate"):

    try:
        x = [float(i.strip()) for i in x_input.split(",")]
        y = [float(i.strip()) for i in y_input.split(",")]

        if len(x) != len(y):
            st.error("Number of x values and y values must be equal.")
            st.stop()

        n = len(x)

        result = 0
        steps = []

        for i in range(n):

            term = y[i]

            formula = f"L{i}(x) = "

            for j in range(n):
                if i != j:
                    formula += f"(({xp}-{x[j]})/({x[i]}-{x[j]})) "
                    term *= (xp - x[j]) / (x[i] - x[j])

            contribution = term

            steps.append(
                {
                    "Basis": formula,
                    "Contribution": contribution
                }
            )

            result += contribution

        st.subheader("Step-by-Step Calculation")

        for k, step in enumerate(steps):
            st.markdown(f"**Term {k+1}**")
            st.code(step["Basis"])
            st.write(f"Contribution = {step['Contribution']:.6f}")

        st.success(f"Interpolated Value = {result:.6f}")

    except Exception as e:
        st.error(f"Error: {e}")