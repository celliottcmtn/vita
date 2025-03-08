import streamlit as st
import pandas as pd
from supplement_data import get_supplement_data, get_interactions_data, get_age_health_concerns

# Set page configuration
st.set_page_config(
    page_title="Supplement Advisor",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load Data
def load_data():
    supplements_data = get_supplement_data()
    interactions_data = get_interactions_data()
    age_health_concerns = get_age_health_concerns()
    return supplements_data, interactions_data, age_health_concerns

# UI Functions
def display_header():
    st.title("Personalized Vitamin & Supplement Advisor")
    st.markdown("""
    This application provides personalized supplement recommendations based on your age, gender, and health concerns.
    
    **Disclaimer:** This tool provides general information only and is not a substitute for professional medical advice.
    Always consult with a healthcare provider before starting any supplement regimen.
    """)

def get_user_info():
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
    
    return age_group, gender

def get_health_concerns(all_supplements, age_health_concerns, age_group, gender):
    # Extract all possible health concerns from the supplement data
    all_health_concerns = set()
    for supplement in all_supplements.values():
        for concern in supplement["recommended_for"]["health_concerns"]:
            all_health_concerns.add(concern)
    
    # Convert to list and sort alphabetically
    all_health_concerns = sorted(list(all_health_concerns))
    
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
        "cognitive_function": "Cognitive Function/Brain Health",
        "fatigue": "Fatigue/Energy Levels",
        "iron_deficiency": "Iron Deficiency",
        "skin_health": "Skin Health",
        "longevity": "Longevity/Anti-Aging",
        "reproductive_health": "Reproductive Health",
        "energy_levels": "Energy Levels",
        "fitness_performance": "Fitness Performance",
        "wound_healing": "Wound Healing",
        "digestive_issues": "Digestive Issues",
        "antibiotic_recovery": "Antibiotic Recovery",
        "vegetarian_vegan": "Vegetarian/Vegan Diet",
        "anemia": "Anemia",
        "heavy_periods": "Heavy Periods",
        "eye_health": "Eye Health",
        "alcoholism_recovery": "Alcoholism Recovery",
        "nerve_health": "Nerve Health",
        "muscle_function": "Muscle Function",
        "inflammation": "Inflammation",
        "prostate_health": "Prostate Health",
        "hormone_balance": "Hormone Balance",
        "weight_management": "Weight Management"
    }
    
    # Convert technical terms to readable format for display
    display_concerns = {concern: concern_mapping.get(concern, concern.replace("_", " ").title()) 
                       for concern in all_health_concerns}
    
    # Create two columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Common Health Concerns")
        # Show recommended concerns first with pre-selected checkboxes
        selected_concerns = []
        for concern in recommended_concerns:
            if concern in display_concerns:
                label = display_concerns[concern]
                if st.checkbox(label, value=False, key=f"rec_{concern}"):
                    selected_concerns.append(concern)
    
    with col2:
        st.subheader("Additional Health Concerns")
        # Show other concerns
        other_concerns = [c for c in all_health_concerns if c not in recommended_concerns]
        for concern in other_concerns:
            label = display_concerns[concern]
            if st.checkbox(label, value=False, key=f"other_{concern}"):
                selected_concerns.append(concern)
                
    # Input for medications
    st.subheader("Current Medications")
    medications = st.text_input("List any medications you are currently taking (separated by commas):")
    
    return selected_concerns, medications

def get_recommended_supplements(supplements_data, age_group, gender, health_concerns):
    recommended = {}
    
    for supp_id, supplement in supplements_data.items():
        # Check if supplement is recommended for this age group and gender
        if (age_group in supplement["recommended_for"]["age_groups"] and
            gender in supplement["recommended_for"]["genders"]):
            
            # Check if any health concerns match
            matching_concerns = [concern for concern in health_concerns 
                                if concern in supplement["recommended_for"]["health_concerns"]]
            
            if matching_concerns:
                # Calculate a relevance score based on how many concerns match
                relevance = len(matching_concerns) / len(health_concerns) if health_concerns else 0
                recommended[supp_id] = {
                    "supplement": supplement,
                    "matching_concerns": matching_concerns,
                    "relevance": relevance
                }
    
    # Sort by relevance score
    sorted_recommendations = dict(sorted(recommended.items(), 
                                 key=lambda x: x[1]["relevance"], 
                                 reverse=True))
    
    return sorted_recommendations

def check_interactions(recommendations, interactions_data, medications):
    """Check for potential interactions between recommended supplements and with medications."""
    
    potential_interactions = {}
    
    # Check supplement-to-supplement interactions
    supplement_ids = list(recommendations.keys())
    
    for i, supp_id in enumerate(supplement_ids):
        interactions = []
        
        # Check against interactions data
        if supp_id in interactions_data:
            for interacting_supp in interactions_data[supp_id]:
                if interacting_supp in supplement_ids:
                    interactions.append({
                        "type": "supplement",
                        "name": recommendations[interacting_supp]["supplement"]["name"],
                        "note": "May reduce absorption when taken together. Take at least 2 hours apart."
                    })
        
        # Check against medication interactions
        if medications:
            med_list = [med.strip().lower() for med in medications.split(",")]
            supp_data = recommendations[supp_id]["supplement"]
            
            for med in med_list:
                for interaction in supp_data.get("interactions", []):
                    # Simple keyword matching (in a real app, would use a more sophisticated approach)
                    if med in interaction or interaction in med:
                        interactions.append({
                            "type": "medication",
                            "name": med,
                            "note": f"Potential interaction with {med}. Consult healthcare provider."
                        })
        
        if interactions:
            potential_interactions[supp_id] = interactions
    
    return potential_interactions

def display_timing_guide(recommendations):
    st.header("Supplement Timing Guide")
    
    if not recommendations:
        return
    
    # Create general timing categories
    timing_categories = {
        "morning_with_food": [],
        "morning_empty_stomach": [],
        "afternoon": [],
        "evening_with_food": [],
        "evening_empty_stomach": [],
        "bedtime": []
    }
    
    # Simple rules for categorizing supplements
    for supp_id, rec_data in recommendations.items():
        supplement = rec_data["supplement"]
        name = supplement["name"]
        
        if name in ["Iron"]:
            timing_categories["morning_empty_stomach"].append(name)
        elif name in ["Vitamin D", "Vitamin B12", "Omega-3 Fatty Acids", "Vitamin B1 (Thiamine)", "Vitamin A"]:
            timing_categories["morning_with_food"].append(name)
        elif name in ["Probiotics"]:
            timing_categories["morning_empty_stomach"].append(name)
        elif name in ["Vitamin C"]:
            timing_categories["afternoon"].append(name)
        elif name in ["Calcium"]:
            timing_categories["evening_with_food"].append(name)
        elif name in ["Magnesium"]:
            timing_categories["bedtime"].append(name)
        elif name in ["Zinc"]:
            timing_categories["morning_with_food"].append(name)
        else:
            # Default to morning with food if no specific rule
            timing_categories["morning_with_food"].append(name)
    
    # Display timing recommendations
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Morning")
        if timing_categories["morning_empty_stomach"]:
            st.markdown("**On empty stomach:**")
            for supp in timing_categories["morning_empty_stomach"]:
                st.markdown(f"- {supp}")
        
        if timing_categories["morning_with_food"]:
            st.markdown("**With breakfast:**")
            for supp in timing_categories["morning_with_food"]:
                st.markdown(f"- {supp}")
        
        st.subheader("Afternoon")
        if timing_categories["afternoon"]:
            for supp in timing_categories["afternoon"]:
                st.markdown(f"- {supp}")
    
    with col2:
        st.subheader("Evening")
        if timing_categories["evening_with_food"]:
            st.markdown("**With dinner:**")
            for supp in timing_categories["evening_with_food"]:
                st.markdown(f"- {supp}")
        
        if timing_categories["evening_empty_stomach"]:
            st.markdown("**After dinner (2+ hours):**")
            for supp in timing_categories["evening_empty_stomach"]:
                st.markdown(f"- {supp}")
        
        st.subheader("Bedtime")
        if timing_categories["bedtime"]:
            for supp in timing_categories["bedtime"]:
                st.markdown(f"- {supp}")
    
    # General timing advice
    st.markdown("""
    ### General Timing Tips:
    1. **Fat-soluble vitamins** (A, D, E, K) are best absorbed with fatty meals
    2. **Iron** absorbs better on an empty stomach, but can cause stomach upset (take with vitamin C to enhance absorption)
    3. **B vitamins** may boost energy, so taking them late in the day might affect sleep
    4. **Calcium and magnesium** can compete for absorption, so take at different times
    5. **Probiotics** are often best taken in the morning on an empty stomach
    """)

def create_supplement_plan(recommendations, interactions, age_group):
    st.header("Your Personalized Supplement Plan")
    
    if not recommendations:
        st.warning("No specific supplements recommended based on your selections.")
        return
    
    # Create formatted plan
    plan_text = "# Your Personalized Supplement Plan\n\n"
    
    for supp_id, rec_data in recommendations.items():
        supplement = rec_data["supplement"]
        
        plan_text += f"### {supplement['name']}\n"
        plan_text += f"- **Dosage:** {supplement['dosage'].get(age_group, 'Consult healthcare provider')}\n"
        plan_text += f"- **Benefits:** {supplement['benefits']}\n"
        
        # Add budget recommendation
        if "budget_tier" in supplement:
            good_option = supplement["budget_tier"].get("good", {})
            if good_option:
                plan_text += f"- **Recommended form:** {good_option.get('form', 'Standard form')}\n"
                plan_text += f"- **Typical price:** {good_option.get('price_range', 'Varies')}\n"
        
        if supp_id in interactions and interactions[supp_id]:
            plan_text += "- **Special Considerations:**\n"
            for interaction in interactions[supp_id]:
                plan_text += f"  - *{interaction['name']}*: {interaction['note']}\n"
        
        plan_text += "\n"
    
    # Add general advice
    plan_text += """## General Recommendations

1. **Start gradually**: Introduce one supplement at a time to monitor for any adverse reactions.
2. **Consistency matters**: Take supplements consistently at the same time(s) each day.
3. **Follow timing guidelines**: Some supplements are better absorbed at specific times or with/without food.
4. **Regular reassessment**: Reassess your supplement needs every 6-12 months or with any significant health changes.
5. **Quality matters**: Look for supplements that have been third-party tested.

## Important Disclaimer
This supplement plan is provided for informational purposes only and is not a substitute for professional medical advice. Always consult with a healthcare provider before starting any supplement regimen, especially if you have health conditions or take medications.
"""
    
    # Display the plan and offer download
    st.markdown(plan_text)
    
    # In a real app, you would generate a PDF here
    st.download_button(
        label="Download Supplement Plan",
        data=plan_text,
        file_name="personalized_supplement_plan.txt",
        mime="text/plain"
    )

def display_recommendations(recommendations, interactions, age_group):
    st.header("Your Personalized Supplement Recommendations")
    
    if not recommendations:
        st.warning("No specific supplements recommended based on your selections.")
        return
    
    # Create expandable sections for each recommendation
    for supp_id, rec_data in recommendations.items():
        supplement = rec_data["supplement"]
        matching_concerns = rec_data["matching_concerns"]
        
        # Format concerns for display
        concern_display = [c.replace("_", " ").title() for c in matching_concerns]
        
        with st.expander(f"**{supplement['name']}**"):
            # Main information
            st.markdown(f"**Benefits**: {supplement['benefits']}")
            st.markdown(f"**Recommended for**: {', '.join(concern_display)}")
            st.markdown(f"**Suggested dosage**: {supplement['dosage'].get(age_group, 'Not specified')}")
            
            # Interaction warnings
            if supp_id in interactions:
                st.markdown("### ⚠️ Potential Interactions")
                for interaction in interactions[supp_id]:
                    st.markdown(f"- **{interaction['name']}**: {interaction['note']}")
            
            # Contraindications
            if supplement.get("contraindications"):
                contraindications = [c.replace("_", " ").title() for c in supplement.get("contraindications", [])]
                st.markdown(f"**Use caution if you have**: {', '.join(contraindications)}")
            
            # Display budget tiers if available
            if "budget_tier" in supplement:
                st.markdown("### Budget-Friendly Options")
                
                essential = supplement["budget_tier"].get("essential", {})
                good = supplement["budget_tier"].get("good", {})
                ideal = supplement["budget_tier"].get("ideal", {})
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.markdown("**Essential**")
                    if essential:
                        st.markdown(f"Form: {essential.get('form', 'N/A')}")
                        st.markdown(f"Price: {essential.get('price_range', 'N/A')}")
                
                with col2:
                    st.markdown("**Good Value**")
                    if good:
                        st.markdown(f"Form: {good.get('form', 'N/A')}")
                        st.markdown(f"Price: {good.get('price_range', 'N/A')}")
                
                with col3:
                    st.markdown("**Ideal Choice**")
                    if ideal:
                        st.markdown(f"Form: {ideal.get('form', 'N/A')}")
                        st.markdown(f"Price: {ideal.get('price_range', 'N/A')}")
                        
            # Sources
            st.markdown("### Sources")
            for source in supplement.get("sources", []):
                st.markdown(f"- [{source}]({source})")
