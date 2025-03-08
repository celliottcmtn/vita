import streamlit as st
import pandas as pd
from simplified_supplement_data import get_supplement_data, get_interactions_data, get_age_health_concerns

# Set page configuration
st.set_page_config(
    page_title="Supplement Advisor",
    page_icon="💊",
    layout="wide"
)

# Load data
supplements_data = get_supplement_data()
interactions_data = get_interactions_data()
age_health_concerns = get_age_health_concerns()

def main():
    st.title("Personalized Vitamin & Supplement Advisor")
    st.markdown("""
    This application provides personalized supplement recommendations based on your age, gender, and health concerns.
    
    **Disclaimer:** This tool provides general information only and is not a substitute for professional medical advice.
    Always consult with a healthcare provider before starting any supplement regimen.
    """)
    
    # User information
    st.header("Your Information")
    col1, col2 = st.columns(2)
    
    with col1:
        age_group = st.selectbox(
            "Select your age group:",
            ["20s", "30s", "40s", "50s", "60s", "70plus"]
        )
        
    with col2:
        gender = st.selectbox(
            "Select your gender:",
            ["female", "male", "prefer_not_to_say"]
        )
    
    # Health concerns
    st.header("Health Concerns")
    
    # Get recommended concerns for this age group and gender
    recommended_concerns = age_health_concerns.get(age_group, {}).get(gender, [])
    
    # Create a readable mapping for display
    concern_mapping = {
        "bone_health": "Bone Health",
        "immune_support": "Immune System Support",
        "depression": "Mood Support/Depression",
        "muscle_cramps": "Muscle Cramps",
        "sleep_issues": "Sleep Issues",
        "stress": "Stress Management",
        "heart_health": "Heart Health",
        "joint_pain": "Joint Pain",
        "cognitive_function": "Cognitive Function",
        "fatigue": "Fatigue/Energy Levels",
        "iron_deficiency": "Iron Deficiency",
        "skin_health": "Skin Health",
        "longevity": "Longevity/Anti-Aging",
        "reproductive_health": "Reproductive Health",
        "energy_levels": "Energy Levels",
        "fitness_performance": "Fitness Performance",
        "weight_management": "Weight Management",
        "prostate_health": "Prostate Health",
        "hormone_balance": "Hormone Balance"
    }
    
    # Convert technical terms to readable format for display
    selected_concerns = []
    
    # Display checkboxes for concerns
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Common Concerns For Your Profile")
        for concern in recommended_concerns:
            label = concern_mapping.get(concern, concern.replace("_", " ").title())
            if st.checkbox(label, value=False, key=f"rec_{concern}"):
                selected_concerns.append(concern)
    
    with col2:
        # Extract all health concerns from supplements
        all_concerns = set()
        for supplement in supplements_data.values():
            for concern in supplement["recommended_for"]["health_concerns"]:
                all_concerns.add(concern)
                
        other_concerns = [c for c in all_concerns if c not in recommended_concerns]
        st.subheader("Other Health Concerns")
        for concern in other_concerns:
            label = concern_mapping.get(concern, concern.replace("_", " ").title())
            if st.checkbox(label, value=False, key=f"other_{concern}"):
                selected_concerns.append(concern)
    
    # Current medications
    st.subheader("Current Medications")
    medications = st.text_input("List any medications you are currently taking (separated by commas):")
    
    # Generate recommendations button
    if st.button("Generate Recommendations"):
        if not selected_concerns:
            st.warning("Please select at least one health concern for personalized recommendations.")
        else:
            st.success("Based on your selections, here are your personalized supplement recommendations:")
            
            # Get recommendations
            recommended_supplements = {}
            for supp_id, supplement in supplements_data.items():
                # Check if supplement is recommended for this age group and gender
                if (age_group in supplement["recommended_for"]["age_groups"] and
                    gender in supplement["recommended_for"]["genders"]):
                    
                    # Check if any health concerns match
                    matching_concerns = [concern for concern in selected_concerns 
                                        if concern in supplement["recommended_for"]["health_concerns"]]
                    
                    if matching_concerns:
                        recommended_supplements[supp_id] = {
                            "supplement": supplement,
                            "matching_concerns": matching_concerns
                        }
            
            # Display recommendations
            for supp_id, data in recommended_supplements.items():
                supplement = data["supplement"]
                matching_concerns = data["matching_concerns"]
                
                # Format concerns for display
                concern_display = [concern_mapping.get(c, c.replace("_", " ").title()) for c in matching_concerns]
                
                with st.expander(f"**{supplement['name']}**"):
                    st.markdown(f"**Benefits**: {supplement['benefits']}")
                    st.markdown(f"**Recommended for**: {', '.join(concern_display)}")
                    st.markdown(f"**Suggested dosage**: {supplement['dosage'].get(age_group, 'Not specified')}")
                    
                    # Contraindications
                    if supplement.get("contraindications"):
                        contraindications = [c.replace("_", " ").title() for c in supplement.get("contraindications", [])]
                        st.markdown(f"**Use caution if you have**: {', '.join(contraindications)}")
                    
                    # Forms
                    if "importance_tier" in supplement:
                        st.markdown("### Recommended Forms")
                        
                        essential = supplement["importance_tier"].get("essential", {})
                        good = supplement["importance_tier"].get("good", {})
                        ideal = supplement["importance_tier"].get("ideal", {})
                        
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            st.markdown("**Essential**")
                            if essential:
                                st.markdown(f"Form: {essential.get('form', 'N/A')}")
                                st.markdown(f"Note: {essential.get('note', 'N/A')}")
                        
                        with col2:
                            st.markdown("**Good Value**")
                            if good:
                                st.markdown(f"Form: {good.get('form', 'N/A')}")
                                st.markdown(f"Note: {good.get('note', 'N/A')}")
                        
                        with col3:
                            st.markdown("**Ideal Choice**")
                            if ideal:
                                st.markdown(f"Form: {ideal.get('form', 'N/A')}")
                                st.markdown(f"Note: {ideal.get('note', 'N/A')}")
                                
                    # Sources
                    st.markdown("### Sources")
                    for source in supplement.get("sources", []):
                        st.markdown(f"- [{source}]({source})")
            
            # Check if no recommendations found
            if not recommended_supplements:
                st.warning("No specific supplements match your selected health concerns.")

if __name__ == "__main__":
    main()
