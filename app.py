import streamlit as st

st.set_page_config(
    page_title="AI Drug Interaction Checker",
    page_icon="💊"
)

st.title("💊 AI Drug Interaction Checker")
st.write("Check possible interactions between two medicines.")

st.warning(
    "⚠️ Educational Project Only: This application does not replace a doctor or pharmacist."
)

drug1 = st.text_input("Enter First Medicine Name")
drug2 = st.text_input("Enter Second Medicine Name")

# Sample interaction database
interactions = {
    ("warfarin", "aspirin"): (
        "HIGH RISK",
        "These medicines may increase the risk of bleeding."
    ),
    ("ibuprofen", "aspirin"): (
        "MODERATE RISK",
        "Taking these together may increase stomach bleeding risk."
    ),
    ("paracetamol", "warfarin"): (
        "MODERATE RISK",
        "Frequent use together may affect bleeding risk."
    ),
}

if st.button("🔍 Check Interaction"):
    
    if not drug1 or not drug2:
        st.error("Please enter both medicine names.")
    
    elif drug1.lower() == drug2.lower():
        st.warning("Please enter two different medicines.")
    
    else:
        d1 = drug1.lower().strip()
        d2 = drug2.lower().strip()

        result = interactions.get((d1, d2)) or interactions.get((d2, d1))

        if result:
            risk, message = result

            if risk == "HIGH RISK":
                st.error(f"⚠️ Risk Level: {risk}")

            else:
                st.warning(f"⚠️ Risk Level: {risk}")

            st.write(message)

        else:
            st.success("No interaction was found in this project's sample database.")
            st.info(
                "This does not guarantee that the medicines are safe to take together. "
                "Please consult a doctor or pharmacist."
            )

st.divider()

st.subheader("About This Project")
st.write(
    "This AI-based Drug Interaction Checker helps users identify possible "
    "medicine interactions and provides basic risk information."
)
